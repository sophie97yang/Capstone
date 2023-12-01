from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Trip,db,User,TripDetail,Expense
from ..forms.trip_form import TripForm
from ..forms.add_user_form import AddUserForm
from .AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3
from datetime import datetime

trip_routes = Blueprint('trips', __name__)

#can access user trips through querying for user

#get a trip details by tripId
@trip_routes.route('/<int:id>',methods=['GET'])
@login_required
def get_trip(id):
    trip = Trip.query.get(id)
    return {"trip":trip.to_dict_trips()}

#create a trip
@trip_routes.route('/new',methods=['POST'])
@login_required
def create_trip():
    form =TripForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        trip = Trip(
            name=form.data['name'],
            description=form.data['description'],
            city=form.data['city'],
            state=form.data['state'],
            start_date=form.data['start_date'],
            end_date=form.data['end_date']
        )

        image = form.data["image"]
        if image:
             image.filename = get_unique_filename(image.filename)
             uploadTripImage = upload_file_to_s3(image)
             if "url" not in uploadTripImage:
                print(uploadTripImage)
                return uploadTripImage
             else:
                trip.image = uploadTripImage["url"]

        trip_detail = TripDetail(settled=False,creator=True)
        trip_detail.user=current_user
        trip.users.append(trip_detail)
        db.session.add(trip)
        db.session.commit()
        return {"trip":trip_detail.to_dict_trips()}
    return {"errors":form.errors},400

#update a trip
@trip_routes.route('/<int:id>/edit',methods=['PUT'])
@login_required
def update_trip(id):
    trip = Trip.query.get(id)

    if trip is None:
        return {'errors': "Trip doesn't exist"}, 404
    form =TripForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        #convert start and end date to date objects
        new_start = form.data['start_date']
        print('NEW STARTTTT',type(new_start))

        trip.name=form.data['name'],
        trip.description=form.data['description'],
        trip.city=form.data['city'],
        trip.state=form.data['state'],
        trip.start_date=form.data['start_date'],
        trip.end_date=form.data['end_date']

        #updating trip image
        image = form.data["image"]
        if image:
             image.filename = get_unique_filename(image.filename)
             if trip.image:
                    remove_file_from_s3(trip.image)
             uploadTripImage = upload_file_to_s3(image)
             if "url" not in uploadTripImage:
                print(uploadTripImage)
                return uploadTripImage
             else:
                trip.image = uploadTripImage["url"]
        db.session.commit()
        return {"trip":trip.to_dict()}
    return {"errors":form.errors},400

# add new users to a trip
@trip_routes.route('/<int:id>/add/users',methods=['POST'])
@login_required
def add_trip_users(id):
    trip = Trip.query.get(id)
    if trip is None:
        return {'errors': "Trip doesn't exist"}, 404

    form =AddUserForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        trip_detail_list=[]

        email_1 = form.data['email_1']
        user_1 = User.query.filter_by(email=email_1).first()
        print('USEERR',user_1)
        if user_1:
            trip_detail_1 = TripDetail(settled=False,creator=False)
            trip_detail_1.user=user_1
            # trip_detail_list.append(trip_detail_1)
            trip.users.append(trip_detail_1)

        email_2 = form.data['email_2']
        user_2 = User.query.filter_by(email=email_2).first()
        if user_2:
            trip_detail_2 = TripDetail(settled=False,creator=False)
            trip_detail_2.user=user_2
            # trip_detail_list.append(trip_detail_2)
            trip.users.append(trip_detail_2)

        email_3 = form.data['email_3']
        user_3 = User.query.filter_by(email=email_3).first()
        if user_3:
            trip_detail_3 = TripDetail(settled=False,creator=False)
            trip_detail_3.user=user_3
            # trip_detail_list.append(trip_detail_3)
            trip.users.append(trip_detail_3)

        # trip.users.append(trip_detail_list)
        db.session.commit()
        return {"trip":trip.to_dict()}
    else:
        return  {"errors":form.errors},400

#delete trip
@trip_routes.route('<int:id>/delete',methods=['DELETE'])
@login_required
def delete_trip(id):
    trip = Trip.query.get(id)
    if not trip:
        return {'errors': "Trip doesn't exist"}, 404
    creator =[user for user in trip.users if user.creator][0]
    if creator.user_id!=current_user.id:
        return {"errors":"Forbidden"},403

    db.session.delete(trip)
    db.session.commit()

    return {'message': 'Deletion successful'}, 200

# get all expense details by trip id
@trip_routes.route('/<int:id>/expenses',methods=['GET'])
@login_required
def get_all_expenses_by_trip(id):
    print(id)
    expenses = Expense.query.order_by(Expense.expense_date).filter_by(trip_id=id).all()
    return {"expenses":[expense.to_dict() for expense in expenses]}
