import { useDispatch,useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import {getBookings} from '../../store/booking';
import { useEffect,useState } from "react";
import './Explore.css'
import OpenModalButton from "../OpenModalButton";
// import { useEffect } from "react";
// import { getHotels } from "../../store/booking";
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


    return (
        <div>
        <h2>Hello from {city}!</h2>
        <div>
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
                <div key={booking.id}>
                    <h3>{booking.name}</h3>
                    <h4>{booking.category}</h4>
                    {booking.category==='Hotel' && <h4>Price per night: ${booking.price.toFixed(2)}</h4>}
                    {booking.category==='Things To Do' && <h4>Price per person: ${booking.price.toFixed(2)}</h4>}
                    {booking.category==='Restaurants' && <h4>{booking.price===1000 ? '$$$' : <span>{booking.price===100 ? "$$": "$"}</span>}</h4>}
                    <div className='explore-images'>
                    <img src={booking.image1} alt={booking.name}></img>
                    <img src={booking.image2} alt={booking.name}></img>
                    <img src={booking.image3} alt={booking.name}></img>
                    <OpenModalButton buttonText="Add to your Trip's Itinerary"/>
                    </div>

                </div>
            ))}
        </div>
        </div>
    )
}
export default Explore;
