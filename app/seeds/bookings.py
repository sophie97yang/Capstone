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
    category = 'Hotel'
    aspen_hotel_one = Booking(
    name='Limelight Hotel',
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1889,  # Add the actual latitude
    lng=-106.8214,  # Add the actual longitude
    description="Discover modern luxury at the Limelight Hotel in Aspen. Enjoy stylish accommodations, top-notch amenities, and proximity to Aspen Mountain.",
    rating=4.5,
    contact_info="(555) 123-4567",
    website="limelighthotels.com/aspen",
    features="Ski-in/Ski-out, Outdoor Pool, Lounge",
    price=759,
    image1="https://media-cdn.tripadvisor.com/media/photo-i/1f/53/dc/38/limelight-hotel-aspen.jpg",
    image2="https://media-cdn.tripadvisor.com/media/oyster/500/05/8b/ee/cb/the-hotel--v1923659-60.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/03/b0/88/23/the-limelight-hotel.jpg"
)
    aspen_hotel_two = Booking(
    name='The Gant',
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1846,  # Add the actual latitude
    lng=-106.8146,  # Add the actual longitude
    description="Experience luxury and comfort at The Gant in Aspen. With spacious condos, breathtaking views, and exceptional amenities, it's the perfect retreat.",
    rating=4.7,
    contact_info="(555) 234-5678",
    website="gantaspen.com",
    features="Heated Pools, Tennis Courts, Fitness Center",
    price=716,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/7e/d4/42/the-gant-lower-pool.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/31/b8/a0/the-gant.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/4b/c3/37/three-bedroom-three-bath-deluxe--.jpg"
)
    aspen_hotel_three = Booking(
    name='Mountain Chalet Aspen',
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1846,  # Add the actual latitude
    lng=-106.8146,
    description="Experience cozy charm at Mountain Chalet Aspen. Relax in comfortable rooms, enjoy mountain views, and take advantage of the hotel's warm hospitality.",
    rating=4.2,
    contact_info="(555) 345-6789",
    website="mountainchaletaspen.com",
    features="Hot Tub, Fireplace, Complimentary Breakfast",
    price=461,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/cb/11/e2/standard-queen-room--v6083403.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/cb/12/47/standard-queen-room--v6083558.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/cb/11/aa/dining-room--v6083348.jpg"
)
    aspen_hotel_four = Booking(
    name='The St. Regis Aspen Resort',
    category=category,
    city="Aspen",
    state="CO",
    lat=39.190747,  # Add the actual latitude
    lng=-106.8207732,  # Add the actual longitude
    description="Indulge in luxury at The St. Regis Aspen Resort. Impeccable service, elegant accommodations, and world-class amenities await you in the heart of Aspen.",
    rating=4.8,
    contact_info="(555) 456-7890",
    website="stregisaspen.com",
    features="Remède Spa, Outdoor Pool, Fine Dining",
    price=716,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/14/76/85/the-beautiful-st-regis.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/b4/72/ce/grand-deluxe-double.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/14/76/f2/fountain-courtyard-wedding.jpg"
)
    aspen_hotel_five = Booking(
    name='Residences at The Little Nell',
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1865231,  # Add the actual latitude
    lng=-106.8189969,  # Add the actual longitude
    description="Experience ultimate luxury at Residences at The Little Nell. These exquisite residences offer unparalleled views, personalized services, and access to world-class amenities.",
    rating=4.9,
    contact_info="(555) 987-6543",
    website="thelittlenell.com/residences",
    features="Ski Concierge, Private Chef, Rooftop Pool",
    price=2139,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/0c/9a/c1/residences-exterior.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/8b/a1/55/residences-at-the-little.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0b/b9/c2/44/residences-bedroom.jpg"
)
    db.session.add(aspen_hotel_one)
    db.session.add(aspen_hotel_two)
    db.session.add(aspen_hotel_three)
    db.session.add(aspen_hotel_four)
    db.session.add(aspen_hotel_five)


    #things to do - per person
    category = 'Things To Do'
    aspen_thing_one = Booking(
    name="Aspen's DarkSide Ghost Tour",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1893609,  # Add the actual latitude
    lng=-106.8225437,  # Add the actual longitude
    description="Embark on Aspen's DarkSide Ghost Tour for a spine-chilling journey through the haunted history of this picturesque town. Explore eerie locations and hear tales of supernatural encounters.",
    rating=4.6,
    contact_info="(555) 123-4567",
    website="darksideghosttour.com",
    features="Guided Tour, Paranormal Stories, Nighttime Excursion",
    price=40,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/74/7c/8b.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/8a/9f/5a.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/8a/a0/b2.jpg"
)

    aspen_thing_two = Booking(
    name="Raft the Colorado River through Glenwood Springs - Half Day Adventure",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.5517872,  # Add the actual latitude
    lng=-107.3291725,  # Add the actual longitude
    description="Embark on an adrenaline-pumping adventure with a half-day rafting tour on the Colorado River through the stunning landscapes of Glenwood Springs. Experience the thrill of white-water rafting.",
    rating=4.8,
    contact_info="(555) 234-5678",
    website="glenwoodrafting.com",
    features="White-water Rafting, Scenic Views, Professional Guides",
    price=67.99,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/39/ee/9c.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/39/ee/7b.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/6a/17/b2/caption.jpg"
)

    aspen_thing_three = Booking(
    name="Aspen to Denver Airport - Departure Private Transfer",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.8563486,  # Add the actual latitude
    lng=-104.6764061,  # Add the actual longitude
    description="Enjoy a hassle-free departure with a private transfer from your Aspen hotel or address to Denver Airport (DEN). Travel in comfort and style with a professional driver.",
    rating=4.5,
    contact_info="(555) 345-6789",
    website="privatetransfersaspen.com",
    features="Private Transfer, Door-to-Door Service, Comfortable Vehicles",
    price=220.37,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/50/10/78.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/50/10/d8.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/50/10/d0.jpg"
)
    db.session.add(aspen_thing_one)
    db.session.add(aspen_thing_two)
    db.session.add(aspen_thing_three)



    #restaurants
    category = 'Restaurants'
    aspen_restaurant_1= Booking(
    name="PARC Aspen",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1886374,  # Add the actual latitude
    lng=-106.8165933,  # Add the actual longitude
    description="Indulge in culinary excellence at PARC Aspen. This upscale restaurant offers a sophisticated atmosphere and a menu featuring exquisite dishes, including organic salmon and fondue.",
    rating=4.5,
    contact_info="(555) 123-4567",
    website="parcaspen.com",
    features="Fine Dining, Contemporary Cuisine",
    opening_hour="6:00 PM",
    closing_hour="10:00 PM",
    price=1000,
    image1="https://media-cdn.tripadvisor.com/media/photo-f/29/87/01/0b/parc-aspen-sign.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/28/ba/52/d9/organic-salmon.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/1d/8f/42/b0/fondue.jpg"
)
    aspen_restaurant_2= Booking(
    name="Matsuhisa-Aspen",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1906522,  # Add the actual latitude
    lng=-106.8202674,  # Add the actual longitude
    description="Experience culinary artistry at Matsuhisa-Aspen. This renowned restaurant, founded by Chef Nobu Matsuhisa, offers a unique blend of Japanese-Peruvian flavors and a stylish ambiance.",
    rating=4.7,
    contact_info="(555) 234-5678",
    website="matsuhisaaspen.com",
    features="Sushi, Japanese-Peruvian Fusion",
    opening_hour="5:30 PM",
    closing_hour="11:00 PM",
    price=100,
    image1="https://media-cdn.tripadvisor.com/media/photo-f/1c/64/35/6b/custom-dishes.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/1c/64/35/5e/downstairs-bar.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/1c/64/35/5d/downstairs-dining-room.jpg"
)
    aspen_restaurant_3= Booking(
    name="The White House Tavern",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.1903053,  # Add the actual latitude
    lng=-106.8204276,  # Add the actual longitude
    description="Enjoy casual elegance at The White House Tavern. Known for its hand-cut French fries and cozy atmosphere, this tavern offers a diverse menu for lunch and dinner.",
    rating=4.3,
    contact_info="(555) 345-6789",
    website="whitehousetavern.com",
    features="American, Pub Fare",
    opening_hour="11:00 AM",
    closing_hour="9:00 PM",
    price=100,
    image1="https://media-cdn.tripadvisor.com/media/photo-s/04/0c/4d/e9/hand-cut-french-fries.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/06/68/28/8e/the-white-house-tavern.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/0f/72/f2/cc/the-white-house-tavern.jpg"
)

    aspen_restaurant_4= Booking(
    name="Plato's Restaurant",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.2011675,  # Add the actual latitude
    lng=-106.8317808,  # Add the actual longitude
    description="Discover a culinary haven at Plato's Restaurant. With a diverse menu and a cozy ambiance, this restaurant is perfect for a casual dining experience in the heart of Aspen.",
    rating=4.0,
    contact_info="(555) 456-7890",
    website="platosaspen.com",
    features="Mediterranean, Casual Dining",
    opening_hour="7:00 AM",
    closing_hour="10:00 PM",
    price=10,
    image1="https://media-cdn.tripadvisor.com/media/photo-s/18/55/43/6a/plato-s-restaurant.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/18/54/a7/6f/plato-s-restaurant.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/18/55/3f/87/plato-s-restaurant.jpg"
)
    aspen_restaurant_5= Booking(
    name="Clark's Oyster Bar - Aspen",
    category=category,
    city="Aspen",
    state="CO",
    lat=39.18851, # Add the actual latitude
    lng=-106.8180609,  # Add the actual longitude
    description="Savor the flavors of the sea at Clark's Oyster Bar in Aspen. Known for its fresh oysters and seafood dishes, this restaurant offers a relaxed atmosphere and a raw bar.",
    rating=4.4,
    contact_info="(555) 987-6543",
    website="clarksoysterbar.com",
    features="Seafood, Oyster Bar",
    opening_hour="4:00 PM",
    closing_hour="11:00 PM",
    price=100,
    image1="https://media-cdn.tripadvisor.com/media/photo-p/28/69/bd/ba/clarks-aspen.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/28/69/d5/43/clarks-aspen.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/28/69/d4/93/clarks-aspen.jpg"
)

    db.session.add(aspen_restaurant_1)
    db.session.add(aspen_restaurant_2)
    db.session.add(aspen_restaurant_3)
    db.session.add(aspen_restaurant_4)
    db.session.add(aspen_restaurant_5)

     # seed miami
    category = 'Hotel'
    miami_hotels = [
    Booking(
    name='The Elser Hotel & Residences',
    category=category,
    city="Miami",
    state="FL",
    lat=25.7788802,  # Add the actual latitude
    lng=-80.1890556,  # Add the actual longitude
    description="Experience luxury at The Elser Hotel & Residences. This Miami gem offers sophisticated accommodations, stunning views, and impeccable service for an unforgettable stay.",
    rating=4.5,
    contact_info="(555) 123-4567",
    website="elserhotelmiami.com",
    features="Swimming Pool, Fitness Center, Rooftop Lounge",
    price=659,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/f7/16/5c/the-elser-hotel-miami.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/f7/25/07/the-elser-hotel-miami.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/f7/24/b3/the-elser-hotel-miami.jpg"
    ),
    Booking(
    name='JW Marriott Marquis Miami',
    category=category,
    city="Miami",
    state="FL",
    lat=25.771089,  # Add the actual latitude
    lng=-80.1894477,  # Add the actual longitude
    description="Indulge in luxury at the JW Marriott Marquis Miami. Enjoy breathtaking views, upscale amenities, and exceptional service at this iconic downtown hotel.",
    rating=4.7,
    contact_info="(555) 234-5678",
    website="jwmarriottmarquismiami.com",
    features="Concierge Service, Bay View Rooms, Rooftop Pool",
    price=778,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/34/60/54/king-concierge-bay-view.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/ec/83/e0/gallery-1-2.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/ec/83/db/concierge-lounge.jpg?w=500&h=500&s=1"
),
    Booking(
    name='Novotel Miami Brickell',
    category=category,
    city="Miami",
    state="FL",
    lat=25.7597839,  # Add the actual latitude
    lng=-80.1969231,  # Add the actual longitude
    description="Discover modern comfort at Novotel Miami Brickell. With a rooftop pool, stylish lobby, and convenient location, this hotel provides a perfect blend of luxury and convenience.",
    rating=4.3,
    contact_info="(555) 345-6789",
    website="novotelmiamibrickell.com",
    features="Rooftop Pool, Stylish Lobby, Contemporary Design",
    price=419,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c8/06/86/rooftop-pool-views.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c8/06/71/hotel-lobby.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c6/57/d4/novotel-miami-brickell.jpg"
),
    Booking(
    name='YOTEL Miami',
    category=category,
    city="Miami",
    state="FL",
    lat=25.7762606,  # Add the actual latitude
    lng=-80.1897584,  # Add the actual longitude
    description="Experience innovation at YOTEL Miami. This tech-forward hotel offers a sleek and efficient design, a rooftop pool deck, and a vibrant atmosphere in the heart of Miami.",
    rating=4.1,
    contact_info="(555) 456-7890",
    website="yotelmiami.com",
    features="Rooftop Pool, Tech-Forward Design, Trendy Atmosphere",
    price=250,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/9c/7f/74/pool-deck.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/9c/7f/91/food-drink.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/9c/7f/90/restaurant.jpg"
),
    Booking(
    name='Hyatt Regency Miami',
    category=category,
    city="Miami",
    state="FL",
    lat=25.77092631,  # Add the actual latitude
    lng=-80.1910809,  # Add the actual longitude
    description="Experience upscale hospitality at Hyatt Regency Miami. With modern amenities, a prime downtown location, and stunning views, this hotel offers a memorable stay in the Magic City.",
    rating=4.4,
    contact_info="(555) 987-6543",
    website="hyattregencymiami.com",
    features="Business Center, Fitness Facility, Skyline Views",
    price=446,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/24/ff/63/2c/exterior.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/6e/96/1b/hyatt-regency-miami.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/6e/96/03/hyatt-regency-miami.jpg"
)
]

    for hotel in miami_hotels:
        db.session.add(hotel)


    category = "Things To Do"
    miami_things = [
        Booking(
    name="Miami Skyline 90 min Cruise of South Beach Millionaire Homes & Venetian Islands",
    category=category,
    city="Miami",
    state="FL",
    lat=25.7771412,  # Add the actual latitude
    lng=-80.1855735,  # Add the actual longitude
    description="Embark on a 90-minute cruise showcasing the stunning Miami skyline, South Beach Millionaire Homes, and the picturesque Venetian Islands. Relax and enjoy the breathtaking views of Miami's iconic landmarks.",
    rating=4.8,
    contact_info="(555) 123-4567",
    website="miami-cruise.com",
    features="Scenic Views, Millionaire Homes, Venetian Islands",
    price=29.99,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/9c/56/ce.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/9c/57/0b.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/9c/56/d2.jpg"
),
Booking(
    name="Superblue Miami Immersive Art Experience Ticket in Miami",
    category=category,
    city="Miami",
    state="FL",
    lat=25.7994058,  # Add the actual latitude
    lng=-80.2144411,  # Add the actual longitude
    description="Immerse yourself in the world of contemporary art at Superblue Miami. This unique experience features immersive and interactive art installations that will captivate your senses and ignite your creativity.",
    rating=4.7,
    contact_info="(555) 234-5678",
    website="superblue.com/miami",
    features="Immersive Art, Interactive Installations, Contemporary Exhibits",
    price=39,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/0d/d8/f0.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/11/0d/d7/50.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0e/99/13/07.jpg"
),
Booking(
    name="Taste of Miami Private Helicopter Tour",
    category=category,
    city="Miami",
    state="FL",
    lat=25.6506251,  # Add the actual latitude
    lng=-80.4270233,  # Add the actual longitude
    description="Soar above Miami's iconic landmarks on a private helicopter tour. Experience a Taste of Miami as you take in panoramic views of the city, beaches, and attractions from the comfort of a helicopter.",
    rating=4.9,
    contact_info="(555) 345-6789",
    website="miami-helitours.com",
    features="Private Helicopter Tour, Panoramic Views, Landmarks",
    price=189,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0d/07/c6/54.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0f/9a/05/98.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0c/0b/08/c3.jpg"
)

    ]


    for thing in miami_things:
        db.session.add(thing)

    category = "Restaurants"
    miami_restaurants = [
    Booking(
    name="Mayu",
    category=category,
    city="Miami",
    state="FL",
    lat=25.7674916,  # Add the actual latitude
    lng=-80.1969625,  # Add the actual longitude
    description="Savor exquisite culinary delights at Mayu, a top-rated restaurant in Miami. Our menu features a fusion of flavors, ensuring a delightful dining experience in a sophisticated atmosphere.",
    rating=4.9,
    contact_info="(555) 123-4567",
    website="mayu-miami.com",
    features="Fine Dining, Fusion Cuisine",
    price=1000,
    opening_hour="5:30 PM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-p/2a/34/27/57/12.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/2a/34/27/5d/7.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-l/2a/34/27/59/5.jpg"
),
Booking(
    name="Sala'o Cuban Restaurant & Bar",
    category=category,
    city="Miami",
    state="FL",
    lat=25.76551,  # Add the actual latitude
    lng=-80.22145,  # Add the actual longitude
    description="Experience the vibrant flavors of Cuba at Sala'o Cuban Restaurant & Bar. Our menu features authentic Cuban dishes, ensuring a taste of the Caribbean in the heart of Miami.",
    rating=4.5,
    contact_info="(555) 234-5678",
    website="salaocubanmiami.com",
    features="Cuban Cuisine, Live Music, Mojito Bar",
    price=10,
    opening_hour="11:00 AM",
    closing_hour="9:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/2a/cf/4a/7b/delicious-cuban-food.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/2a/c8/77/e0/chuleta-de-cerdo.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/99/10/64/pesca-malecon-la-mulata.jpg"
),
Booking(
    name="CRAFT South Beach - Espanola Way",
    category=category,
    city="Miami",
    state="FL",
    lat=25.7869657,  # Add the actual latitude
    lng=-80.132806,  # Add the actual longitude
    description="Indulge in a culinary adventure at CRAFT South Beach - Espanola Way. Our diverse menu showcases innovative dishes and craft cocktails, creating a unique dining experience on Miami's iconic Espanola Way.",
    rating=4.7,
    contact_info="(555) 345-6789",
    website="craftsouthbeach.com",
    features="Craft Cocktails, Artisanal Cuisine, Vibrant Atmosphere",
    price=100,
    opening_hour="6:00 PM",
    closing_hour="11:00 PM",
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/8b/e2/62/a-bit-of-out-best-sellers.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/0d/09/83/some-of-our-pizzas.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/0d/02/4d/potatoe-rosti.jpg"
),
Booking(
    name="Osteria Positano",
    category=category,
    city="Miami",
    state="FL",
    lat=25.782942,  # Add the actual latitude
    lng=-80.1313247,  # Add the actual longitude
    description="Transport yourself to the flavors of Italy at Osteria Positano. Our authentic Italian cuisine, charming ambiance, and exceptional service create a memorable dining experience in the heart of Miami.",
    rating=4.6,
    contact_info="(555) 456-7890",
    website="osteriapositano.com",
    features="Italian Cuisine, Romantic Setting, Wine Selection",
    price=100,
    opening_hour="5:00 PM",
    closing_hour="10:30 PM",
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/fc/d9/b5/italian-restaurant-in.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/89/a0/84/italian-restaurant-in.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/89/a0/81/italian-restaurant-in.jpg?w=1200&h=800&s=1"
),
Booking(
    name="On Ocean 7 Cafe",
    category=category,
    city="Miami",
    state="FL",
    lat=25.7766653,  # Add the actual latitude
    lng=-80.131572,  # Add the actual longitude
    description="Discover a cozy retreat at On Ocean 7 Cafe. Our charming cafe offers a variety of delightful dishes in a relaxed atmosphere. Whether you're craving a delicious coffee or a tasty snack, we have something for every palate.",
    rating=4.2,
    contact_info="(555) 567-8901",
    website="onocean7cafe.com",
    features="Cafe, Coffee, Snacks",
    price=10,
    opening_hour="7:00 AM",
    closing_hour="6:00 PM",
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/f9/b9/10/on-ocean-7-cafe.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/f9/ba/5b/on-ocean-7-cafe.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/f9/b8/bf/on-ocean-7-cafe.jpg?w=1200&h=800&s=1"
)

    ]

    for restaurant in miami_restaurants:
        db.session.add(restaurant)

     #seed napa

    category = "Hotel"
    napa_hotels = [
    Booking(
    name='The Meritage Resort and Spa',
    category=category,
    city="Napa",
    state="CA",
    lat=38.246123,  # Add the actual latitude
    lng=-122.2741878,  # Add the actual longitude
    description="Experience luxury and relaxation at The Meritage Resort and Spa. Our resort offers exquisite accommodations, world-class spa services, and breathtaking views of the surrounding vineyards.",
    rating=4.5,
    contact_info="(555) 123-4567",
    website="meritageresort.com",
    features="Spa, Vineyard Views, Fine Dining",
    price=329,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/ca/23/70/meritage-resort-and-spa.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/21/f8/e5/cd/vineyards.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/21/f8/e5/c6/lawn-yoga.jpg"
),
Booking(
    name='Grand Reserve',
    category=category,
    city="Napa",
    state="CA",
    lat=38.2470521, # Add the actual latitude
    lng=-122.2731245,   # Add the actual longitude
    description="Indulge in luxury at Grand Reserve. Our hotel offers a refined atmosphere, spacious guestrooms, and a vineyard setting, providing an unforgettable stay in the heart of Napa Valley.",
    rating=4.7,
    contact_info="(555) 234-5678",
    website="grandreservenapa.com",
    features="Vineyard Views, Wine Tasting, Outdoor Pool",
    price=450,
    image1="https://media-cdn.tripadvisor.com/media/photo-w/14/04/b5/6c/vista-collina-resort.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/14/04/bd/06/double-guestroom.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/14/94/d2/8c/vista-collina-resort.jpg"
),
Booking(
    name='Carneros Resort and Spa',
    category=category,
    city="Napa",
    state="CA",
    lat=38.2557099,  # Add the actual latitude
    lng=-122.3351096,  # Add the actual longitude
    description="Discover ultimate tranquility at Carneros Resort and Spa. Our resort showcases luxurious accommodations, spa treatments, and panoramic views of the Napa Valley, creating an oasis for relaxation.",
    rating=4.8,
    contact_info="(555) 345-6789",
    website="carnerosresort.com",
    features="Spa, Gourmet Dining, Vineyard Cottages",
    price=749,
    image1="https://media-cdn.tripadvisor.com/media/photo-w/2a/a7/d6/6f/caption.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/16/c1/66/a3/carneros-resort-and-spa.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/16/c1/64/9b/carneros-resort-and-spa.jpg"
),
Booking(
    name='Candlelight Inn Napa Valley',
    category=category,
    city="Napa",
    state="CA",
    lat=38.303399,
    lng=-122.311396,  # Add the actual longitude
    description="Experience charm and elegance at Candlelight Inn Napa Valley. Our historic inn offers comfortable accommodations, beautiful gardens, and personalized service for a memorable stay.",
    rating=4.4,
    contact_info="(555) 456-7890",
    website="candlelightinn.com",
    features="Gardens, Gourmet Breakfast, Cozy Atmosphere",
    price=199,
    image1="https://media-cdn.tripadvisor.com/media/photo-w/0e/78/fb/49/side-view-of-the-house.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/07/d8/31/aa/candlelight-inn-napa.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/0e/78/fb/3c/view-of-the-house-through.jpg"
),
Booking(
    name='Archer Hotel Napa',
    category=category,
    city="Napa",
    state="CA",
    lat=38.2985362,  # Add the actual latitude
    lng=122.2876861,  # Add the actual longitude
    description="Immerse yourself in luxury at Archer Hotel Napa. Our boutique hotel combines modern elegance with Napa Valley's charm, offering sophisticated accommodations, a rooftop bar, and personalized service.",
    rating=4.6,
    contact_info="(555) 567-8901",
    website="archerhotel.com",
    features="Rooftop Bar, Boutique Accommodations, Wine Tasting",
    price=229,
    image1="https://media-cdn.tripadvisor.com/media/photo-w/2a/a7/80/dd/archer-hotel-napa-lobby.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/2a/a7/80/e7/archer-hotel-napa-lobby.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/29/60/b8/df/archer-hotel-napa-deluxe.jpg"
)
     ]

    for hotel in napa_hotels:
        db.session.add(hotel)

    category = "Things To Do"
    napa_things = [
Booking(
    name="Napa and Sonoma Wine Country Full-Day Tour from San Francisco",
    category="Things To Do",
    city="Napa",
    state="CA",
    lat=37.7882375,  # Add the actual latitude
    lng=-122.4096931,  # Add the actual longitude
    description="Embark on a full-day adventure exploring the picturesque Napa and Sonoma Wine Country. Enjoy wine tastings at renowned vineyards, savor local cuisine, and take in the stunning landscapes.",
    rating=4.8,
    contact_info="(555) 123-4567",
    website="winetourcompany.com",
    features="Wine Tasting, Vineyard Tours, Gourmet Lunch",
    price=160,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/09/4c/21/3c.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/75/6c/48.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/75/6c/4a.jpg"
),
Booking(
    name="Self Guided Full Day E-bike Rental With Picnic Lunch",
    category="Things To Do",
    city="Napa",
    state="CA",
    lat=38.2981548,  # Add the actual latitude
    lng=-122.2868175,  # Add the actual longitude
    description="Explore Napa at your own pace with a self-guided e-bike tour. Cruise through vineyards, enjoy a scenic picnic lunch, and experience the beauty of Napa Valley on two wheels.",
    rating=4.5,
    contact_info="(555) 234-5678",
    website="ebiketoursnapa.com",
    features="E-bike Rental, Self-Guided Tour, Picnic Lunch",
    price=179,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0f/1c/84/7c.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0f/1c/85/8e.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0f/2c/cc/26.jpg"
),
Booking(
    name="The Original Napa Valley Wine Trolley Classic Tour",
    category="Things To Do",
    city="Napa",
    state="CA",
    lat=38.3015876,  # Add the actual latitude
    lng=-122.2816788,  # Add the actual longitude
    description="Hop aboard the iconic Napa Valley Wine Trolley for a classic tour. Visit historic wineries, enjoy scenic views, and learn about the rich winemaking heritage of the region.",
    rating=4.7,
    contact_info="(555) 345-6789",
    website="winetrolleytours.com",
    features="Guided Trolley Tour, Wine Tastings, Historical Sites",
    price=125,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/07/9a/92/20.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0e/7f/a3/ba.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/2a/98/47/ba/caption.jpg"
)
    ]
    for thing in napa_things:
        db.session.add(thing)

    category = 'Restaurants'
    napa_restaurants = [
    Booking(
    name="Bistro Don Giovanni",
    category="Restaurants",
    city="Napa",
    state="CA",
    lat=38.3446769,  # Add the actual latitude
    lng=-122.3264692,  # Add the actual longitude
    description="Indulge in a delightful dining experience at Bistro Don Giovanni. Discover a menu featuring Italian cuisine, fresh ingredients, and a warm ambiance that complements the Napa Valley setting.",
    rating=4.7,
    contact_info="(555) 123-4567",
    website="bistrodongiovanni.com",
    features="Italian",
    price=100,
    opening_hour="11:00 AM",
    closing_hour="9:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/04/65/56/b6/bistro-don-giovanni.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/12/a6/b9/fb/bistro-don-giovanni.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-l/1d/9a/7e/c0/caption.jpg"
),
Booking(
    name="Wit & Wisdom",
    category="Restaurants",
    city="Napa",
    state="CA",
    lat=38.2773803,  # Add the actual latitude
    lng=-122.4605143,  # Add the actual longitude
    description="Experience culinary excellence at Wit & Wisdom. Delight in a modern American menu, crafted with seasonal ingredients, and savor exquisite dishes in an inviting atmosphere.",
    rating=4.6,
    contact_info="(555) 234-5678",
    website="witandwisdomnapa.com",
    features="American",
    price=100,
    opening_hour="5:00 PM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/1b/fa/45/c1/grab-a-seat-at-the-bar.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/1b/fa/45/90/crispy-berkshire-porchetta.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/1b/fa/48/fb/fresh-local-fruits-and.jpg"
),
Booking(
    name="LaSalette Restaurant",
    category="Restaurants",
    city="Napa",
    state="CA",
    lat=38.2926861,  # Add the actual latitude
    lng=-122.45585,  # Add the actual longitude
    description="Immerse yourself in Portuguese flavors at LaSalette Restaurant. Enjoy a unique culinary journey with a menu inspired by the rich and diverse traditions of Portuguese cuisine.",
    rating=4.9,
    contact_info="(555) 345-6789",
    website="lasaletterestaurant.com",
    features="Portuguese",
    price=1000,
    opening_hour="5:30 PM",
    closing_hour="9:30 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/09/c2/e5/fd/lasalette-restaurant.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-l/1b/f5/d0/4c/img-20200906-200010-largejpg.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/1c/da/16/f0/20210412-125746-largejpg.jpg"
),
Booking(
    name="the girl & the fig",
    category="Restaurants",
    city="Napa",
    state="CA",
    lat=38.293948,  # Add the actual latitude
    lng=-122.45883,  # Add the actual longitude
    description="Discover a farm-to-table dining experience at the girl & the fig. Delight in French-inspired cuisine featuring locally sourced ingredients and a charming ambiance in the heart of Napa.",
    rating=4.5,
    contact_info="(555) 456-7890",
    website="thegirlandthefig.com",
    features="French",
    price=10,
    opening_hour="4:00 PM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/1d/29/e0/c5/roasted-half-chicken.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-l/1d/b4/b5/e8/local-king-salmon-pepperonata.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-l/1d/86/b5/10/gulf-shrimp-corn-sweet.jpg"
),


    ]
    for restaurant in napa_restaurants:
        db.session.add(restaurant)

     #seed boston
    category ="Restaurants"
    city="Boston"
    state="MA"
    boston_restaurants = [
    Booking(
    name="Legal Sea Foods",
    category=category,
    city=city,
    state=state,
    lat=42.3590,
    lng=-71.0495,
    description="A Boston classic, Legal Sea Foods offers the freshest seafood in a vibrant waterfront setting. Immerse yourself in a culinary experience synonymous with quality and tradition.",
    rating=4.5,
    contact_info="(617) 123-4567",
    website="legalseafoods.com",
    features="Seafood",
    price=1000,
    opening_hour="11:00 AM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-f/1c/b3/f0/c8/oysters.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/21/21/a0/2f/long-wharf.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/1c/b3/f5/07/calamari.jpg"
    ),
    Booking(
    name="Union Oyster House",
    lat=42.3614,
    lng=-71.0569,
    city=city,
    state=state,
    category=category,
    description="Steeped in history, Union Oyster House is the oldest continuously operating restaurant in the United States. Enjoy classic New England fare in an atmospheric colonial setting.",
    rating=4.3,
    contact_info="(617) 234-5678",
    website="unionoysterhouse.com",
    features="Seafood, American",
    price=10,
    opening_hour="11:30 AM",
    closing_hour="9:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-p/16/ad/1e/25/photo6jpg.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/16/ad/1e/1f/photo0jpg.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-l/1d/39/79/6c/caption.jpg"
),
    Booking(
    name="Mike's Pastry",
    lat=42.3632,
    lng=-71.0569,
    city=city,
    state=state,
    category=category,
    description="A North End gem, Mike's Pastry is renowned for its delectable pastries and cannoli. Join the queue for a taste of authentic Italian sweets in a bustling neighborhood.",
    rating=4.6,
    contact_info="(617) 456-7890",
    website="mikespastry.com",
    features="Bakery, Italian",
    price=10,
    opening_hour="8:00 AM",
    closing_hour="10:00 PM",
    image1='https://media-cdn.tripadvisor.com/media/photo-s/17/f0/6d/ed/when-in-boston-go-to.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-l/1d/07/53/65/photo3jpg.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-s/1c/d2/df/f4/photo3jpg.jpg'
),

    Booking(
    name="Myers + Chang",
    lat=42.3435,
    lng=-71.0610,
    city=city,
    state=state,
    category=category,
    description="Experience the vibrant fusion of flavors at Myers + Chang, a modern Asian-inspired eatery. Creative dishes and a lively atmosphere make it a local favorite.",
    rating=4.4,
    contact_info="(617) 567-8901",
    website="myersandchang.com",
    features="Asian Fusion",
    price=100,
    opening_hour="5:00 PM",
    closing_hour="11:00 PM",
    image1='https://media-cdn.tripadvisor.com/media/photo-s/0c/92/8e/ed/photo2jpg.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-s/1a/0f/05/93/photo2jpg.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-f/10/d9/46/15/the-tuna-poke.jpg'
),
    Booking(
    name="Neptune Oyster",
    lat=42.3636,
    lng=-71.0567,
    city=city,
    state=state,
    category=category,
    description="A hidden gem in the North End, Neptune Oyster is celebrated for its fresh seafood and intimate atmosphere. Seating is limited, but the experience is unparalleled.",
    rating=4.8,
    contact_info="(617) 234-5678",
    website="neptuneoyster.com",
    features="Seafood",
    price=100,
    opening_hour="11:30 AM",
    closing_hour="10:00 PM",
    image1='https://media-cdn.tripadvisor.com/media/photo-s/19/a4/c1/f3/photo5jpg.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-s/18/ec/d8/0b/lobster-roll-and-fries.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-l/1d/aa/1a/49/caption.jpg'
),
    Booking(
    name="Oleana",
    lat=42.3725,
    lng=-71.1028,
    city=city,
    state=state,
    category=category,
    description="Discover the flavors of the Mediterranean at Oleana. This cozy restaurant in Cambridge offers a seasonal menu featuring inventive dishes with a focus on local ingredients.",
    rating=4.5,
    contact_info="(617) 345-6789",
    website="oleanarestaurant.com",
    features="Mediterranean",
    price=1000,
    opening_hour="5:30 PM",
    closing_hour="10:00 PM",
    image1='https://media-cdn.tripadvisor.com/media/photo-s/1a/98/5c/cc/great-food-and-service.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-s/0f/d9/d1/1a/some-of-the-great-dishes.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-l/18/e4/b6/08/zucchini-pancakes-oleana.jpg'
),
Booking(
    name="Ciccio",
    category="Restaurants",
    city="Napa",
    state="CA",
    lat=38.4065875,  # Add the actual latitude
    lng=-122.3668438,  # Add the actual longitude
    description="Immerse yourself in the vibrant ambiance of Ciccio, offering a diverse menu inspired by Italian flavors. From classic pasta dishes to innovative creations, Ciccio promises a delightful culinary journey.",
    rating=4.3,
    contact_info="(555) 567-8901",
    website="ciccio.com",
    features="Italian Cuisine, Pasta, Innovative Creations",
    price=100,
    opening_hour="4:00 PM",
    closing_hour="9:30 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/05/71/16/b4/ciccio.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-o/03/42/08/4a/all-decked-out-for-the.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-l/16/e6/38/10/photo0jpg.jpg"
)
]

    for restaurant in boston_restaurants:
        db.session.add(restaurant)

    category ="Hotel"

    boston_hotels = [
    Booking(
    name="Boston Harbor Hotel",
    lat=42.3561,
    lng=-71.0525,
    city=city,
    state=state,
    category=category,
    description="Experience luxury on the waterfront at Boston Harbor Hotel. Enjoy unparalleled views, exquisite accommodations, and world-class amenities.",
    rating=4.9,
    contact_info="(617) 123-4567",
    website="bhh.com",
    features="Spa, Fine Dining, Waterfront Views",
    price=400,
    image1='https://media-cdn.tripadvisor.com/media/photo-w/21/8f/6d/c9/boston-harbor-hotel.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-o/2a/fa/cb/bf/constitution-suite.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-s/2a/b7/ec/ce/meeting-space.jpg'
),
Booking(
    name="The Liberty Hotel",
    lat=42.3614,
    lng=-71.0672,
    city=city,
    state=state,
    category=category,
    description="A historic landmark transformed into a luxury hotel, The Liberty Hotel offers a blend of modern elegance and historic charm. Enjoy upscale accommodations in the heart of Boston.",
    rating=4.6,
    contact_info="(617) 234-5678",
    website="libertyhotel.com",
    features="Rooftop Bar, Fitness Center, Spa",
    price=209,
    image1='https://media-cdn.tripadvisor.com/media/photo-w/15/23/38/4f/grand-deluxe-courtyard.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-w/15/23/37/ce/the-liberty-ballroom.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-s/15/04/10/4a/the-liberty-a-luxury.jpg'
),
Booking(
    name="Four Seasons Hotel Boston",
    lat=42.3472,
    lng=-71.0767,
    city=city,
    state=state,
    category=category,
    description="Indulge in luxury at the Four Seasons Hotel Boston. Impeccable service, spacious rooms, and a central location make it a top choice for discerning travelers.",
    rating=4.8,
    contact_info="(617) 345-6789",
    website="fourseasons.com/boston",
    features="Fine Dining, Spa, Indoor Pool",
    price=795,
    image1='https://media-cdn.tripadvisor.com/media/photo-w/0e/af/56/e3/boston-public-garden.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-s/0f/7f/14/d2/four-seasons-executive.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-s/0f/7f/13/c5/deluxe-king-bedded-room.jpg'
),
Booking(
    name="The Ritz-Carlton, Boston",
    lat=42.3512,
    lng=-71.0731,
    city=city,
    state=state,
    category=category,
    description="Experience opulence at The Ritz-Carlton, Boston. Elegant rooms, gourmet dining, and personalized service define this luxury hotel in the heart of the city.",
    rating=4.7,
    contact_info="(617) 456-7890",
    website="ritzcarlton.com/boston",
    features="Spa, Michelin-starred Restaurant, Concierge Service",
    price=695,
    image1='https://media-cdn.tripadvisor.com/media/photo-w/0f/b6/de/81/the-ritz-carlton-boston.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-o/04/0f/45/e5/ritz-carlton-boston-common.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-s/06/be/14/4f/the-ritz-carlton-boston.jpg'
),
Booking(
    name="XV Beacon",
    lat=42.3589,
    lng=-71.0630,
    city=city,
    state=state,
    category=category,
    description="Discover boutique luxury at XV Beacon. With its historic charm and modern amenities, this intimate hotel provides a unique and elegant retreat in downtown Boston.",
    rating=4.5,
    contact_info="(617) 987-6543",
    website="xvbeacon.com",
    features="Rooftop Terrace, Fireplace Suites, In-room Spa Services",
    price=495,
    image1='https://media-cdn.tripadvisor.com/media/oyster/730/14/bd/7b/6e/lobby-v18588585.jpg',
    image2='https://media-cdn.tripadvisor.com/media/oyster/500/14/bd/7b/5b/house-lexus-v18588579.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-o/1c/18/77/98/boston-common-studio.jpg'
)
    ]

    for hotel in boston_hotels:
        db.session.add(hotel)
    category ="Things To Do"
    boston_things =[
    Booking(
    name="Freedom Trail Walking Tour",
    lat=42.3584,
    lng=-71.0636,
    city=city,
    state=state,
    category=category,
    description="Embark on a historical journey with a guided Freedom Trail Walking Tour. Explore Boston's rich past, visiting iconic landmarks such as the Massachusetts State House and Paul Revere's House.",
    rating=4.7,
    contact_info="(617) 123-4567",
    website="freedomtrail.org",
    features="Historical Landmarks, Guided Tour",
    price=39,
    image1='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/0e/3d/d1/b1.jpg',
    image2='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/10/24/ef/2b.jpg',
    image3='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/10/5a/94/4c.jpg'
),
Booking(
    name="Boston Harbor Sunset Cruise",
    lat=42.3553,
    lng=-71.0504,
    city=city,
    state=state,
    category=category,
    description="Sail into the sunset aboard a Boston Harbor Sunset Cruise. Enjoy breathtaking views of the city skyline, historic sites, and harbor islands while experiencing the beauty of dusk on the water.",
    rating=4.5,
    contact_info="(617) 234-5678",
    website="bostonharborcruises.com",
    features="Scenic Views, Live Entertainment, Refreshments",
    price=45,
    image1='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/06/71/cb/e7.jpg',
    image2='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/07/1a/96/66.jpg',
    image3='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/06/e3/18/18.jpg'
),
Booking(
    name="Museum of Fine Arts",
    lat=42.3394,
    lng=-71.0942,
    city=city,
    state=state,
    category=category,
    description="Immerse yourself in art at the Museum of Fine Arts. Explore a diverse collection spanning centuries and cultures, featuring paintings, sculptures, and decorative arts.",
    rating=4.8,
    contact_info="(617) 345-6789",
    website="mfa.org",
    features="Art Exhibits, Special Exhibitions, Cafeteria",
    price=59,
    image1='https://media-cdn.tripadvisor.com/media/photo-w/10/7e/20/f3/photo0jpg.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-w/08/af/1b/c8/museum-of-fine-arts.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-p/08/af/1b/7f/museum-of-fine-arts.jpg'
),
Booking(
    name="Fenway Park Tour",
    lat=42.3465,
    lng=-71.0978,
    city=city,
    state=state,
    category=category,
    description="Step into baseball history with a Fenway Park Tour. Discover the iconic stadium's storied past, explore the dugout, and relive memorable moments from Red Sox history.",
    rating=4.6,
    contact_info="(617) 456-7890",
    website="redsox.com/tours",
    features="Baseball History, Behind-the-Scenes Access",
    price=33.34,
    image1='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/10/3e/d7/a1.jpg',
    image2='https://media-cdn.tripadvisor.com/media/photo-s/2a/fd/90/83/caption.jpg',
    image3='https://media-cdn.tripadvisor.com/media/photo-s/2a/f1/7f/c8/caption.jpg'
),
Booking(
    name="Boston Tea Party Ships & Museum",
    lat=42.3592,
    lng=-71.0519,
    city=city,
    state=state,
    category=category,
    description="Experience the Boston Tea Party like never before at the Boston Tea Party Ships & Museum. Participate in interactive exhibits, witness a reenactment, and learn about this pivotal moment in history.",
    rating=4.7,
    contact_info="(617) 987-6543",
    website="bostonteapartyship.com",
    features="Interactive Exhibits, Reenactments, Gift Shop",
    price=34,
    image1='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/0b/1d/d7/bb.jpg',
    image2='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-480x320/0b/1d/d7/3b.jpg',
    image3='https://media-cdn.tripadvisor.com/media/attractions-splice-spp-360x240/0a/0a/6b/f8.jpg'
)
    ]

    for thing in boston_things:
        db.session.add(thing)

    #seed jacskon
    jackson_restaurants =[
    Booking(
    name="The Blue Lion",
    category="Restaurants",
    city="Jackson",
    state="WY",
    lat=43.48125,  # Add the actual latitude
    lng=-110.7647861,  # Add the actual longitude
    description="Experience a cozy and elegant dining atmosphere at The Blue Lion. Known for its delectable American cuisine and attentive service, it's a perfect spot for a memorable evening in Jackson.",
    rating=3.5,
    contact_info="(555) 123-4567",
    website="bluelionrestaurant.com",
    features="American Cuisine, Cozy Atmosphere",
    price=100,
    opening_hour="5:00 PM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/10/e6/9f/ab/deck-seating-in-the-summer.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/10/e6/9f/4a/dining-in-a-cozy-historic.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/10/e6/9e/56/the-world-renowned-rack.jpg"
),
Booking(
    name="Snake River Grill",
    category="Restaurants",
    city="Jackson",
    state="WY",
    lat=43.4792525,
    lng=-110.7610536,  # Add the actual longitude
    description="Indulge in a culinary journey at Snake River Grill, renowned for its innovative dishes using locally sourced ingredients. The rustic yet sophisticated ambiance adds to the charm of this Jackson gem.",
    rating=4.2,
    contact_info="(555) 234-5678",
    website="snakerivergrill.com",
    features="Innovative Cuisine, Locally Sourced Ingredients",
    price=1000,
    opening_hour="4:30 PM",
    closing_hour="9:30 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/0f/ed/da/fb/srg-deck-summer.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-p/1a/bb/74/e7/photo0jpg.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/10/3c/73/62/photo1jpg.jpg"
),
Booking(
    name="Local Restaurant & Bar",
    category="Restaurants",
    city="Jackson",
    state="WY",
    lat=43.480049,  # Add the actual latitude
    lng=-110.7625025,  # Add the actual longitude
    description="Embrace the local flavors at Local Restaurant & Bar. With a diverse menu featuring regional ingredients, this spot offers a welcoming atmosphere for a delightful dining experience in Jackson.",
    rating=2.8,
    contact_info="(555) 345-6789",
    website="localrestaurantwy.com",
    features="Regional Cuisine, Welcoming Atmosphere",
    price=100,
    opening_hour="11:00 AM",
    closing_hour="11:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/10/e4/cc/ef/come-on-in-and-join-us.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/11/c1/fd/e1/bacon-wedge-salad.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/11/c1/fe/23/meat-and-magnum-enjoy.jpg"
),
Booking(
    name="Gather",
    category="Restaurants",
    city="Jackson",
    state="WY",
    lat=43.4787506,  # Add the actual latitude
    lng=-110.7635154,  # Add the actual longitude
    description="Discover the vibrant culinary scene at Gather, a restaurant known for its contemporary American cuisine. With a focus on fresh and seasonal ingredients, it's a must-visit in Jackson.",
    rating=4.7,
    contact_info="(555) 456-7890",
    website="gatherjackson.com",
    features="Contemporary American Cuisine, Fresh Ingredients",
    price=1000,
    opening_hour="5:30 PM",
    closing_hour="10:30 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-f/07/49/42/5e/gather.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-l/17/ba/b4/dc/red-wine-marinated-bison.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/07/e2/7b/9e/gather.jpg"
),

Booking(
    name="Persephone Bakery",
    category="Restaurants",
    city="Jackson",
    state="WY",
    lat=43.479763,
    lng=-110.760007,
    description="Indulge in a delightful culinary experience at Persephone Bakery, known for its artisanal bread, pastries, and exquisite brunch options. With a charming atmosphere and a commitment to quality ingredients, it's a perfect spot for breakfast or a cozy coffee date.",
    rating=4.5,
    contact_info="(307) 200-6708",
    website="persephonebakery.com",
    features="Artisanal Baked Goods, Brunch",
    price=100,
    opening_hour="7:00 AM",
    closing_hour="3:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/10/7e/2a/2d/fresh-and-hearty-breakfast.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/14/2c/23/1f/persephone-breakfast.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/0f/f5/c1/4f/truffled-scone-skillet.jpg"
)

    ]

    for restaurant in jackson_restaurants:
        db.session.add(restaurant)


    jackson_hotels = [
        Booking(
    name="Hotel Jackson",
    category="Hotel",
    city="Jackson",
    state="WY",
    lat=43.4799,
    lng=-110.7624,
    description="Experience luxury and comfort at Hotel Jackson, where Western charm meets modern elegance. With spacious rooms, a gourmet restaurant, and attentive service, it's the perfect retreat in the heart of Jackson Hole.",
    rating=4.8,
    contact_info="(307) 733-2200",
    website="hoteljackson.com",
    features="Gourmet Dining, Spa, Concierge",
    price=281,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/3f/0a/87/hotel-jackson-s-contemporary.jpg",
    image2="https://cf.bstatic.com/xdata/images/hotel/max1024x768/347921580.jpg",
    image3="https://image-tc.galaxy.tf/wijpeg-nyb9l5sodupoq6xaveu0cioi/miller-suite-view.jpg"
),
Booking(
    name="The Wort Hotel",
    category="Hotel",
    city="Jackson",
    state="WY",
    lat=43.4782,
    lng=-110.7628,
    description="Immerse yourself in Western heritage at The Wort Hotel. Offering classic charm, comfortable accommodations, and a historic saloon, this landmark hotel provides an authentic Jackson Hole experience.",
    rating=4.6,
    contact_info="(307) 733-2190",
    website="worthotel.com",
    features="Historic Saloon, Live Music",
    price=314,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/7a/81/2c/the-wort-hotel.jpg",
    image2="https://wort-hotel.s3.amazonaws.com/101/the_wort_hotel-16__detail.jpg",
    image3="https://wort-hotel.s3.amazonaws.com/102/191216_0955v2-web__detail.jpg"
),
Booking(
    name="Amangani",
    category="Hotel",
    city="Jackson",
    state="WY",
    lat=43.5040497,
    lng=-110.7743935,
    description="Escape to luxury at Amangani, a tranquil retreat overlooking the majestic Teton Mountains. With spacious suites, a world-class spa, and breathtaking views, it's a haven for those seeking relaxation and natural beauty.",
    rating=4.9,
    contact_info="(307) 734-7333",
    website="aman.com/amangani",
    features="Spa, Mountain Views, Fine Dining",
    price=890,
    image1="https://www.aman.com/sites/default/files/2022-11/Amangani%2C%20Exterior.jpg",
    image2="https://www.aman.com/sites/default/files/styles/full_size_extra_large/public/2022-07/Website%20-%20Landscape%20.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/78/d5/51/amangani.jpg"
),
Booking(
    name="The Lodge at Jackson Hole",
    category="Hotel",
    city="Jackson",
    state="WY",
    lat=43.4730138,
    lng=-110.7819396,
    description="Discover comfort and convenience at The Lodge at Jackson Hole. Featuring rustic elegance, an outdoor pool, and proximity to downtown attractions, it's an ideal choice for both relaxation and exploration.",
    rating=4.4,
    contact_info="(307) 739-9703",
    website="lodgeatjh.com",
    features="Outdoor Pool, Mountain Views",
    price=189,
    image1="https://cf.bstatic.com/xdata/images/hotel/max1024x768/26969759.jpg",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/e3/5a/95/l-p-dbl-q-room.jpg",
    image3="https://assets.hospitalityonline.com/photos/employers/277759/884288_l.jpg"
),
Booking(
    name="SpringHill Suites by Marriott Jackson Hole",
    category="Hotel",
    city="Jackson",
    state="WY",
    lat=43.4770905,
    lng=-110.764434,
    description="Experience modern comfort at SpringHill Suites. Offering spacious suites, an indoor pool, and complimentary breakfast, it's a welcoming home base for visitors exploring the wonders of Jackson Hole.",
    rating=4.5,
    contact_info="(307) 201-5320",
    website="marriott.com/jacsh",
    features="Indoor Pool, Complimentary Breakfast",
    price=259,
    image1="https://cache.marriott.com/content/dam/marriott-renditions/JACSH/jacsh-exterior-0003-hor-clsc.jpg",
    image2="https://cache.marriott.com/content/dam/marriott-renditions/JACSH/jacsh-suite-0008-hor-wide.jpg",
    image3="https://cf.bstatic.com/xdata/images/hotel/max1024x768/486764320.jpg"
)
    ]

    for hotel in jackson_hotels:
        db.session.add(hotel)

    jackson_things = [
    Booking(
    name="Jackson Hole Mountain Resort",
    category="Things To Do",
    city="Jackson",
    state="WY",
    lat=43.5942458,
    lng=-110.8437169,
    description="Experience world-class skiing and stunning views at Jackson Hole Mountain Resort. Whether you're a seasoned skier or enjoying the aerial tram, it's an adventure-packed destination.",
    rating=4.8,
    contact_info="(307) 733-2292",
    website="jacksonhole.com",
    features="Skiing, Scenic Views",
    price=89.99,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/02/51/fa/34/jackson-hole-ski-resort.jpg?w=1100&h=800&s=1",
    image2="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/83/db/b8/people-hiking-together.jpg?w=2400&h=1800&s=1",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/83/db/b2/the-aerial-tram-flying.jpg?w=2400&h=1800&s=1"
),
Booking(
    name="National Museum of Wildlife Art",
    category="Things To Do",
    city="Jackson",
    state="WY",
    lat=43.5195032,
    lng=-110.748766,
    description="Immerse yourself in the beauty of wildlife art at the National Museum of Wildlife Art. With a diverse collection and scenic surroundings, it's a cultural gem in Jackson.",
    rating=4.5,
    contact_info="(307) 733-5771",
    website="wildlifeart.org",
    features="Art Exhibits, Scenic Location",
    price=24.99,
    image1="https://d16kd6gzalkogb.cloudfront.net/magazine_images/Wapiti-Trail-by-Bart-Walter-at-the-National-Museum-of-Wildlife-Art.jpg",
    image2="https://www.wildlifeart.org/wp-content/uploads/2021/09/Exploring-Wildlife-Art-Jackson-Hole-Wyoming-1200x800.jpg",
    image3="https://live.staticflickr.com/65535/46958716855_8ca0f1a23b_b.jpg"
),
Booking(
    name="Snake River Whitewater Rafting",
    category="Things To Do",
    city="Jackson",
    state="WY",
    lat=43.472553,
    lng=-110.7860642,
    description="Embark on an exhilarating whitewater rafting adventure on the Snake River. With experienced guides and thrilling rapids, it's an unforgettable experience for outdoor enthusiasts.",
    rating=4.7,
    contact_info="(307) 733-1000",
    website="snakeriverpark.com",
    features="Whitewater Rafting, Scenic Views",
    price=89.99,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/6f/20/6f.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/6f/20/71.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/d9/7d/29.jpg"
),
Booking(
    name="Jackson Hole Rodeo",
    category="Things To Do",
    city="Jackson",
    state="WY",
    lat=43.3689481,
    lng=-110.7399183,
    description="Experience the excitement of the Old West at the Jackson Hole Rodeo. Witness thrilling rodeo events, live entertainment, and immerse yourself in cowboy culture.",
    rating=4.6,
    contact_info="(307) 733-7980",
    website="jhrodeo.com",
    features="Rodeo Events, Live Entertainment",
    price=29.99,
    image1="https://jhrodeo.com/wp-content/uploads/2022/05/Jackson-Hole-Rodeo-Bareback-Riding.jpg",
    image2="https://jacksonhole-traveler-production.s3.amazonaws.com/wp-content/uploads/2014/08/Jackson-Hole-Rodeo-Grandstand-1280x960.jpg",
    image3="https://jhrodeo.com/wp-content/uploads/2022/06/Meet-the-Crew.jpg"
)
    ]

    for thing in jackson_things:
        db.session.add(thing)

    #seed nashville
    nashville_restaurants = [
        Booking(
    name="Hattie B's Hot Chicken",
    category="Restaurants",
    city="Nashville",
    state="TN",
    lat=36.1526,
    lng=-86.7965,
    description="Savor the iconic Nashville hot chicken at Hattie B's. Choose your spice level and enjoy the perfect blend of crispy, flavorful chicken.",
    rating=4.7,
    contact_info="(615) 678-4794",
    website="hattieb.com",
    features="Hot Chicken, Southern Cuisine",
    price=100,
    opening_hour="11:00 AM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/1a/4a/f1/f3/the-best-spicy-chicken.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/0d/53/00/8e/a-typical-meal-at-hattie.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/1c/a5/c2/23/the-plate.jpg"
),
Booking(
    name="The Stillery",
    category="Restaurants",
    city="Nashville",
    state="TN",
    lat=36.1590,
    lng=-86.7759,
    description="Indulge in Southern comfort food and live music at The Stillery. From handcrafted pizzas to signature cocktails, it's a lively spot on Broadway.",
    rating=4.5,
    contact_info="(615) 942-8080",
    website="stillerynashville.com",
    features="Live Music, Pizza",
    price=100,
    opening_hour="11:00 AM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-p/15/d9/50/42/photo1jpg.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/0b/5f/15/b4/this-was-the-sonoran.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/1c/b9/8b/e4/pxl-20210307-201304120.jpg"
),
Booking(
    name="Biscuit Love",
    category="Restaurants",
    city="Nashville",
    state="TN",
    lat=36.1530503,
    lng=-86.7832308,
    description="Experience a Southern breakfast at its best. Biscuit Love serves up delicious biscuits, brunch favorites, and a warm, welcoming atmosphere.",
    rating=4.6,
    contact_info="(615) 610-3336",
    website="biscuitlove.com",
    features="Biscuits, Brunch, Southern Breakfast",
    price=10,
    opening_hour="7:00 AM",
    closing_hour="3:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-p/15/6e/2f/3e/photo0jpg.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/1a/68/90/cb/fresh-out-of-the-oven.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-l/1a/68/90/c2/bonuts.jpg"
),
Booking(
    name="Prince's Hot Chicken Shack",
    category="Restaurants",
    city="Nashville",
    state="TN",
    lat=36.1612745,
    lng=-86.779233,
    description="Home of the original Nashville hot chicken! Prince's Hot Chicken Shack offers fiery and flavorful hot chicken for those who crave some heat.",
    rating=4.4,
    contact_info="(615) 226-9442",
    website="princeshotchicken.com",
    features="Hot Chicken, Spicy, Casual Dining",
    price=10,
    opening_hour="11:00 AM",
    closing_hour="4:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/1c/79/f6/b7/20201230-160850-largejpg.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/1c/79/f6/bb/20201230-164401-largejpg.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-o/1c/79/f6/bd/20201230-164443-largejpg.jpg"
),
Booking(
    name="Martin's Bar-B-Que Joint",
    category="Restaurants",
    city="Nashville",
    state="TN",
    lat=36.1567715,
    lng=-86.774038,
    description="Savor the authentic taste of Tennessee barbecue at Martin's Bar-B-Que Joint. Enjoy slow-cooked meats, savory sides, and a laid-back atmosphere.",
    rating=4.5,
    contact_info="(615) 864-5650",
    website="martinsbbqjoint.com",
    features="Barbecue, Ribs, Southern BBQ",
    price=100,
    opening_hour="11:00 AM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/12/ae/01/14/bar.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/0f/23/01/e4/kid-brother-sampler.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/1c/2a/ce/fe/photo0jpg.jpg"
)
    ]
    for restaurant in nashville_restaurants:
        db.session.add(restaurant)

    nashville_hotels = [
    Booking(
    name="The Hermitage Hotel",
    category="Hotel",
    city="Nashville",
    state="TN",
    lat=36.1637611,
    lng=-86.7823611,
    description="Experience luxury and Southern hospitality at The Hermitage Hotel. This historic landmark offers opulent rooms, award-winning dining, and a prime location in downtown Nashville.",
    rating=4.8,
    contact_info="(615) 244-3121",
    website="thehermitagehotel.com",
    features="Fine Dining, Spa, Historic Ambiance",
    price=400,
    image1="https://www.thehermitagehotel.com/wp-content/uploads/2023/02/Home_Page_Header_2560_x_1500-1920x1080.jpg",
    image2="https://www.kayak.com/rimg/himg/0f/c2/d7/ice-16082-102019648-305994.jpg?width=1366&height=768&crop=true",
    image3="https://www.thehermitagehotel.com/wp-content/uploads/2023/01/Rooms__Suites_Page_Studio_Suite-1024x600.jpg"
),
Booking(
    name="Omni Nashville Hotel",
    category="Hotel",
    city="Nashville",
    state="TN",
    lat=36.1572621,
    lng=-86.7754139,
    description="Discover the vibrant energy of Nashville at Omni Nashville Hotel. With modern accommodations, a rooftop pool, and proximity to popular attractions, it's an ideal choice for visitors.",
    rating=4.5,
    contact_info="(615) 782-5300",
    website="omnihotels.com/nashville",
    features="Rooftop Pool, Fitness Center, On-site Dining",
    price=300,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/08/74/ab/omni-nashville-hotel.jpg",
    image2="https://www.omnihotels.com/-/media/images/hotels/bnadtn/digex/carousel/bnadtn_3_2880x1870.jpeg",
    image3="https://www.oyster.com/wp-content/uploads/sites/35/2019/05/pool-v9931054-1440-1024x683.jpg"
),
Booking(
    name="Thompson Nashville",
    category="Hotel",
    city="Nashville",
    state="TN",
    lat=36.1523179,
    lng=-86.7840306,
    description="Immerse yourself in the vibrant culture of Nashville at Thompson Nashville. Stylish rooms, a rooftop bar with live music, and a central location make it a top choice for travelers.",
    rating=4.6,
    contact_info="(615) 262-6000",
    website="thompsonhotels.com/nashville",
    features="Rooftop Bar, Live Music, Modern Design",
    price=350,
    image1="https://assets.hyatt.com/content/dam/hyatt/hyattdam/images/2019/03/15/1127/Thompson-Nashville-P016-Exterior-View.jpg/Thompson-Nashville-P016-Exterior-View.16x9.jpg",
    image2="https://media.cntraveler.com/photos/58f536bdd3e4d55528e7764c/16:9/w_2560,c_limit/Lobby-ThompsonNashville-Tennessee-CRHotel.jpg",
    image3="https://assets.hyatt.com/content/dam/hyatt/hyattdam/images/2019/02/07/1444/Thompson-Nashville-P001-Neighborhood-View-King.jpg/Thompson-Nashville-P001-Neighborhood-View-King.16x9.jpg"
),
Booking(
    name="Noelle, Nashville, a Tribute Portfolio Hotel",
    category="Hotel",
    city="Nashville",
    state="TN",
    lat=36.1640057,
    lng=-86.778751,
    description="Experience a blend of modern luxury and historic charm at Noelle, a Tribute Portfolio Hotel. Unique design, curated amenities, and a central location make it a standout choice.",
    rating=4.7,
    contact_info="(615) 649-5000",
    website="noelle-nashville.com",
    features="Boutique Style, Rooftop Lounge, Artistic Ambiance",
    price=280,
    image1="https://cdn.noelle-nashville.com/assets/uploads/2019/02/StudioSuite2-1024x683.jpg",
    image2="https://cdn.noelle-nashville.com/assets/uploads/2018/11/171215_Noelle_Interiors0029.jpg",
    image3="https://www.idcconstruction.com/wp-content/uploads/Noelle12.jpg"
),
Booking(
    name="Hutton Hotel",
    category="Hotel",
    city="Nashville",
    state="TN",
    lat=36.1530416,
    lng=-86.797068,
    description="Discover refined comfort and sophistication at Hutton Hotel. Elegant rooms, a signature restaurant, and a focus on sustainability make it a distinctive choice in Nashville.",
    rating=4.5,
    contact_info="(615) 340-9333",
    website="huttonhotel.com",
    features="Signature Restaurant, Sustainability, Modern Design",
    price=250,
    image1="https://costar.brightspotcdn.com/ff/e6/7b82d0864de594522e05f4cb8b8f/huttonhotel.jpeg",
    image2="https://media.cntraveler.com/photos/5a734cd62ed5fb182058f94c/16:9/w_2560%2Cc_limit/Hutton-Hotel-2018-Lobby-@-Hutton-Hotel-1_credit-Nils-Schlebusch.jpg",
    image3="https://cf.bstatic.com/xdata/images/hotel/max1024x768/130607073.jpg"
)
    ]

    for hotel in nashville_hotels:
        db.session.add(hotel)

    nashville_things = [
        Booking(
    name="Country Music Hall of Fame and Museum Admission",
    category="Things To Do",
    city="Nashville",
    state="TN",
    lat=36.1582632,
    lng=-86.7761258,
    description="Explore the rich history of country music at the Country Music Hall of Fame and Museum. Discover exhibits, memorabilia, and interactive displays that celebrate the genre's legendary artists.",
    price=27.95,
    rating=3.2,
    features="Exhibits, Memorabilia, Interactive Displays",
    contact_info="(615) 416-2001",
    website="countrymusichalloffame.org",
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/09/15/cf/8a.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/be/9c/05.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/ef/19/49.jpg"
),
Booking(
    name="Admission to Ryman Auditorium",
    category="Things To Do",
    city="Nashville",
    state="TN",
    lat=36.1612481,
    lng=-86.7784714,
    description="Visit the historic Ryman Auditorium, known as the 'Mother Church of Country Music.' Take a guided tour to explore the iconic venue that has hosted legendary performances throughout the years.",
    rating=4.8,
    contact_info="(615) 889-3060",
    website="ryman.com",
    features="Guided Tours, Live Music Venue",
    price=35.52,
    image1="https://www.trolleytours.com/wp-content/uploads/2016/06/nashville-ryman-auditorium.jpg",
    image2="https://parkmobile.io/wp-content/uploads/2022/06/visiting-ryman-auditorium-history-and-venue-info-guide-2-scaled.jpg",
    image3="https://media.tacdn.com/media/attractions-splice-spp-674x446/09/15/d2/6f.jpg"
),
Booking(
    name="Nashville Hot Chicken Cooking Class",
    category="Things To Do",
    city="Nashville",
    state="TN",
    lat=36.1740488,
    lng=-86.7613955,
    description="Join a Nashville Hot Chicken cooking class to learn the secrets behind this iconic dish. Enjoy a hands-on experience and savor the delicious flavors of this spicy and savory specialty.",
    rating=4.9,
    contact_info="(615) 555-1234",
    website="cookingclassnashville.com",
    features="Hands-on Cooking, Culinary Experience, Nashville Hot Chicken",
    price=80,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/84/a8/b9.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/84/a8/bc.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/a4/0f/53.jpg"
),
Booking (
    name="Nashville Honky Tonk Bar Crawl",
    category="Things To Do",
    city="Nashville",
    state="TN",
    lat=36.1641938,
    lng=-86.7786528,
    description="Embark on a Nashville Honky Tonk Bar Crawl for a lively night out. Visit iconic honky-tonk bars, enjoy live country music, and experience the vibrant nightlife of Music City.",
    rating=4.7,
    contact_info="(615) 555-5678",
    website="honkytonkcrawl.com",
    features="Bar Crawl, Live Music, Nashville Nightlife",
    price=45,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/f3/d8/aa.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/a3/1c/ce.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/a3/1c/9c.jpg"
    ),
Booking(
    name="Nashville Grand Ole Opry Show",
    category="Things To Do",
    city="Nashville",
    state="TN",
    lat=36.2068571,
    lng=-86.6921085,
    description="Experience the magic of country music at the Grand Ole Opry. Enjoy a live show featuring top country artists, iconic performances, and the rich history of this legendary venue.",
    rating=4.8,
    contact_info="(615) 555-8765",
    website="grandoleopry.com",
    features="Live Music, Country Artists, Historic Venue",
    price=57.70,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/be/93/08.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/be/94/04.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/e8/3c/d2.jpg"
)
    ]
    for thing in nashville_things:
        db.session.add(thing)

     #seed dc
    dc_restaurants =[
        Booking(
    name="Founding Farmers",
    category="Restaurants",
    city="Washington",
    state="DC",
    lat=38.9002806,
    lng=-77.0444736,
    description="Founding Farmers offers farm-to-table American cuisine with a focus on sustainability. Enjoy a diverse menu featuring locally sourced ingredients and creative dishes.",
    rating=4.5,
    contact_info="(202) 555-1234",
    website="wearefoundingfarmers.com",
    features="Farm-to-Table, Sustainable, American Cuisine",
    price=100,
    opening_hour="11:00 AM",
    closing_hour="10:00 PM",
    image1="https://www.wearefoundingfarmers.com/wp-content/uploads/2020/02/LocationsModule_FFMoco_01.jpg",
    image2="https://www.wearefoundingfarmers.com/wp-content/uploads/2020/07/Menu_Header_01-1200x800.jpg",
    image3="https://dixon.philly.com/wp-content/uploads/2018/03/1083783_d79fe5e054a12a7-1.jpg"
),
Booking(
    name="Le Diplomate",
    category="Restaurants",
    city="Washington",
    state="DC",
    lat=38.911365,
    lng=-77.0316635,
    description="Le Diplomate brings a taste of France to DC with classic French dishes served in a charming brasserie setting. Enjoy expertly crafted cuisine and a delightful ambiance.",
    rating=3.4,
    contact_info="(202) 555-5678",
    website="lediplomatedc.com",
    features="French Cuisine, Brasserie, Charming Atmosphere",
    price=1000,
    opening_hour="9:00 AM",
    closing_hour="11:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-o/05/ec/4a/a9/delicious-hamburger-and.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/03/d5/6c/6e/le-diplomate.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/1c/c0/83/7f/photo0jpg.jpg"
),
Booking(
    name="District Taco",
    category="Restaurants",
    city="Washington",
    state="DC",
    lat=38.8976072,
    lng=-77.0301325,
    description="District Taco serves delicious Mexican street food, including tacos, burritos, and bowls. Enjoy fresh ingredients and a lively atmosphere.",
    rating=3.2,
    contact_info="(202) 555-4321",
    website="districttaco.com",
    features="Mexican Street Food, Lively Atmosphere",
    price=10,
    opening_hour="10:00 AM",
    closing_hour="9:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-p/15/0c/12/f2/district-taco.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-l/14/42/ed/29/20180821-120741-largejpg.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/14/aa/df/f1/photo0jpg.jpg"
),
Booking(
    name="Rose's Luxury",
    category="Restaurants",
    city="Washington",
    state="DC",
    lat=38.8806472,
    lng=-76.995211,
    description="Rose's Luxury offers an eclectic menu of inventive dishes in a relaxed setting. Experience a unique culinary journey with creative flavors and welcoming hospitality.",
    rating=4.0,
    contact_info="(202) 555-8765",
    website="rosesluxury.com",
    features="Inventive Dishes, Eclectic Menu, Relaxed Atmosphere",
    price=1000,
    opening_hour="5:00 PM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/08/d3/6b/b0/rose-s-luxury.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-o/05/78/a8/e6/rose-s-luxury.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-l/1d/4f/72/bc/20210710-180352-largejpg.jpg"
),
Booking(
    name="Old Ebbitt Grill",
    category="Restaurants",
    city="Washington",
    state="DC",
    lat=38.8979475,
    lng=-77.0332478,
    description="Old Ebbitt Grill, located steps from the White House, is a historic American saloon offering classic dishes and a vibrant atmosphere.",
    rating=2.8,
    contact_info="(202) 555-5678",
    website="oldebbitt.com",
    features="Historic Saloon, American Classics",
    price=1000,
    opening_hour="11:00 AM",
    closing_hour="12:00 AM",
    image1="https://upload.wikimedia.org/wikipedia/commons/c/c0/Old_Ebbitt_Grill.jpg",
    image2="https://media.cntraveler.com/photos/5b4e45ef354ed17951b4373c/16:9/w_2560,c_limit/Old-Ebbitt-Grill_Courtesy-Clyde%E2%80%99s-Restaurant-Group_2018_Old-Ebbitt-Grill-Main-Dining-Room,-Ron-Blunt-Photog.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/06/09/b0/2d/old-ebbitt-grill.jpg"
)
    ]
    for restaurant in dc_restaurants:
        db.session.add(restaurant)

    dc_hotels = [
        Booking(
    name="The Watergate Hotel",
    category="Hotel",
    city="Washington",
    state="DC",
    lat=38.8994851,
    lng=-77.0556711,
    description="Experience luxury and history at The Watergate Hotel. Enjoy stylish accommodations, breathtaking views, and world-class amenities.",
    rating=4.5,
    contact_info="(202) 555-1111",
    website="watergatehotel.com",
    features="Luxury Accommodations, Breathtaking Views",
    price=250,
    image1="https://media-cdn.tripadvisor.com/media/photo-s/2a/ac/8f/d7/entrance.jpg",
    image2="https://www.fivestaralliance.com/files/fivestaralliance.com/field/image/nodes/2018/46248/0_terrace-lounge-G.jpg",
    image3="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/e4/1b/a8/indoor-pool.jpg"
),
Booking(
    name="The Hay-Adams",
    category="Hotel",
    city="Washington",
    state="DC",
    lat=38.9004014,
    lng=-77.0369333,
    description="The Hay-Adams offers a historic and luxurious stay near the White House. Enjoy elegant rooms, exceptional service, and stunning views.",
    rating=4.8,
    contact_info="(202) 555-2222",
    website="hayadams.com",
    features="Historic Charm, Luxurious Rooms",
    price=350,
    image1="https://upload.wikimedia.org/wikipedia/commons/d/d4/Hay_Adams_Hotel.jpg",
    image2="https://cf.bstatic.com/xdata/images/hotel/max1024x768/117267550.jpg",
    image3="https://www.oyster.com/wp-content/uploads/sites/35/2019/05/lobby-v11039536-1440-1024x683.jpg"
),
Booking(
    name="The Willard InterContinental",
    category="Hotel",
    city="Washington",
    state="DC",
    lat=38.8968125,
    lng=-77.0322812,
    description="Discover timeless luxury at The Willard InterContinental. Immerse yourself in elegance with well-appointed rooms and exceptional service.",
    rating=4.6,
    contact_info="(202) 555-3333",
    website="washington.intercontinental.com",
    features="Timeless Luxury, Exceptional Service",
    price=300,
    image1="https://media.cntraveler.com/photos/5f62c630b981fb78a3045f16/16:9/w_2560%2Cc_limit/intercontinental-willard-washingtondc-exterior.jpg",
    image2="https://media.cntraveler.com/photos/585aa89edc9583092d3e8781/16:9/w_2560%2Cc_limit/Suite1-InterContinentalTheWillard-WashingtonDC-CRHotel.jpg",
    image3="https://cf.bstatic.com/xdata/images/hotel/max1024x768/375440459.jpg"
),
Booking(
    name="Kimpton Hotel Monaco Washington DC",
    category="Hotel",
    city="Washington",
    state="DC",
    lat=38.8970339,
    lng=-77.022408,
    description="Indulge in the eclectic charm of Kimpton Hotel Monaco. Experience unique design, personalized service, and a central location.",
    rating=4.2,
    contact_info="(202) 555-4444",
    website="monaco-dc.com",
    features="Eclectic Charm, Personalized Service",
    price=180,
    image1="https://www.monaco-dc.com/images/1700-960/kimpton-lobby-60af503b.jpg",
    image2="https://www.monaco-dc.com/images/1700-960/kimpton-hotel-monaco-dc-guestroom-0ffdc061.jpg",
    image3="https://www.kayak.com/rimg/himg/66/ac/e0/leonardo-1272453-PHLPM_7193556804_O-249376.jpg"
),
Booking(
    name="The Line DC",
    category="Hotel",
    city="Washington",
    state="DC",
    lat=38.9227591,
    lng=-77.0416516,
    description="Experience contemporary style and cultural immersion at The Line DC. Discover thoughtfully designed spaces and vibrant local art.",
    rating=4.4,
    contact_info="(202) 555-6666",
    website="thelinehotel.com/dc",
    features="Contemporary Style, Cultural Immersion",
    price=220,
    image1="https://www.chrisferenzi.com/wp-content/uploads/2020/03/Brothers-and-Sisters-Line-Hotel-DC-1024x614.jpg",
    image2="https://washington.org/sites/default/files/dc_import/LINE-Hotel-DC-eXTERIOR-1-_71B7B0CE-19BB-4FE9-9E3A83CF05D33BD1_7847688f-aa8d-437d-bbfb61c55a26793c.jpg",
    image3="https://media.cntraveler.com/photos/5c8f14fc2fd2ea2d63da364b/16:9/w_2560,c_limit/The-LINE_DC_2019_Unknown-3.jpg"
)
    ]

    for hotel in dc_hotels:
        db.session.add(hotel)

    dc_things = [
        Booking(
    name="Small-Group Guided Tour inside US Capitol & Library of Congress",
    category="Things To Do",
    city="Washington",
    state="DC",
    lat=38.8887251,
    lng=-77.0048754,
    description="Discover the rich history and architecture of the US Capitol and Library of Congress with a small-group guided tour. Learn about the nation's legislative process and explore the impressive collections of the Library of Congress.",
    rating=4.8,
    contact_info="(202) 555-1234",
    website="capitoltours.example.com",
    features="Historical Tour, Capitol Building, Library of Congress",
    price=35.00,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/ef/3b/86.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/09/9b/5c/5c.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/ef/39/9a.jpg"
),
Booking(
    name="Washington DC Holiday Light Tour of the National Mall & Memorials",
    category="Things To Do",
    city="Washington",
    state="DC",
    lat=38.8936878,
    lng=-77.0224981,
    description="Experience the magic of the holiday season with a guided light tour of the National Mall and Memorials in Washington DC. Marvel at the beautifully illuminated monuments and learn about the history behind each one.",
    rating=4.5,
    contact_info="(202) 555-5678",
    website="holidaylightsdc.example.com",
    features="Holiday Lights, Guided Tour, National Mall, Memorials",
    price=25.99,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/73/46/37.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/73/46/38.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/09/1a/08/27.jpg"
),
Booking(
    name="Ghosts of Georgetown Night-Time Walking Tour",
    category="Things To Do",
    city="Washington",
    state="DC",
    lat=38.9053915,
    lng=-77.0603792,
    description="Embark on a thrilling night-time walking tour through the historic streets of Georgetown. Discover the eerie tales and haunted history of this enchanting neighborhood as experienced guides share chilling stories of the paranormal.",
    rating=4.2,
    contact_info="(202) 555-6789",
    website="georgetownghosttours.example.com",
    features="Night-Time Tour, Ghost Stories, Historic Georgetown",
    price=35.50,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/73/d4/8d.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/73/eb/0e.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/73/d4/8c.jpg"
),
Booking(
    name="House of Cards Outdoor Escape Game",
    category="Things To Do",
    city="Washington",
    state="DC",
    lat=38.88973,
    lng=-77.01486,
    description="Experience the excitement of an outdoor escape game inspired by House of Cards. Solve puzzles, unravel mysteries, and navigate through the political intrigue of Washington DC. Gather your team and enjoy an immersive adventure in the heart of the nation's capital.",
    rating=4.5,
    contact_info="(202) 555-1234",
    website="houseofcardsescapes.example.com",
    features="Outdoor Adventure, Puzzle Solving, Political Intrigue",
    price=45.99,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0f/27/83/b4.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0f/27/83/9f.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/10/3f/97/4d.jpg"
),
Booking(
    name="International Spy Museum",
    category="Things To Do",
    city="Washington",
    state="DC",
    lat=38.8841419,
    lng=-77.0255748,
    description="Embark on an intriguing journey into the world of espionage at the International Spy Museum, featuring spy artifacts and interactive exhibits.",
    rating=4.7,
    contact_info="(202) 555-3456",
    website="spymuseum.org",
    features="Spy Exhibits, Interactive Displays",
    price=25.75,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/23/f0/a7/new-spy-museum-at-l-enfant.jpg",
    image2="https://spy-museum.s3.amazonaws.com/files/pages/classic-xsml-covert-action-exhibit-at-the-spy-museum-3.jpg",
    image3="https://i0.wp.com/hyperallergic-newspack.s3.amazonaws.com/uploads/2019/09/IMG_2060-t.jpg"
)

    ]

    for thing in dc_things:
        db.session.add(thing)
     # seed vegas

    vegas_restaurants = [
         Booking(
    name="Joël Robuchon",
    category="Restaurants",
    city="Las Vegas",
    state="NV",
    lat=36.1019132,
    lng=-115.1688204,
    description="Indulge in exquisite French cuisine at Joël Robuchon, where culinary artistry meets luxury. Experience a world-class dining atmosphere with meticulously crafted dishes and exceptional service.",
    rating=4.8,
    contact_info="(702) 555-1234",
    website="joelrobuchon.com",
    features="Fine Dining, French Cuisine",
    price=1000,
    opening_hour="6:00 PM",
    closing_hour="10:30 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/1a/af/f3/66/joel-robuchon.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/1a/af/f3/3a/joel-robuchon.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/1a/af/f3/8a/joel-robuchon.jpg"
),
Booking(
    name="Gordon Ramsay Steak",
    category="Restaurants",
    city="Las Vegas",
    state="NV",
    lat=36.1127578,
    lng=-115.1712046,
    description="Savor the bold flavors of steakhouse cuisine at Gordon Ramsay Steak. Enjoy a modern twist on classic dishes in a stylish and vibrant atmosphere, curated by the renowned chef Gordon Ramsay.",
    rating=4.5,
    contact_info="(702) 555-5678",
    website="gordonramsaysteak.com",
    features="Steakhouse, Celebrity Chef",
    price=100,
    opening_hour="5:00 PM",
    closing_hour="11:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/1a/58/88/68/beef-wellington.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/1a/58/67/30/inside-gordon-ramsay.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/1a/58/8a/c2/hamachi-crudo.jpg"
),
Booking(
    name="Mastro's Ocean Club",
    category="Restaurants",
    city="Las Vegas",
    state="NV",
    lat=36.1077666,
    lng=-115.1744648,
    description="Experience the finest in seafood and steaks at Mastro's Ocean Club. Immerse yourself in an elegant dining atmosphere, featuring live music and a menu crafted with the freshest ingredients.",
    rating=3.3,
    contact_info="(702) 555-9876",
    website="mastrosoceanclub.com",
    features="Seafood, Steaks, Live Music",
    price=1000,
    opening_hour="5:30 PM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/16/18/ee/0e/dining-room.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-f/0e/a0/01/73/mastro-s-ocean-club.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/08/fc/8b/26/mastro-s-ocean-club.jpg"
),
Booking(
    name="Bacchanal Buffet",
    category="Restaurants",
    city="Las Vegas",
    state="NV",
    lat=36.1159291,
    lng=-115.1762385,
    description="Delight in an unparalleled buffet experience at Bacchanal Buffet. Explore a vast array of international cuisines, from fresh seafood to decadent desserts, in a vibrant and energetic setting.",
    rating=4.2,
    contact_info="(702) 555-4321",
    website="bacchanalbuffet.com",
    features="Buffet, International Cuisine",
    price=100,
    opening_hour="8:00 AM",
    closing_hour="10:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/1a/cf/e1/38/bacchanal-buffet.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/1d/34/a0/0a/bacchanal-buffet.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-s/02/df/f0/1f/bacchanal-buffet-caesars.jpg"
),
Booking(
    name="Eggslut",
    category="Restaurants",
    city="Las Vegas",
    state="NV",
    lat=36.1099889,
    lng=-115.174303,
    description="Satisfy your breakfast cravings at Eggslut, known for its gourmet egg-centric dishes. Enjoy a casual and trendy dining experience with a menu featuring delicious twists on classic breakfast items.",
    rating=4.0,
    contact_info="(702) 555-8765",
    website="eggslut.com",
    features="Breakfast, Gourmet Eggs",
    price=10,
    opening_hour="7:00 AM",
    closing_hour="3:00 PM",
    image1="https://media-cdn.tripadvisor.com/media/photo-s/11/84/5e/b5/eggslut-is-inspired-by.jpg",
    image2="https://media-cdn.tripadvisor.com/media/photo-s/11/84/5e/82/slut-cage-free-coddled.jpg",
    image3="https://media-cdn.tripadvisor.com/media/photo-f/11/84/5e/a6/salted-chocolate-chip.jpg"
)

     ]
    for restaurant in vegas_restaurants:
        db.session.add(restaurant)

    vegas_hotels = [
        Booking(
    name="The Venetian Resort",
    category="Hotel",
    city="Las Vegas",
    state="NV",
    lat=36.121174,
    lng=-115.1696526,
    description="Experience luxury at The Venetian Resort, offering spacious suites, world-class dining, and a replica of Venice's Grand Canal. Immerse yourself in elegance and enjoy a memorable stay on the Las Vegas Strip.",
    rating=4.7,
    contact_info="(702) 555-1111",
    website="venetian.com",
    features="Spa, Pool, Fine Dining",
    price=1000,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/16/8e/c3/f8/vous-cherchez-des-infos.jpg",
    image2="https://ewscripps.brightspotcdn.com/dims4/default/37261d5/2147483647/strip/true/crop/6701x3769+0+349/resize/1280x720!/quality/90/?url=http%3A%2F%2Fewscripps-brightspot.s3.amazonaws.com%2F8b%2F6d%2Fec13f6e640e1b81140373ec2f38d%2Fthe-venetian-resort-pool-east.jpg",
    image3="https://begasvaby.com/wp-content/uploads/2022/07/Venetian-Las-Vegas-hotels.jpg"
),
Booking(
    name="Wynn Las Vegas",
    category="Hotel",
    city="Las Vegas",
    state="NV",
    lat=36.126119,
    lng=-115.1619583,
    description="Discover opulence at Wynn Las Vegas, where luxury meets sophistication. Indulge in spacious rooms, upscale dining, and entertainment, creating an unforgettable experience in the heart of the Strip.",
    rating=4.6,
    contact_info="(702) 555-2222",
    website="wynnlasvegas.com",
    features="Golf Course, Spa, Nightlife",
    price=778,
    image1="https://assets.simpleviewcms.com/simpleview/image/fetch/c_fill,f_jpg,h_475,q_65,w_640/https://lasvegas.simpleviewcrm.com/images/listings/original_Wynn_Encore_1.jpg",
    image2="https://www.onthestrip.com/wp-content/uploads/2021/09/wynn-las-vegas-on-the-strip-pool.jpg",
    image3="https://cimg3.ibsrv.net/cimg/www.fodors.com/2000x2000_60/931/5abae03409299-355931.jpg"
),
Booking(
    name="Bellagio Hotel and Casino",
    category="Hotel",
    city="Las Vegas",
    state="NV",
    lat=36.1129455,
    lng=-115.1765067,
    description="Immerse yourself in the iconic Bellagio experience, known for its stunning fountains and luxurious accommodations. Enjoy world-class amenities, upscale dining, and entertainment in the heart of the Strip.",
    rating=4.5,
    contact_info="(702) 555-3333",
    website="bellagio.com",
    features="Fountains, Casino, Fine Dining",
    price=450,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/8a/e0/b9/bellagio-las-vegas.jpg",
    image2="https://www.travelandleisure.com/thmb/S1K-V4TjWureMrMByWYcOPtt4SY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/TAL-bellagio-las-vegas-penthouse-bedroom-render-NEWBELLAGIO0323-ca8fb3524fef4ed18006d15ba6d935c2.jpg",
    image3="https://bellagio.my-vegashotels.com/data/Images/OriginalPhoto/11871/1187164/1187164582/las-vegas-bellagio-hotel-image-18.JPEG"
),
Booking(
    name="MGM Grand Hotel & Casino",
    category="Hotel",
    city="Las Vegas",
    state="NV",
    lat=36.1036224,
    lng=-115.167574,
    description="Experience the grandeur of MGM Grand Hotel & Casino, a world-renowned resort offering entertainment, dining, and nightlife. Stay in style and enjoy the vibrant atmosphere of the Las Vegas Strip.",
    rating=3.4,
    contact_info="(702) 555-4444",
    website="mgmgrand.com",
    features="Casino, Shows, Nightclub",
    price=329,
    image1="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/0e/e1/1b/mgm-grand-exterior-evening.jpg",
    image2="https://www.oyster.com/wp-content/uploads/sites/35/2019/05/grand-king-v1974050-73-1440-1024x683.jpg",
    image3="https://i.ytimg.com/vi/uW9CmT_Zzc0/maxresdefault.jpg"
),
Booking(
    name="Caesars Palace",
    category="Hotel",
    city="Las Vegas",
    state="NV",
    lat=36.1172612,
    lng=-115.176141,
    description="Step into luxury at Caesars Palace, an iconic resort with Roman-inspired architecture. Indulge in world-class amenities, fine dining, and entertainment for an unforgettable stay on the Strip.",
    rating=4.7,
    contact_info="(702) 555-5555",
    website="caesars.com",
    features="Spa, Pool, Forum Shops",
    price=785,
    image1="https://travelnevada.com/wp-content/uploads/2020/10/Caesars_Featured-scaled.jpg",
    image2="https://media.cntraveler.com/photos/5f625bb1978ff785b25015af/16:9/w_2560,c_limit/caesars-palace-las-vegas-lobby.jpg",
    image3="https://www.colorkinetics.com/content/dam/color-kinetics/showcases/caesars-palace-forum-shops/caesars-palace-forum-shops1_lg.jpg"
)
    ]

    for hotel in vegas_hotels:
        db.session.add(hotel)

    vegas_things = [
        Booking(
    name="Happy Half Hour on The High Roller at The LINQ",
    category="Things To Do",
    city="Las Vegas",
    state="NV",
    lat=36.1181537,
    lng=-115.1724421,
    description="Soar above the Las Vegas Strip on the High Roller Observation Wheel, the world's tallest observation wheel. Enjoy breathtaking views of the city and surrounding landscapes from spacious cabins.",
    rating=4.6,
    contact_info="(702) 555-7777",
    website="highroller.com",
    features="Panoramic Views, Cabins with Bars",
    price=73.72,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/6f/f2/0e.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0a/ee/06/77.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/6e/c7/b0.jpg"
),
Booking(
    name="Cirque du Soleil - O",
    category="Things To Do",
    city="Las Vegas",
    state="NV",
    lat=36.1137192,
    lng=-115.1767906,
    description="Experience the mesmerizing aquatic-themed show 'O' by Cirque du Soleil. Marvel at breathtaking performances, synchronized swimming, and acrobatics in a visually stunning production.",
    rating=4.8,
    contact_info="(702) 555-8888",
    website="cirquedusoleil.com",
    features="Aquatic Acrobatics, Theatrical Spectacle",
    price=179.50,
    image1="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/06/6e/cf/d7.jpg",
    image2="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/07/71/7b/23.jpg",
    image3="https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0e/7f/af/8b.jpg"
),
Booking(
    name="The Mob Museum",
    category="Things To Do",
    city="Las Vegas",
    state="NV",
    lat=36.1728198,
    lng=-115.1412395,
    description="Explore the fascinating history of organized crime at The Mob Museum. Discover interactive exhibits, artifacts, and immersive experiences that showcase the impact of the mob on Las Vegas and beyond.",
    rating=4.4,
    contact_info="(702) 555-9999",
    website="themobmuseum.org",
    features="Interactive Exhibits, Crime History",
    price=26.95,
    image1="https://themobmuseum.org/wp-content/uploads/2022/10/Homepage_7.jpg",
    image2="https://www.unlv.edu/sites/default/files/styles/1200_width/public/articles/main-images/960_Made-Men.jpg?itok=QKhTF3GW",
    image3="https://travelnevada.com/wp-content/uploads/2017/07/MobMuseum_Featured-scaled.jpg"
)
    ]

    for thing in vegas_things:
        db.session.add(thing)
    db.session.commit()

def undo_bookings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bookings"))
    db.session.commit()

def undo_itineraries():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.itineraries RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM itineraries"))

    db.session.commit()
