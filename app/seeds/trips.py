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
             ['Jackson','WY'],
             ['Nashville','TN'],
             ['Washington','DC'],
             ['Las Vegas','NV']
             ]
    unseeded_locations = [
            ['Savannah','GA'],
             ['Charleston','SC'],
             ['Sedona','AZ'],
             ['New Orleans','LA'],
             ['Chicago','IL'],
             ['Orlando','FL'],
             ['Oahu','HI'],
             ['Maui','HI'],
             ['New York City','NY'],
              ['Moab','UT'],
    ]
    names = [f"{fake.first_name_female()}'s Bachelorette",f"{fake.first_name_male()}'s Bachelor Party",
      f"{fake.first_name_female()}'s 21st Birthday Bash",f"{fake.first_name_male()}'s 40th Birthday Party",
      f"Annual {fake.last_name()} Family Vacation", f"{fake.first_name_male()} and {fake.first_name_female()}'s Honeymoon",
      f"{fake.first_name_female()} and {fake.first_name_male()}'s Anniversary",f"{fake.last_name()} Family Reunion",
      f"{fake.last_name()}'s Vacation",f"{fake.first_name_female()}'s Bachelorette"]

    images=['https://images.unsplash.com/photo-1522878129833-838a904a0e9e?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1433838552652-f9a46b332c40?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1475503572774-15a45e5d60b9?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTR8fHxlbnwwfHx8fHw%3D',
            'https://images.unsplash.com/photo-1515859005217-8a1f08870f59?q=80&w=2820&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1482192505345-5655af888cc4?q=80&w=2728&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1532274402911-5a369e4c4bb5?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2673&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NDV8fHxlbnwwfHx8fHw%3D',
            'https://images.unsplash.com/photo-1519451241324-20b4ea2c4220?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NDd8fHxlbnwwfHx8fHw%3D',
            'https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NTZ8fHxlbnwwfHx8fHw%3D',
            'https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NTV8fHxlbnwwfHx8fHw%3D',
            'https://images.unsplash.com/photo-1440778303588-435521a205bc?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Njd8fHxlbnwwfHx8fHw%3D',
            'https://images.unsplash.com/photo-1505778276668-26b3ff7af103?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8ODF8fHxlbnwwfHx8fHw%3D'
            ]
    trip_list=[]
    for i in names:
        name = i
        location = choice(locations)
        city=location[0]
        state=location[1]
        startDate=fake.date_between(start_date='-4d',end_date='today')
        endDate=fake.date_between(start_date='today', end_date='+5d')
        image= choice(images)
        trip = Trip(
            name=name,city=city,state=state,start_date=startDate,end_date=endDate,image=image
        )
        users_involved = sample(users,randint(3,4))
        trip_list_detail=[]
        count=1
        for user in users_involved:
            if count==1:
                trip_detail = TripDetail(settled=False,creator=True)
                trip_detail.user=user
            else:
                trip_detail = TripDetail(settled=False)
                trip_detail.user=user
            trip_list_detail.append(trip_detail)
            count+=1

        trip.users = trip_list_detail

        db.session.add(trip)
        trip_list.append(trip)

    db.session.commit()
    return trip_list


def undo_trips():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.trips RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM between_user_expenses"))
        db.session.execute (text("DELETE FROM trip_details"))
        db.session.execute(text("DELETE FROM trips"))

    db.session.commit()
