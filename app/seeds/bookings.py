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

    db.session.commit()

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
