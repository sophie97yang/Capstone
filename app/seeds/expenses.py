from app.models import db, Expense,ExpenseDetail,BetweenUserExpense, environment, SCHEMA
from sqlalchemy.sql import text
from faker import Faker
from random import choice,sample,randint

fake = Faker()

def seed_expenses(users,trips):
    name_category= [
        ['Gas','Transportation'],
        ['Grocery trip','Food and Drink'],
        ['Hot dogs','Food and Drink'],
        ['Groceries walmart','Food and Drink'],
        ['Mac and Cheese and Hot Dog Night','Food and Drink'],
        ['Charcuterie night','Food and Drink'],
        ['Rental car gas','Transportation'],
        ['Rental car','Transportation'],
        ['Goodie bag stuff','Entertainment'],
        ['Uber','Transportation'],
        ['Lyft','Transportation'],
        ['Target','Entertainment'],
        ['Taco Night','Food and Drink'],
        ['Cookies','Food and Drink'],
        ['Breakfast','Food and Drink'],
        ['Uber from airport','Transportation'],
        ['Starbucks','Food and Drink'],
        ['Dinner Night 1','Food and Drink'],
        ['CVS Cups and Balls','Entertainment'],
        ['Dunkin','Food and Drink'],
        ['Skydiving','Entertainment'],
        ['Ski Rentals','Entertainment'],
        ['Airbnb','Transportation'],
        ['Hotel','Transportation'],
        ['Lyft to airport','Transportation'],
        ['Taco Bell','Food and Drink'],
        ['Camping supplies','Entertainment'],
        ['Extra Fee from Bank','General']
    ]

    split_types=['Equal','Percentages','Exact']

    prices=[45.00,54.95,24.00,67.75,15.34,68.32,74.59,43.23,98.78]
    expense_list=[]
    for i in name_category:
        trip = choice(trips)
        payer = choice(trip.users).user

        name = i[0]
        expense_date=fake.date_between_dates(date_start=trip.start_date, date_end=trip.end_date)
        split_type='Equal'
        image= fake.image_url()
        category=i[1]
        if name == 'Airbnb':
            total=1456.67
        else:
            total=choice(prices)
        expense = Expense(name=name,expense_date=expense_date,split_type=split_type,image=image,category=category,total=total)
        expense.trip=trip
        expense.payer=payer

        users_involved = sample(trip.users,randint(1,len(trip.users)))
        expense_list_detail=[]
        for user in users_involved:
            #check if there is already an existing expense relationship between two users in trip
            relationship_one = BetweenUserExpense.query.filter_by(user_one_id=payer.id,user_two_id=user.user.id,trip_id=trip.id).first()
            relationship_two= BetweenUserExpense.query.filter_by(user_one_id=user.user.id,user_two_id=payer.id,trip_id=trip.id).first()
            # if a relationship is found
            if relationship_one or relationship_two:
                if relationship_one:
                    #user_one=payer,user_two=user involved in expense
                    #user_one now is owed $
                    relationship_one.owed+=total/len(users_involved)
                elif relationship_two:
                    #user_one=user involved in expense, user_two=payer
                    #user_one now owes money $
                    relationship_two.owes+=total/len(users_involved)
            #if there is no existing relationship,create one
            else:
                #user_one=payer,user_two=user involved in expense
                #user one now is owed $
                relationship=BetweenUserExpense(user_one_id=payer.id,
                                                user_two_id=user.user.id,
                                                trip_id=trip.id,
                                                owed= total/len(users_involved)
                                                )
                db.session.add(relationship)

            expense_detail = ExpenseDetail(price=(total/len(users_involved)))
            expense_detail.user=user.user
            expense_list_detail.append(expense_detail)

        expense.users = expense_list_detail
        db.session.add(expense)
        expense_list.append(expense)

    db.session.commit()
    return expense_list


def undo_expenses():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.expenses RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM expense_update_details"))
        db.session.execute(text("DELETE FROM expense_details"))
        db.session.execute(text("DELETE FROM expenses"))

    db.session.commit()
