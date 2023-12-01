from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Trip,db,User,TripDetail
from ..forms.trip_form import TripForm
from .AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

trip_routes = Blueprint('trips', __name__)

#can access user trips through querying for user

#get a trip details by tripId
@trip_routes.route('/<int:id>',methods=['GET'])
@login_required
def get_trip(id):
    trip = Trip.query.get(id)
    return {"trip":trip.to_dict_users()}

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

        return {"trip":trip.to_dict_users()}
    return {"errors":form.errors},400

# add new users to a trip
@trip_routes.route('/<int:id>/add/<int:user_id>',methods=['PUT'])
@login_required
def add_trip_users(id,user_id):
    trip = Trip.query.get(id)
    user = User.query.get(user_id)
    if not trip or not user:
        return {'errors': "Trip/User doesn't exist"}, 404

    trip_detail = TripDetail(settled=False)
    trip_detail.user=user
    trip.users.append(trip_detail)
    return {"trip":trip.to_dict()}

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
