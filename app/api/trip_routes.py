from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Trip,db,User,TripDetail,Expense,ExpenseDetail,ExpenseUpdateDetail,BetweenUserExpense,Itinerary
from ..forms.trip_form import TripForm
from ..forms.add_user_form import AddUserForm
from ..forms.expense_form import ExpenseForm
from ..forms.itinerary_form import ItineraryForm
from .AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3
from datetime import date,datetime

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

        # #convert start and end date to date objects
        # new_start = form.data['start_date']
        # print('NEW STARTTTT',new_start.date())

        trip.name=form.data['name']
        trip.description=form.data['description']
        trip.city=form.data['city']
        trip.state=form.data['state']
        trip.start_date=form.data['start_date']
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
        for detail in trip.users:
            if detail.user==user_1:
                return {"errors":f"{user_1.first_name} is already a collaborator of this trip"},400

        if user_1:
            trip_detail_1 = TripDetail(settled=False,creator=False)
            trip_detail_1.user=user_1
            # trip_detail_list.append(trip_detail_1)
            trip.users.append(trip_detail_1)

        email_2 = form.data['email_2']
        user_2 = User.query.filter_by(email=email_2).first()
        for detail in trip.users:
            if detail.user==user_2:
                return {"errors":f"{user_2.first_name} is already a collaborator of this trip"},400
        if user_2:
            trip_detail_2 = TripDetail(settled=False,creator=False)
            trip_detail_2.user=user_2
            # trip_detail_list.append(trip_detail_2)
            trip.users.append(trip_detail_2)

        email_3 = form.data['email_3']
        user_3 = User.query.filter_by(email=email_3).first()
        for detail in trip.users:
            if detail.user==user_3:
                return {"errors":f"{user_3.first_name} is already a collaborator of this trip"},400
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
@trip_routes.route('/<int:id>/delete',methods=['DELETE'])
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

# create an expense for a trip
@trip_routes.route('/<int:id>/expense/new',methods=['POST'])
@login_required
def create_expense(id):
    form =ExpenseForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        expense = Expense(
            name=form.data['name'],
            expense_date=form.data['expense_date'],
            split_type=form.data['split_type'],
            split_type_info=form.data['split_type_info'],
            category=form.data['category'],
            total=form.data['total']
        )
        db.session.add(expense)

        #expense payer is current user
        expense.payer = current_user

        #users involved
        trip = Trip.query.get(id)
        split_info = form.data['split_type_info']
        split_type = form.data['split_type']
        expense_detail_list = []
        # if users involved = All - iterate through all of trips users and create an expense detail
        if (form.data['users_id']=='All'):
            #users come in reg order
            index=0
            for trip_detail in trip.users:
                if split_type=='Equal':
                    price=float(form.data['total'])/len(trip.users)
                elif split_type=='Exact':
                    split_info = form.data['split_type_info'].split(',')
                    print('SPLIT_INFOO',split_info)
                    price=float(split_info.pop(index))
                    index+=1
                elif split_type=='Percentages':
                    split_info = form.data['split_type_info'].split(',')
                    price=(int(split_info.pop(index))/100)*float(form.data['total'])
                    index+=1
                #ADD/UPDATE EXPENSE RELATIONSHIP BETWEEN THE TWO USERS
                #check if there is already an existing expense relationship between two users in trip
                relationship_one = BetweenUserExpense.query.filter_by(user_one_id=current_user.id,user_two_id=trip_detail.user.id,trip_id=trip.id).first()
                relationship_two= BetweenUserExpense.query.filter_by(user_one_id=trip_detail.user.id,user_two_id=current_user.id,trip_id=trip.id).first()
                            # if a relationship is found
                if relationship_one or relationship_two:
                    if relationship_one:
                    #user_one=payer,user_two=user involved in expense
                    #user_one now is owed $
                        relationship_one.owed+=price
                    elif relationship_two:
                    #user_one=user involved in expense, user_two=payer
                    #user_one now owes money $
                        relationship_two.owes+=price
            #if there is no existing relationship,create one
                else:
                #user_one=payer,user_two=user involved in expense
                #user one now is owed $
                    relationship=BetweenUserExpense(user_one_id=current_user.id,
                                                user_two_id=trip_detail.user.id,
                                                trip_id=trip.id,
                                                owed= price
                                                )
                    db.session.add(relationship)

                expense_detail = ExpenseDetail(user_id=trip_detail.user.id,price=price)
                expense_detail_list.append(expense_detail)
        # else:
        else:
            users_involved = form.data['users_id'].split(',')
            index=0
            for user in users_involved:
                if split_type=='Equal':
                    price=float(form.data['total'])/len(users_involved)
                elif split_type=='Exact':
                    split_info = form.data['split_type_info'].split(',')
                    print('SPLIT_INFOO',split_info)
                    price=float(split_info.pop(index))
                    index+=1
                elif split_type=='Percentages':
                    split_info = form.data['split_type_info'].split(',')
                    price=(int(split_info.pop(index))/100)*float(form.data['total'])
                    index+=1
                #ADD/UPDATE EXPENSE RELATIONSHIP BETWEEN THE TWO USERS
                #check if there is already an existing expense relationship between two users in trip
                relationship_one = BetweenUserExpense.query.filter_by(user_one_id=current_user.id,user_two_id=int(user),trip_id=trip.id).first()
                relationship_two= BetweenUserExpense.query.filter_by(user_one_id=int(user),user_two_id=current_user.id,trip_id=trip.id).first()
                            # if a relationship is found
                if relationship_one or relationship_two:
                    if relationship_one:
                    #user_one=payer,user_two=user involved in expense
                    #user_one now is owed $
                        relationship_one.owed+=price
                    elif relationship_two:
                    #user_one=user involved in expense, user_two=payer
                    #user_one now owes money $
                        relationship_two.owes+=price
            #if there is no existing relationship,create one
                else:
                #user_one=payer,user_two=user involved in expense
                #user one now is owed $
                    relationship=BetweenUserExpense(user_one_id=current_user.id,
                                                user_two_id=int(user),
                                                trip_id=trip.id,
                                                owed= price
                                                )
                    db.session.add(relationship)
                expense_detail = ExpenseDetail(user_id=int(user),price=price)
                expense_detail_list.append(expense_detail)
        #attach all of expense details to expense
        expense.users = expense_detail_list
        #attach expense to trip
        trip.expenses.append(expense)
        db.session.commit()
        return {"trip":trip.to_dict(),"expense":expense.to_dict()}
    return {"errors":form.errors},400



#UPDATE AN EXPENSE
@trip_routes.route('/<int:id>/expense/<int:expenseId>/edit',methods=['PUT'])
@login_required
def update_expense(id,expenseId):
    form =ExpenseForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        expense = Expense.query.get(expenseId)
         # CHECK WHAT DIFFERENCES EXIST AND LOG THOSE CHANGES IN EXPENSE UPDATE DETAILS
        #categories for update:'split_type','total','name'
        details_changed=[]
        if expense.split_type!=form.data['split_type']:
            details_changed.append(['split_type',f'{expense.split_type},{form.data["split_type"]}'])
        if expense.total!=form.data['total']:
            details_changed.append(['total',f'{expense.total},{form.data["total"]}'])
        if expense.name!=form.data['name']:
            details_changed.append(['name',f'{expense.name},{form.data["name"]}'])

        #update details
        expense.name=form.data['name']
        expense.expense_date=form.data['expense_date']
        split_type=form.data['split_type']
        expense.split_type_info=form.data['split_type_info']
        expense.category=form.data['category']
        expense.total=form.data['total']

        #REMOVE THIS EXPENSE FOR EVERY USER ORIGINALLY INVOLVED - THIS NEW PRICE WILL GET ADDED BACK LATER
        trip = Trip.query.get(id)
        for user in expense.users:
            relationship_one = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==expense.payer_id and relationship.user_two_id==user.user_id]
            relationship_two = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==user.user_id and relationship.user_two_id==expense.payer_id]
            if len(relationship_one):
                relationship_one[0].owed-=user.price
            elif len(relationship_two):
                relationship_two[0].owes-=user.price

        #UPDATE EXPENSE DETAILS FOR USERS INVOLVED
        # CHECK IF EXPENSE DETAIL EXISTS
        # IF NOT CREATE A NEW ONE
        split_info = form.data['split_type_info']
        split_type = form.data['split_type']
        expense_detail_list = []
        # if users involved = All - iterate through all of trips users and create an expense detail
        if (form.data['users_id']=='All'):
            index=0
            for trip_detail in trip.users:
                if split_type=='Equal':
                    price=float(form.data['total'])/len(trip.users)
                elif split_type=='Exact':
                    split_info = form.data['split_type_info'].split(',')
                    print('SPLIT_INFOO',split_info)
                    price=float(split_info.pop(index))
                    index+=1
                elif split_type=='Percentages':
                    split_info = form.data['split_type_info'].split(',')
                    price=(int(split_info.pop(index))/100)*float(form.data['total'])
                    index+=1
                #ADD/UPDATE EXPENSE RELATIONSHIP BETWEEN THE TWO USERS
                #check if there is already an existing expense relationship between two users in trip -> LOOKING BETWEEN EXPENSE PAYER AND USERS INVOLVED
                relationship_one = BetweenUserExpense.query.filter_by(user_one_id=expense.payer_id,user_two_id=trip_detail.user.id,trip_id=trip.id).first()
                relationship_two= BetweenUserExpense.query.filter_by(user_one_id=trip_detail.user.id,user_two_id=expense.payer_id,trip_id=trip.id).first()
                            # if a relationship is found
                if relationship_one or relationship_two:
                    if relationship_one:
                    #user_one=payer,user_two=user involved in expense
                    #user_one now is owed $
                        relationship_one.owed+=price
                    elif relationship_two:
                    #user_one=user involved in expense, user_two=payer
                    #user_one now owes money $
                        relationship_two.owes+=price
            #if there is no existing relationship,create one
                else:
                #user_one=payer,user_two=user involved in expense
                #user one now is owed $
                    relationship=BetweenUserExpense(user_one_id=expense.payer_id,
                                                user_two_id=int(user),
                                                trip_id=trip.id,
                                                owed= price
                                                )
                    db.session.add(relationship)

                #check if expense detail already exists
                user_exists=False
                detail_found=None
                for detail in expense.users:
                    #if detail is found
                    if detail.user_id==trip_detail.user.id:
                        user_exists=True
                        detail_found=detail
                if user_exists:
                    detail_found.price=price
                    expense_detail_list.append(detail_found)
                else:
                    expense_detail = ExpenseDetail(user_id=trip_detail.user.id,price=price)
                    expense_detail_list.append(expense_detail)
        # else-SELECT USERS
        else:
            users_involved = form.data['users_id'].split(',')
            # # IF USERS INVOLVED IS LESS THAN EXPENSE.USERS (AKA A USER HAS BEEN REMOVED FROM THE EXPENSE),
            # # WE NEED TO REMOVE THAT EXPENSE FROM BETWEEN_USER_EXPENSE RECORD
            # # THIS INCLUDES IF THE UPDATE CHANGES FROM ALL USERS TO SELECT USERS
            # # THIS ALSO MEANS THAT THE PRICE CHANGES FOR OTHER USERS. ADJUST ACCORDINGLY
            # if len(users_involved)<len(expense.users):
            #     for user in expense.users:
            #         # if str(user.user_id) not in users_involved:
            #             #FIND EXPENSE RECORD
            #             #adjust prices for everyone else - remove old price from this record
            #         relationship_one = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==expense.payer_id and relationship.user_two_id==user.user_id]
            #         relationship_two = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==user.user_id and relationship.user_two_id==expense.payer_id]
            #         if len(relationship_one):
            #             relationship_one[0].owed-=user.price
            #         elif len(relationship_two):
            #             relationship_two[0].owes-=user.price
            # #if USERS INVOLVED IS GREATER THAN EXPENSE.USERS (AKA A USER HAS BEEN ADDED TO THE EXPENSE)
            # #WE NEED TO REMOVE EXPENSE ACCORDINGLY AS THE NEW PRICE WILL GET ADDED LATER
            # else:
            #     for user in users_involved:
            #         user_database = User.query.get(int(user))
            #         if user_database in expense.users:
            #             relationship_one = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==expense.payer_id and relationship.user_two_id==int(user)]
            #             relationship_two = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==int(user) and relationship.user_two_id==expense.payer_id]
            #             if len(relationship_one):
            #                 relationship_one[0].owed-=user.price
            #             elif len(relationship_two):
            #                 relationship_two[0].owes-=user.price

            index=0
            for user in users_involved:
                if split_type=='Equal':
                    price=float(form.data['total'])/len(users_involved)
                elif split_type=='Exact':
                    split_info = form.data['split_type_info'].split(',')
                    print('SPLIT_INFOO',split_info)
                    price=float(split_info.pop(index))
                    index+=1
                elif split_type=='Percentages':
                    split_info = form.data['split_type_info'].split(',')
                    price=(int(split_info.pop(index))/100)*float(form.data['total'])
                    index+=1
                #ADD/UPDATE EXPENSE RELATIONSHIP BETWEEN THE TWO USERS
                #check if there is already an existing expense relationship between two users in trip
                relationship_one = BetweenUserExpense.query.filter_by(user_one_id=expense.payer_id,user_two_id=int(user),trip_id=trip.id).first()
                relationship_two= BetweenUserExpense.query.filter_by(user_one_id=int(user),user_two_id=expense.payer_id,trip_id=trip.id).first()
                # if a relationship is found
                if relationship_one or relationship_two:
                    if relationship_one:
                    #user_one=payer,user_two=user involved in expense
                    #user_one now is owed $
                        relationship_one.owed+=price
                    elif relationship_two:
                    #user_one=user involved in expense, user_two=payer
                    #user_one now owes money $
                        relationship_two.owes+=price
            #if there is no existing relationship,create one
                else:
                #user_one=payer,user_two=user involved in expense
                #user one now is owed $
                    relationship=BetweenUserExpense(user_one_id=expense.payer_id,
                                                user_two_id=int(user),
                                                trip_id=trip.id,
                                                owed= price
                                                )
                    db.session.add(relationship)
                #check if expense detail already exists
                user_exists=False
                detail_found=None
                for detail in expense.users:
                    #if detail is found
                    if detail.user_id==int(user):
                        user_exists=True
                        detail_found=detail
                if user_exists:
                    detail_found.price=price
                    expense_detail_list.append(detail_found)
                else:
                    expense_detail = ExpenseDetail(user_id=int(user),price=price)
                    expense_detail_list.append(expense_detail)
        #attach all of expense details to expense
        #IMPORTANT DETAIL UPDATE USERS:
        if len(expense.users)!=len(expense_detail_list):
            details_changed.append(['users'])
        expense.users = expense_detail_list
        #attach expense to trip
        trip.expenses.append(expense)
        #if important details have been changed:
        if len(details_changed):
            #categories for update:'split_type','total','name','users'
            for change in details_changed:
                if change[0]!='users':
                    update_detail=ExpenseUpdateDetail(user_id=current_user.id,expense_id=expense.id,update_date=date.today(),update_type=change[0],update_info=change[1])
                    db.session.add(update_detail)
                else:
                    update_detail=ExpenseUpdateDetail(user_id=current_user.id,expense_id=expense.id,update_date=date.today(),update_type=change[0])
                    db.session.add(update_detail)
        db.session.commit()
        return {"trip":trip.to_dict()}
    return {"errors":form.errors},400

#settle a trip
#changed trip detail for the user to settled and set settled date
#change between user expenses for that user and all existing settlements to 0 owed, 0 owe
@trip_routes.route('/<int:id>/settle',methods=['PUT'])
@login_required
def settlement(id):
    trip = Trip.query.get(id)
    if not trip:
        return {"errors":"Trip not found"}
    user_settlements = [relationship for relationship in trip.between_user_expenses if (relationship.user_one.id==current_user.id or relationship.user_two.id==current_user.id) and not (relationship.user_one.id==current_user.id and relationship.user_two.id==current_user.id)]
    to_pay=[]
    #FILTER JUST SETTLEMENTS THAT USER HAS TO PAY
    for settlement in user_settlements:
        # related_user= settlement.user_one.id == current_user.id ? settlement.user_two : settlement.user_one,
        type=  "payer" if settlement.user_one.id==current_user.id and settlement.owed-settlement.owes>0  else "payee"
        if type=='payee':
            to_pay.append(settlement)


    trip_detail = TripDetail.query.filter_by(user_id=current_user.id,trip_id=id).first()
    if not trip_detail:
        return {"errors":"Trip doesn't exist for the user"}
    trip_detail.settled=True
    trip_detail.settled_date= date.today()

    #if user has to pay someone, those take priority in settlement
    if len(to_pay):
        for settlement in to_pay:
            settlement.owed=0
            settlement.owes=0
        db.session.commit()
        return {"trip":trip.to_dict()}
    #if user doesn't, they can record all the payments that someone owes them - it's up to the related user to settle
    else:
        for settlement in user_settlements:
            settlement.owed=0
            settlement.owes=0
        db.session.commit()
        return {"trip":trip.to_dict()}

#add a booking to a trip's itinerary
@trip_routes.route('/<int:id>/add_booking',methods=['POST'])
@login_required
def add_booking(id):
    trip = Trip.query.get(id)
    form = ItineraryForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        itinerary = Itinerary(
            booking_id = form.data['booking_id'],
            user_id = current_user.id,
            booking_date = datetime.now(),
            booking_startdate = form.data['booking_startdate'],
            booking_enddate = form.data['booking_enddate'],
            booking_time = form.data['booking_time'],
            expensed = form.data['expensed'],
            total= form.data['price'],
            people=form.data['people']
        )
        db.session.add(itinerary)
        trip.bookings.append(itinerary)
        db.session.commit()
        return {"trip":trip.to_dict()}
    else:
        return {"errors":form.errors},400
#expensing itinerary
@trip_routes.route('/<int:id>/itineraries/<int:itid>/expense/<int:exid>',methods=['PUT'])
@login_required
def expense_itinerary(id,itid,exid):
    trip = Trip.query.get(id)
    itinerary = Itinerary.query.get(itid)

    if trip is None:
        return {'errors': "Trip doesn't exist"}, 404
    if itinerary is None:
        return {'errors': "Itinerary doesn't exist"}, 404

    itinerary.expensed=True
    itinerary.expense_id = int(exid)


    db.session.commit()
    return {"trip":trip.to_dict()}
