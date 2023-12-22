import { useDispatch,useSelector } from "react-redux";
import { useParams,Link } from "react-router-dom";
import {getBookings} from '../../store/booking';
import { useEffect,useState } from "react";
import './Explore.css'
import OpenModalButton from "../OpenModalButton";
// import { useEffect } from "react";
// import { getHotels } from "../../store/booking";
import CreateTripShortcut from "../CreateTripForm/CreateTripShortcut";
import AddToItinerary from "../AddToItinerary";
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";

function Explore () {
    const dispatch = useDispatch();
    const {city} = useParams();
    const bookings = useSelector(state=>state.bookings.bookings);
    const user = useSelector(state=>state.session.user);
    const bookings_city = Object.values(bookings).filter(booking => booking.city===city);

    bookings_city.forEach(booking=> {
        let stars=''
        for (let i=0;i<Math.round(booking.rating);i++) {
            stars+='🟢'
        }
        booking.stars=stars;
    })

    const bookings_city_hotels = bookings_city.filter(booking=> booking.category==='Hotel');
    const bookings_city_restaurants = bookings_city.filter(booking=> booking.category==='Restaurants');
    const bookings_city_things = bookings_city.filter(booking=> booking.category==='Things To Do');

    const [filter,setFiltered] = useState('All')
    const [bookingsFilter,setBookings]=useState(bookings_city);

    useEffect(()=> {
        dispatch(getBookings())
    },[dispatch])

    useEffect(()=> {
        if (filter!=='All') {
            if (filter==='Hotel' && (bookingsFilter.length!==bookings_city_hotels.length || bookingsFilter[0].name!==bookings_city_hotels[0].name)) setBookings(bookings_city_hotels);
            else if (filter==='Restaurants' && (bookingsFilter.length!==bookings_city_restaurants.length || bookingsFilter[0].name!==bookings_city_restaurants[0].name)) setBookings(bookings_city_restaurants);
            else if (filter==='Things To Do' && (bookingsFilter.length!==bookings_city_things.length || bookingsFilter[0].name!==bookings_city_things[0].name)) setBookings(bookings_city_things);
        } else {
            if (bookingsFilter.length!==bookings_city.length){
            setBookings(bookings_city)
            }
        }
    },[filter,bookings_city,bookings_city_hotels,bookings_city_restaurants,bookings_city_things])

    const locations = [{city:'Aspen',state:'CO',image:"https://www.travelandleisure.com/thmb/Yiq3rXHGmHnDrgzBsGmEvqjHxSo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/aspen-colorado-lead-ASPENTG0122-3bd432152d1f4758b1b89fd8a3a231cc.jpg", header:"About Aspen",about:"Everyone knows Aspen as a top-notch winter resort town. But outdoor enthusiasts will enjoy it in the summer, too, when the mountains become a perfect setting for hiking, biking and horseback tours. Some may be surprised to find it’s a top romance destination—but after all that outdoor exercise, who wouldn’t want to repair to a luxurious hotel room or a cozy, firelit bar?"},
    {city:'Miami',state:'FL',image:'https://www.mayflower.com/wp-content/uploads/2022/05/Miami-City-Guide_Header-scaled.jpg',header:"About Miami",about:"Miami at night is legendary—it’s all art-deco neon, music spilling into the streets and rooftop cocktails. But by day, there’s just as much to explore. Architecture buffs can visit the reconstructed 12th century Ancient Spanish Monastery and Renaissance-inspired Vizcaya Museum & Gardens, or cruise down the art deco-dotted Ocean Drive. For beach lovers, there’s plenty beyond South Beach: Swim with sea turtles at Boynton Beach, go windsurfing at Hobie Beach, or skip the sand and take a dip at the Venetian Pool (another architectural gem). And thanks to the strong Cuban and Jewish communities, you can snack on pastelitos in Little Havana or grab a loaf of kosher rye in Wynwood—in the same day, if you’re up for it."},
    {city:'Napa',state:'CA',image:"https://falstaff.b-cdn.net/core/5039223/napa-valley_5039223.jpg",header:"The valley's namesake city is a destination unto itself",about:"Gold and silver may have inspired the crowds that flocked to Napa in the 1800s, but liquid gold—Chardonnays, Cabernet Sauvignons and Pinot Noirs—fuels the modern migration. With an abundance of fine restaurants and inns, Napa has become a dream destination for wine-lovers. And this thriving, creative city has come into its own as a can't-miss stop on any wine-country vacation."},
    {city:'Boston',state:'MA',image:"https://content.r9cdn.net/rimg/dimg/8d/d4/5837febe-city-25588-16b90081d43.jpg",header:"About Boston",about:"In Boston, you can bump into American history any time you step out the door. Walk the city’s brick-lined Freedom Trail to see historic sites that teleport you back to the Revolutionary War. But Boston is hardly frozen in the past. Every neighborhood has its own vibrant, thriving scene. Spend an afternoon in the North End, taste-testing cannoli from Italian-American bakeries. Or people-watch from a bench in Boston Common, which locals treat as an extension of their living room. It’s worth taking the T out to neighboring Cambridge or Sommerville, especially during charming local festivals like What the Fluff, a festival dedicated to—what else?—marshmallow fluff. Another outing that’s a real classic—Fenway Park. Watching a Red Sox game from the bleachers is a Boston rite of passage."},
    {city:'Moab',state:'UT',image:"https://www.visittheusa.com/sites/default/files/styles/hero_l/public/images/hero_media_image/2017-07/92ce662af277a11b73ea3a6d451271fc.jpeg",about:"With its glowing red rocks and arches, surreal craters and mesas, tiny Moab has serious desert chops (not to mention some of the most incredible sunsets we’ve ever seen). It’s no wonder the town is a go-to destination for outdoor adventurers with tons of mountain biking, rock climbing, rafting, and hiking, especially in Arches National Park. But when you’re ready to take the activity level down a notch, there’s plenty else to do: shop for artisan wares on Main Street, check out the region’s cinematic history at the Film Museum at Red Cliffs Ranch, indulge in a decadent massage or energy healing session, or just kick back by the pool and take in the views."},
    {city:'Jackson',state:'WY',image:"https://assets.vogue.com/photos/61d453c3069d2a61c3d376e1/master/w_2560%2Cc_limit/520395534",header:"A Western mountain town that's catnip to serious skiers and big spenders",about:"Jackson, the namesake town in the valley known as Jackson Hole, is the beating heart of this famous destination's upscale rustic scene. Western mountain town chic meets serious outdoor offerings: In the winter, skiing (regular, cross-country, snowcat, and heli-), takes center stage; while in summer, there’s plenty of hiking, fly-fishing, rafting, biking, and hot-air ballooning."},
    {city:'Nashville',state:'TN',image:"https://i.natgeofe.com/n/070fbe2c-a644-4c62-aa76-bddf63dd6f10/broadway-record-shop-nashville-tennessee.jpg",about:"Music is the heartbeat of Nashville. From up-and-coming bands jamming in honky tonks on Lower Broadway to legends rocking the Grand Ole Opry, it’s everywhere, providing a non-stop, rollicking soundtrack. And while music often takes center stage, the city’s also home to a dynamic food scene—no trip would be complete without a stop at Hattie B’s for some hot chicken—gorgeous green spaces like Centennial Park, and art galleries galore. So yes, come to Nashville for the music, but stay for everything else. Its creative spirit is sure to inspire you"},
    {city:'Washington',state:'DC',image:"https://www.thoughtco.com/thmb/_ZNhs9lhwfoos1WoYBygoL03g6c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-497322993-598b2ad403f4020010ae0a08.jpg",about:"Washington, D.C.’s rep is spot on: For history and politics, you can’t get any closer to the action. But what you might not know is its softer side. The city has over 600 parks, and in the spring, you can see the National Mall all decked out in its famous cherry blossoms. Or, stroll through Georgetown—D.C.’s oldest neighborhood—to find cool shops and restaurants alongside buildings from the 1700s. And while you definitely shouldn’t miss the major monuments and Smithsonian museums, there are plenty of lesser-known landmarks, too. Check out Hillwood Estate (go for the Russian and French art, stay for the 13-acre garden), and the Municipal Fish Market—it’s the oldest in the U.S. and it’s got killer crab cakes. We’ve got more recs where this came from, below."},
    {city:'Las Vegas',state:'NV',image:"https://media.cnn.com/api/v1/images/stellar/prod/180313182911-01-las-vegas-travel-strip.jpg",about:"Whatever you can dream up, Las Vegas delivers: Michelin-starred restaurants, 24-hour wedding chapels, larger-than-life scenery, slot machines, all of it. But just when you think you have Vegas pinned down, it surprises you. Consider Meow Wolf, an immersive experience that’s equal parts theme park and art gallery. Or the ice rink at the Cosmopolitan (winter in the desert!). And then there’s the nature—head out past the Strip, and you’ll find state parks and views for days in spots like Valley of Fire and Red Rock Canyon. It’s gems like these that round out Vegas as a destination for families and non-partiers too."},
    {city:'Savannah',state:'GA',image:"https://ballastone.com/wp-content/uploads/2019/04/best-time-to-travel-to-savannah-ga-1.jpg"},
    {city:'Charleston',state:'SC',image:"https://www.fodors.com/wp-content/uploads/2022/09/HERO-shutterstock_1577091133.jpg"},
    {city:'Sedona',state:'AZ',image:"https://visit-sedona.s3.amazonaws.com/CMS/2214/view_from_airport_mesa_at_sunrise__medium.jpg"},
    {city:'New Orleans',state:'LA',image:"https://media.timeout.com/images/105770969/750/562/image.jpg"},
    {city:'Chicago',state:'IL',image:"https://cdn.choosechicago.com/uploads/2022/06/wygyk-agnostic-A.Alexander_5cloudgateMay13-scaled.jpg"},
    {city:'Orlando',state:'FL',image:"https://a.cdn-hotels.com/gdcs/production4/d842/1da7b753-73d3-4f87-9661-13fc8b819242.jpg"},
    {city:'Oahu',state:'HI',image:"https://i.insider.com/62867ef1577b8a001827a029?width=1136&format=jpeg"},
    {city:'Maui',state:'HI',image:"https://a.cdn-hotels.com/gdcs/production81/d1269/0cffe15a-7fdf-4e75-9415-92eaf78e2f73.jpg"},
    {city:'New York City',state:'NY',image:"https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"}
    ]

    const location_picture = locations.filter(locationObj => locationObj.city===city)[0]

    const renderRightArrow = (onClickHandler, hasNext, label) => hasNext && (
        <button type="button" onClick={onClickHandler} title={label} className='carousel-buttons button-right'>
            <i className="fa-solid fa-arrow-right fa-xl"></i>
        </button>
    )

    const renderLeftArrow = (onClickHandler, hasPrev, label) => hasPrev && (
    <button type="button" onClick={onClickHandler} title={label} className='carousel-buttons button-left'>
        <i className="fa-solid fa-arrow-left fa-xl"></i>
    </button>
)
    return (
        <div className='explore'>
        <h3 className='breadcrumb-container'><Link to='/' className='breadcrumb'>Home </Link> {`  >`} Explore {city}</h3>
        <h2><span className='explore-word'>Explore </span>{city}</h2>
        {bookingsFilter.length ?
            <>
        <div className='filter-buttons'>
            <button className={filter==='All'? "filter-button selected-button" : "filter-button"} onClick={(e)=> {
                setFiltered('All');
            }}>All</button>
            <button className={filter==='Hotel'? "filter-button selected-button" : "filter-button"} onClick={(e)=> {
                setFiltered('Hotel')
            }}>Hotels <i className="fa-solid fa-bed"></i></button>
            <button className={filter==='Things To Do'? "filter-button selected-button" : "filter-button"} onClick={(e)=> {
                setFiltered('Things To Do')
            }}>Things To Do <i className="fa-solid fa-ticket"></i></button>
            <button className={filter==='Restaurants'? "filter-button selected-button" : "filter-button"} onClick={(e)=> {
                setFiltered('Restaurants')
            }}>Restaurants <i className="fa-solid fa-utensils"></i></button>
        </div>

        <div className='about-city'>
        <img src={location_picture.image} alt={city}></img>
        <h3>{location_picture.header}</h3>
        <p>{location_picture.about}</p>
        </div>

        {user &&
        <div className='plan-trip'>
            <h2>Plan your trip to {city} </h2>
            <CreateTripShortcut city={city} state={location_picture.state}/>

        </div>}

        <div className='explore-bookings'>
            <h2>Essential {city}</h2>
            <p> {filter!=='All' ?
            <span>{filter==='Hotel' ?
             <>
             A mix of the charming, iconic, and modern.
             </>
            : <>
            {
                filter==='Things To Do' ?
            <>
            Places to see, ways to wander, and signature experiences that define {city}.
            </>:
            <>
            Quintessential {city} bistros, bars, and beyond.
            </>
            }
            </>}</span> :""
            }</p>

            {
                filter==='All' ?
                <>
                <div className="explore-hotels">
                <div className='about-explore-section'>
                <h2>Stay</h2>
                <p>A mix of the charming, iconic, and modern.</p>
                </div>
                <Carousel className='bookings-carousel' showThumbs={false} centerMode={true}
                centerSlidePercentage={50} showIndicators={false}
                showStatus={false}
                renderArrowNext={renderRightArrow} renderArrowPrev={renderLeftArrow}
                >
                {bookings_city_hotels.map((booking)=> (
                <div key={booking.id} className='booking-places'>
                    <div className='explore-images'>
                        <img src={booking.image1} alt={booking.name}></img>
                    {user ?  <i className="fa-regular fa-heart fa-xl"></i>:<></>}
                    {user ?
                        <OpenModalButton
                        buttonText={`Add to Trip`}
                        modalComponent={<AddToItinerary booking={booking}/>}
                        />
                        :<></>
                    }
                    </div>
                    <h3><Link to={`/bookings/${booking.id}`}>{booking.name}</Link></h3>
                    <h3>{booking.stars}</h3>
                    <h4>{booking.features}</h4>
                    <h4>from ${booking.price.toFixed(2)}/night</h4>
                </div>
                ))}
                </Carousel>
                </div>

                <div className="explore-things">
                <div className='about-explore-section'>
                <h2>Do</h2>
                <p>Places to see, ways to wander, and signature experiences that define {city}.</p>
                </div>
                <Carousel className='bookings-carousel' showThumbs={false} centerMode={true}
                centerSlidePercentage={50} showIndicators={false}
                showStatus={false}
                renderArrowNext={renderRightArrow} renderArrowPrev={renderLeftArrow}
                >
                {bookings_city_things.map((booking)=> (
                <div key={booking.id} className='booking-places'>
                    <div className='explore-images'>
                        <img src={booking.image1} alt={booking.name}></img>
                        {user ?  <i className="fa-regular fa-heart fa-xl"></i>:<></>}
                        {user ?
                        <OpenModalButton
                        buttonText={`  Add to Trip`}
                        modalComponent={<AddToItinerary booking={booking}/>}
                        />
                        :<></>
                    }
                    </div>
                    <h3><Link to={`/bookings/${booking.id}`}>{booking.name}</Link></h3>
                    <h3>{booking.stars}</h3>
                    <h4>{booking.features}</h4>
                    <h4>from ${booking.price.toFixed(2)}/person</h4>
                </div>
                ))}
                </Carousel>
                </div>

                <div className="explore-restaurants">
                <div className='about-explore-section'>
                <h2>Eat</h2>
                <p>Quintessential {city} bistros, bars, and beyond.</p>
                </div>
                <Carousel className='bookings-carousel' showThumbs={false} centerMode={true}
                centerSlidePercentage={50} showIndicators={false}
                showStatus={false}
                renderArrowNext={renderRightArrow} renderArrowPrev={renderLeftArrow}
                >
                {bookings_city_restaurants.map((booking)=> (
                <div key={booking.id} className='booking-places'>
                    <div className='explore-images'>
                        <img src={booking.image1} alt={booking.name}></img>
                        {user ?  <i className="fa-regular fa-heart fa-xl"></i>:<></>}
                        {user ?
                        <OpenModalButton
                        buttonText={`Add to Trip`}
                        modalComponent={<AddToItinerary booking={booking}/>}
                        />
                        :<></>
                    }
                    </div>
                    <h3><Link to={`/bookings/${booking.id}`}>{booking.name}</Link></h3>
                    <h3>{booking.stars}</h3>
                    <h4>{booking.price===1000 ? '$$$' : <span>{booking.price===100 ? "$$": "$"}</span>}  •  {booking.features}</h4>
                </div>
                ))}
                 </Carousel>
                </div>

                </>:
            <>
            {bookingsFilter.map((booking)=> (
                <div key={booking.id} className='booking-places'>
                    <h3>{booking.name}</h3>
                    <h3>{booking.stars}</h3>
                    {booking.category==='Hotel' && <h4>from ${booking.price.toFixed(2)}/night</h4>}
                    {booking.category==='Things To Do' && <h4>Price per person: ${booking.price.toFixed(2)}</h4>}
                    {booking.category==='Restaurants' && <h4>{booking.price===1000 ? '$$$' : <span>{booking.price===100 ? "$$": "$"}</span>}</h4>}
                    <div className='explore-images'>
                    <img src={booking.image1} alt={booking.name}></img>
                    {/* <img src={booking.image2} alt={booking.name}></img>
                    <img src={booking.image3} alt={booking.name}></img> */}
                    </div>
                </div>
            ))}
            </>
        }
        </div>
        </>:


        <div className='coming-soon'>
            <img src={location_picture.image} alt={location_picture.city}></img>
            <h2>Exciting Developments Underway: Unveiling Soon!
                Get Ready to Embark on a Journey Through Our Latest Travel Destination in the Making.
            </h2>
        </div>
}
        </div>
    )
}
export default Explore;
