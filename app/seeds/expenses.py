from app.models import db, Expense,ExpenseDetail, environment, SCHEMA
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
        user = choice(trip.users).user

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
        expense.payer=user

        users_involved = sample(trip.users,randint(3,len(trip.users)))
        expense_list_detail=[]
        for user in users_involved:
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
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM expense_details"))
        db.session.execute(text("DELETE FROM expenses"))

    db.session.commit()
