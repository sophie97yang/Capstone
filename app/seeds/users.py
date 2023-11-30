from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from faker import Faker
from random import randint

fake = Faker()
location_city = 'Denver,San Francisco,Austin,Phoenix,Los Angeles,Washington,Seattle,Portland'
location_state='CO,CA,TX,AZ,CA,DC,WA,OR'

# Adds a demo user, you can add other users here if you want
def seed_users():
    user_list=[]
    for i in range(13):
        first_name=fake.first_name()
        last_name=fake.last_name()
        email = fake.email(first_name,last_name)
        location=randint(0,7)
        city = location_city.split(',')[location]
        state=location_state.split(',')[location]
        user = User(first_name=first_name,last_name=last_name,email=email,password='password',city=city,state=state)
        db.session.add(user)
        user_list.append(user)
    db.session.commit()
    return user_list



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
