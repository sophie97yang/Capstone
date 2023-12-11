import { useDispatch,useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import {getBookings} from '../../store/booking';
import { useEffect,useState } from "react";
import './Explore.css'
// import OpenModalButton from "../OpenModalButton";
// import { useEffect } from "react";
// import { getHotels } from "../../store/booking";
import {Link} from 'react-router-dom';
function Explore () {
    const dispatch = useDispatch();
    const {city} = useParams();
    const bookings = useSelector(state=>state.bookings.bookings)
    const bookings_city = Object.values(bookings).filter(booking => booking.city===city)
    const [filter,setFiltered] = useState('All')
    const [bookingsFilter,setBookings]=useState(bookings_city)
    console.log(bookings_city)

    useEffect(()=> {
        dispatch(getBookings())
    },[dispatch])

    useEffect(()=> {
        if (filter!=='All') {
        const bookings = bookings_city.filter(booking=>booking.category===filter)
        setBookings(bookings)
        } else {
            setBookings(bookings_city)
        }
    },[filter])

    const locations = [{city:'Aspen',state:'CO',image:"https://www.travelandleisure.com/thmb/Yiq3rXHGmHnDrgzBsGmEvqjHxSo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/aspen-colorado-lead-ASPENTG0122-3bd432152d1f4758b1b89fd8a3a231cc.jpg"},
    {city:'Miami',state:'FL',image:'https://www.mayflower.com/wp-content/uploads/2022/05/Miami-City-Guide_Header-scaled.jpg'},
    {city:'Napa',state:'CA',image:"https://falstaff.b-cdn.net/core/5039223/napa-valley_5039223.jpg"},
    {city:'Boston',state:'MA',image:"https://content.r9cdn.net/rimg/dimg/8d/d4/5837febe-city-25588-16b90081d43.jpg"},
    {city:'Moab',state:'UT',image:"https://www.visittheusa.com/sites/default/files/styles/hero_l/public/images/hero_media_image/2017-07/92ce662af277a11b73ea3a6d451271fc.jpeg"},
    {city:'Jackson',state:'WY',image:"https://assets.vogue.com/photos/61d453c3069d2a61c3d376e1/master/w_2560%2Cc_limit/520395534"},
    {city:'Nashville',state:'TN',image:"https://i.natgeofe.com/n/070fbe2c-a644-4c62-aa76-bddf63dd6f10/broadway-record-shop-nashville-tennessee.jpg"},
    {city:'Savannah',state:'GA',image:"https://ballastone.com/wp-content/uploads/2019/04/best-time-to-travel-to-savannah-ga-1.jpg"},
    {city:'Charleston',state:'SC',image:"https://www.fodors.com/wp-content/uploads/2022/09/HERO-shutterstock_1577091133.jpg"},
    {city:'Sedona',state:'AZ',image:"https://visit-sedona.s3.amazonaws.com/CMS/2214/view_from_airport_mesa_at_sunrise__medium.jpg"},
    {city:'Washington',state:'DC',image:"https://www.thoughtco.com/thmb/_ZNhs9lhwfoos1WoYBygoL03g6c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-497322993-598b2ad403f4020010ae0a08.jpg"},
    {city:'New Orleans',state:'LA',image:"https://media.timeout.com/images/105770969/750/562/image.jpg"},
    {city:'Chicago',state:'IL',image:"https://cdn.choosechicago.com/uploads/2022/06/wygyk-agnostic-A.Alexander_5cloudgateMay13-scaled.jpg"},
    {city:'Orlando',state:'FL',image:"https://a.cdn-hotels.com/gdcs/production4/d842/1da7b753-73d3-4f87-9661-13fc8b819242.jpg"},
    {city:'Las Vegas',state:'NV',image:"https://media.cnn.com/api/v1/images/stellar/prod/180313182911-01-las-vegas-travel-strip.jpg"},
    {city:'Oahu',state:'HI',image:"https://i.insider.com/62867ef1577b8a001827a029?width=1136&format=jpeg"},
    {city:'Maui',state:'HI',image:"https://a.cdn-hotels.com/gdcs/production81/d1269/0cffe15a-7fdf-4e75-9415-92eaf78e2f73.jpg"},
    {city:'New York City',state:'NY',image:"https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"}
    ]

    const location_picture = locations.filter(locationObj => locationObj.city===city)[0]


    return (
        <div className='explore'>
        <h3 className='breadcrumb-container'><Link to='/' className='breadcrumb'>Home </Link> {`  >`} Explore {city}</h3>
        <h2>Hello from {city}!</h2>
        {bookingsFilter.length ?
            <>
        <div className='filter-buttons'>
            <button className={filter==='All'? "filter-button selected" : "filter-button"} onClick={(e)=> {
                setFiltered('All');
            }}>All</button>
            <button className={filter==='Hotels'? "filter-button selected" : "filter-button"} onClick={(e)=> {
                setFiltered('Hotel')
            }}>Hotels</button>
            <button className={filter==='Things To Do'? "filter-button selected" : "filter-button"} onClick={(e)=> {
                setFiltered('Things To Do')
            }}>Things To Do</button>
            <button className={filter==='Restaurants'? "filter-button selected" : "filter-button"} onClick={(e)=> {
                setFiltered('Restaurants')
            }}>Restaurants</button>
        </div>

        <div>
            {bookingsFilter.map((booking)=> (
                <div key={booking.id} className='booking-places'>
                    <h3>{booking.name}</h3>
                    <h4>{booking.category}</h4>
                    {booking.category==='Hotel' && <h4>Price per night: ${booking.price.toFixed(2)}</h4>}
                    {booking.category==='Things To Do' && <h4>Price per person: ${booking.price.toFixed(2)}</h4>}
                    {booking.category==='Restaurants' && <h4>{booking.price===1000 ? '$$$' : <span>{booking.price===100 ? "$$": "$"}</span>}</h4>}
                    <div className='explore-images'>
                    <img src={booking.image1} alt={booking.name}></img>
                    <img src={booking.image2} alt={booking.name}></img>
                    <img src={booking.image3} alt={booking.name}></img>
                    {/* <OpenModalButton buttonText="Add to your Trip's Itinerary"/> */}
                    </div>

                </div>
            ))}
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
