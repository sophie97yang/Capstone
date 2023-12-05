def seed_bookings():
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
    categories=['Hotel','Things To Do','Restaurants']

    # seed aspen
    aspen_hotel_one = Booking
