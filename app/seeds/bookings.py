from app.models import db, Booking, environment, SCHEMA
from sqlalchemy.sql import text
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
    # hotels - per night
    aspen_hotel_one = Booking(name='Limelight Hotel',category='Hotel',city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/photo-i/1f/53/dc/38/limelight-hotel-aspen.jpg",image2="https://media-cdn.tripadvisor.com/media/oyster/500/05/8b/ee/cb/the-hotel--v1923659-60.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/03/b0/88/23/the-limelight-hotel.jpg",price=759)
    aspen_hotel_two = Booking(name='The Gant',category='Hotel',city="Aspen",state="CO",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/7e/d4/42/the-gant-lower-pool.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/31/b8/a0/the-gant.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/4b/c3/37/three-bedroom-three-bath-deluxe--.jpg",price=716)
    aspen_hotel_three = Booking(name='Mountain Chalet Aspen',category='Hotel',city="Aspen",state="CO",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/cb/11/e2/standard-queen-room--v6083403.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/cb/12/47/standard-queen-room--v6083558.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/cb/11/aa/dining-room--v6083348.jpg",price=461)
    aspen_hotel_four = Booking(name='The St. Regis Aspen Resort',category='Hotel',city="Aspen",state="CO",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/14/76/85/the-beautiful-st-regis.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/b4/72/ce/grand-deluxe-double.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/14/76/f2/fountain-courtyard-wedding.jpg",price=716)
    aspen_hotel_five = Booking(name='Residences at The Little Nell',category='Hotel',city="Aspen",state="CO",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/0c/9a/c1/residences-exterior.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/8b/a1/55/residences-at-the-little.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0b/b9/c2/44/residences-bedroom.jpg",price=2139)
    db.session.add(aspen_hotel_one)
    db.session.add(aspen_hotel_two)
    db.session.add(aspen_hotel_three)
    db.session.add(aspen_hotel_four)
    db.session.add(aspen_hotel_five)
    #things to do - per person
    aspen_thing_one = Booking(name="Aspen's DarkSide Ghost Tour",category="Things To Do",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/74/7c/8b.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/8a/9f/5a.jpg",image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/8a/a0/b2.jpg",price=40)
    aspen_thing_two = Booking(name="Raft the Colorado River through Glenwood Springs - Half Day Adventure",category="Things To Do",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/39/ee/9c.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/39/ee/7b.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/6a/17/b2/caption.jpg",price=67.99)
    aspen_thing_three = Booking(name="Aspen hotel or address to Denver Airport (DEN) - Departure Private Transfer",category="Things To Do",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/50/10/78.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/50/10/d8.jpg",image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/50/10/d0.jpg",price=220.37)
    db.session.add(aspen_thing_one)
    db.session.add(aspen_thing_two)
    db.session.add(aspen_thing_three)
    #restaurants
    aspen_restaurant_1= Booking(name="PARC Aspen",category="Restaurants",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/photo-f/29/87/01/0b/parc-aspen-sign.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/28/ba/52/d9/organic-salmon.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/1d/8f/42/b0/fondue.jpg")
    aspen_restaurant_2= Booking(name="Matsuhisa-Aspen",category="Restaurants",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/photo-f/1c/64/35/6b/custom-dishes.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-f/1c/64/35/5e/downstairs-bar.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/1c/64/35/5d/downstairs-dining-room.jpg")
    aspen_restaurant_3= Booking(name="The White House Tavern",category="Restaurants",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/photo-s/04/0c/4d/e9/hand-cut-french-fries.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/06/68/28/8e/the-white-house-tavern.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-f/0f/72/f2/cc/the-white-house-tavern.jpg")
    aspen_restaurant_4= Booking(name="Plato's Restaurant",category="Restaurants",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/photo-s/18/55/43/6a/plato-s-restaurant.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-f/18/54/a7/6f/plato-s-restaurant.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-f/18/55/3f/87/plato-s-restaurant.jpg")
    aspen_restaurant_5= Booking(name="Clark's Oyster Bar - Aspen",category="Restaurants",city="Aspen",state="CO",image1="https://media-cdn.tripadvisor.com/media/photo-p/28/69/bd/ba/clarks-aspen.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/28/69/d5/43/clarks-aspen.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/28/69/d4/93/clarks-aspen.jpg")

    db.session.add(aspen_restaurant_1)
    db.session.add(aspen_restaurant_2)
    db.session.add(aspen_restaurant_3)
    db.session.add(aspen_restaurant_4)
    db.session.add(aspen_restaurant_5)

     # seed miami
    miami_hotels = [
        Booking(name='The Elser Hotel & Residences',category='Hotel',city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/f7/16/5c/the-elser-hotel-miami.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/f7/25/07/the-elser-hotel-miami.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/f7/24/b3/the-elser-hotel-miami.jpg",price=659),
        Booking(name='JW Marriott Marquis Miami',category='Hotel',city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/34/60/54/king-concierge-bay-view.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/ec/83/e0/gallery-1-2.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/ec/83/db/concierge-lounge.jpg?w=500&h=500&s=1",price=778),
        Booking(name='Novotel Miami Brickell',category='Hotel',city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c8/06/86/rooftop-pool-views.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c8/06/71/hotel-lobby.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c6/57/d4/novotel-miami-brickell.jpg",price=419),
        Booking(name='YOTEL Miami',category='Hotel',city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/9c/7f/74/pool-deck.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/9c/7f/91/food-drink.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/9c/7f/90/restaurant.jpg",price=250),
        Booking(name='Hyatt Regency Miami',category='Hotel',city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/24/ff/63/2c/exterior.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/6e/96/1b/hyatt-regency-miami.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/6e/96/03/hyatt-regency-miami.jpg",price=446)
     ]
    miami_things = [
        Booking(name="Miami Skyline 90 min Cruise of South Beach Millionaire Homes & Venetian Islands",category="Things To Do",city="Miami",state="FL",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/9c/56/ce.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/9c/57/0b.jpg",image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/9c/56/d2.jpg",price=29.99),
        Booking(name="Superblue Miami Immersive Art Experience Ticket in Miami",category="Things To Do",city="Miami",state="FL",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/0d/d8/f0.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/0d/d7/50.jpg",image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0e/99/13/07.jpg",price=39),
        Booking(name="Taste of Miami Private Helicopter Tour",category="Things To Do",city="Miami",state="FL",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0d/07/c6/54.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0f/9a/05/98.jpg",image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0c/0b/08/c3.jpg",price=189)
    ]

    miami_restaurants = [
        Booking(name="Mayu",category="Restaurants",city="Miami",state="FL",image1="https://media-cdn.tripadvisor.com/media/photo-p/2a/34/27/57/12.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-f/2a/34/27/5d/7.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-l/2a/34/27/59/5.jpg"),
        Booking(name="Sala'o Cuban Restaurant & Bar",category="Restaurants",city="Miami",state="FL",image1="https://media-cdn.tripadvisor.com/media/photo-s/2a/cf/4a/7b/delicious-cuban-food.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-f/2a/c8/77/e0/chuleta-de-cerdo.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/99/10/64/pesca-malecon-la-mulata.jpg"),
        Booking(name="CRAFT South Beach - Espanola Way",category="Restaurants",city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/8b/e2/62/a-bit-of-out-best-sellers.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/0d/09/83/some-of-our-pizzas.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/0d/02/4d/potatoe-rosti.jpg"),
        Booking(name="Osteria Positano",category="Restaurants",city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/fc/d9/b5/italian-restaurant-in.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/89/a0/84/italian-restaurant-in.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/89/a0/81/italian-restaurant-in.jpg?w=1200&h=800&s=1"),
        Booking(name="On Ocean 7 Cafe",category="Restaurants",city="Miami",state="FL",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/f9/b9/10/on-ocean-7-cafe.jpg",image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/f9/ba/5b/on-ocean-7-cafe.jpg",image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/f9/b8/bf/on-ocean-7-cafe.jpg?w=1200&h=800&s=1")
    ]

    for hotel in miami_hotels:
        db.session.add(hotel)

    for thing in miami_things:
        db.session.add(thing)

    for restaurant in miami_restaurants:
        db.session.add(restaurant)

     #seed napa

    napa_hotels = [
        Booking(name='The Meritage Resort and Spa',category='Hotel',city="Napa",state="CA",image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/ca/23/70/meritage-resort-and-spa.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/21/f8/e5/cd/vineyards.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/21/f8/e5/c6/lawn-yoga.jpg",price=329),
        Booking(name='TGrand Reserve',category='Hotel',city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-w/14/04/b5/6c/vista-collina-resort.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/14/04/bd/06/double-guestroom.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/14/94/d2/8c/vista-collina-resort.jpg",price=450),
        Booking(name='Carneros Resort and Spa',category='Hotel',city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-w/2a/a7/d6/6f/caption.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/16/c1/66/a3/carneros-resort-and-spa.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/16/c1/64/9b/carneros-resort-and-spa.jpg",price=749),
        Booking(name='Candlelight Inn Napa Valley',category='Hotel',city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-w/0e/78/fb/49/side-view-of-the-house.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/07/d8/31/aa/candlelight-inn-napa.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/0e/78/fb/3c/view-of-the-house-through.jpg",price=199),
        Booking(name='Archer Hotel Napa',category='Hotel',city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-w/2a/a7/80/dd/archer-hotel-napa-lobby.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/2a/a7/80/e7/archer-hotel-napa-lobby.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/29/60/b8/df/archer-hotel-napa-deluxe.jpg",price=229),
     ]
    napa_things = [
        Booking(name="Napa and Sonoma Wine Country Full-Day Tour from San Francisco",category="Things To Do",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/09/4c/21/3c.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/75/6c/48.jpg",image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/75/6c/4a.jpg",price=160),
        Booking(name="Self Guided Full Day E-bike Rental With Picnic Lunch",category="Things To Do",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0f/1c/84/7c.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0f/1c/85/8e.jpg",image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0f/2c/cc/26.jpg",price=179),
        Booking(name="The Original Napa Valley Wine Trolley Classic Tour",category="Things To Do",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/07/9a/92/20.jpg",image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0e/7f/a3/ba.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-s/2a/98/47/ba/caption.jpg",price=125),
    ]

    napa_restaurants = [
        Booking(name="Bistro Don Giovanni",category="Restaurants",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-s/04/65/56/b6/bistro-don-giovanni.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-s/12/a6/b9/fb/bistro-don-giovanni.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-l/1d/9a/7e/c0/caption.jpg"),
        Booking(name="Wit & Wisdom",category="Restaurants",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-s/1b/fa/45/c1/grab-a-seat-at-the-bar.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-f/1b/fa/45/90/crispy-berkshire-porchetta.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-f/1b/fa/48/fb/fresh-local-fruits-and.jpg"),
        Booking(name="LaSalette Restaurant",category="Restaurants",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-s/09/c2/e5/fd/lasalette-restaurant.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-l/1b/f5/d0/4c/img-20200906-200010-largejpg.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-f/1c/da/16/f0/20210412-125746-largejpg.jpg"),
        Booking(name="the girl & the fig",category="Restaurants",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-s/1d/29/e0/c5/roasted-half-chicken.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-l/1d/b4/b5/e8/local-king-salmon-pepperonata.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-l/1d/86/b5/10/gulf-shrimp-corn-sweet.jpg"),
        Booking(name="Ciccio",category="Restaurants",city="Napa",state="CA",image1="https://media-cdn.tripadvisor.com/media/photo-s/05/71/16/b4/ciccio.jpg",image2="https://media-cdn.tripadvisor.com/media/photo-o/03/42/08/4a/all-decked-out-for-the.jpg",image3="https://media-cdn.tripadvisor.com/media/photo-l/16/e6/38/10/photo0jpg.jpg")
    ]

    for hotel in napa_hotels:
        db.session.add(hotel)

    for thing in napa_things:
        db.session.add(thing)

    for restaurant in napa_restaurants:
        db.session.add(restaurant)

    db.session.commit()
     #seed boston

     #seed jackson

     #seed nashville

     #seed savannah

     # seed charleston

     #seed sedona

def undo_bookings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bookings"))
    db.session.commit()
