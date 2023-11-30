from app.models import db, Trip, environment, SCHEMA,TripDetail
from sqlalchemy.sql import text
from faker import Faker
from random import choice,sample,randint
from datetime import datetime

fake = Faker()

def seed_trips(users):
    locations = [['Aspen','CO'],
             ['Miami','FL'],
             ['Napa','CA'],
             ['Boston','MA'],
             ['Moab','UT'],
             ['Jackson','WY'],
             ['Nashville','TN'],
             ['Savannah','GA'],
             ['Charleston','SC'],
             ['Sedona','AZ'],
             ['Washington','DC'],
             ['New Orleans','LA'],
             ['Chicago','IL'],
             ['Orlando','FL'],
             ['Las Vegas','NV'],
             ['Oahu','HI'],
             ['Maui','HI'],
             ['New York City','NY']
             ]
    names = [f"{fake.first_name_female()}'s Bachelorette",f"{fake.first_name_male()}'s Bachelor Party",
      f"{fake.first_name_female()}'s 21st Birthday Bash",f"{fake.first_name_male()}'s 40th Birthday Party",
      f"Annual {fake.last_name()} Family Vacation", f"{fake.first_name_male()} and {fake.first_name_female()}'s Honeymoon",
      f"{fake.first_name_female()} and {fake.first_name_male()}'s Anniversary",f"{fake.last_name()} Family Reunion",
      f"{fake.last_name()}'s Vacation",f"{fake.first_name_female()}'s Bachelorette"]
    trip_list=[]
    for i in names:
        name = i
        location = choice(locations)
        city=location[0]
        state=location[1]
        startDate=fake.future_date()
        endDate=fake.date_between(start_date=startDate, end_date='+20d')
        image= fake.image_url()
        trip = Trip(
            name=name,city=city,state=state,start_date=startDate,end_date=endDate,image=image
        )
        users_involved = sample(users,randint(3,7))
        trip_list_detail=[]
        for user in users_involved:
            trip_detail = TripDetail(settled=False)
            trip_detail.user=user
            trip_list_detail.append(trip_detail)

        trip.users = trip_list_detail

        db.session.add(trip)
        trip_list.append(trip)

    db.session.commit()
    return trip_list


def undo_trips():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute (text("DELETE FROM trip_details"))
        db.session.execute(text("DELETE FROM trips"))

    db.session.commit()
