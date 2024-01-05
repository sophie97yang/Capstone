from app.models import db, Booking,Itinerary, User,environment, SCHEMA
import datetime

def seed_itineraries (trips):
    demo_user = User.query.filter(User.first_name=='Demo').first()
    #seed past trip's itineraries
    past_trip = trips[0]
    #book hotel
    hotel = Booking.query.filter(Booking.name=='The Gant' and Booking.city=='Aspen').first()
    booked_hotel_1 = Itinerary(
        booking_date=datetime.date(2023,11,20),
        booking_startdate = past_trip.start_date,
        booking_enddate=past_trip.end_date,
        booking_time="00:00",
        expensed=False,
        total=3296.24,
        people=3
    )
    booked_hotel_1.booking=hotel
    booked_hotel_1.trip = past_trip
    booked_hotel_1.user=demo_user

    db.session.add(booked_hotel_1)
    #reservation
    thing = Booking.query.filter(Booking.name=='Raft the Colorado River through Glenwood Springs - Half Day Adventure' and Booking.city=='Aspen').first()
    booked_thing_1 = Itinerary(
        booking_date=datetime.date(2023,12,2),
        booking_startdate = datetime.date(2023,12,9),
        booking_enddate=datetime.date(2023,12,9),
        booking_time="11:00 AM",
        expensed=False,
        total=387.54,
        people=5
    )
    booked_thing_1.booking=thing
    booked_thing_1.trip = past_trip
    booked_thing_1.user=demo_user

    db.session.add(booked_thing_1)


    #seed restaurant
    rest = Booking.query.filter(Booking.name=='The White House Tavern' and Booking.city=='Aspen').first()
    booked_thing_2 = Itinerary(
        booking_date=datetime.date(2023,12,6),
        booking_startdate = datetime.date(2023,12,7),
        booking_enddate=datetime.date(2023,12,7),
        booking_time="07:30 PM",
        expensed=False,
        people=5
    )
    booked_thing_2.booking=rest
    booked_thing_2.trip = past_trip
    booked_thing_2.user=demo_user

    db.session.add(booked_thing_2)


    #seed current trip's itineraries
    current_trip = trips[1]

    #book_hotel_2
    hotel_2 = Booking.query.filter(Booking.name=='Wynn Las Vegas' and Booking.city=='Las Vegas').first()
    booked_hotel_2 = Itinerary(
        booking_date=datetime.date(2023,11,30),
        booking_startdate = current_trip.start_date,
        booking_enddate=current_trip.end_date,
        booking_time="00:00",
        expensed=False,
        total=7089.64,
        people=4
    )
    booked_hotel_2.booking=hotel_2
    booked_hotel_2.trip = current_trip
    booked_hotel_2.user=demo_user

    db.session.add(booked_hotel_2)

    db.session.commit()
