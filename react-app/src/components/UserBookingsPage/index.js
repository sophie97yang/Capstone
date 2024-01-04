import {useEffect, useState} from 'react';
import { useSelector } from "react-redux";
import { useHistory,Link } from "react-router-dom";
import OpenModalButton from '../OpenModalButton';
import AddExpenseFromItinerary from "../TripDetailsPage/AddExpenseFromItinerary";
import './UserBookings.css';
function UserBookings() {
    const user = useSelector(state=>state.session.user);
    const history=useHistory();
    const trips = user.trips;
    let bookings=[];
    Object.entries(trips).forEach(([tripId,trip])=> {
        // console.log(trip.trip.bookings_itinerary)
        trip.trip.bookings_itinerary?.forEach(booking=>{
            bookings.push({trip,tripId,booking})
        })

        bookings = bookings.sort((obj1,obj2)=> {
            return new Date(obj1.booking.booking_startdate)-new Date(obj2.booking.booking_startdate);
        })
    })

    const options={}
    options.timeZone = "UTC";

    return (
        <div className='user-bookings'>
             <h3 className='breadcrumb-container'><Link to='/' className='breadcrumb'>Home </Link> {`  >`} Your Bookings</h3>
             {bookings?.map(({trip,tripId,booking})=>(
                <div className={`individual-booking ${new Date(booking.booking_enddate)<new Date() ? 'past':'current'}`} key={booking.id}>
                    <img src={booking.booking.image1} alt={booking.booking.name}
                    onError={e => { e.currentTarget.src = "https://i.pinimg.com/736x/be/c1/69/bec169e6963d7ffe14f10c641af31141.jpg"}}
                    />
                    <div>
                        <h3><Link to={`/bookings/${booking.booking.id}`}>{booking.booking.name}</Link></h3>
                       {booking.booking.category==='Hotel' ?
                       <p><i className="fa-solid fa-calendar-day"/>{new Date(booking.booking_startdate).toLocaleDateString('en-US',options)} - {new Date(booking.booking_enddate).toLocaleDateString('en-US',options)}</p>:
                       <p><i className="fa-solid fa-calendar-day"/>{new Date(booking.booking_startdate).toLocaleDateString('en-US',options)} at {booking.booking_time}</p>
                    }
                    {
                        booking.booking.category==='Hotel' ?
                        <p><i className="fa-solid fa-bed"/> {booking.people} {booking.people===1 ?"Room":"Rooms"}</p>:
                        <p><i className="fa-solid fa-users"/>{booking.people} people</p>
                    }
                    <p><i className="fa-solid fa-location-dot"/> {booking.booking.city}, {booking.booking.state}</p>
                    <p><i className="fa-solid fa-suitcase"/> <Link to={`/trips/${trip.trip.id}/itineraries`}>{trip.trip.name}</Link></p>
                    {
                        booking.booking.category==='Restaurants' ?
                        "":
                        <p><i className="fa-regular fa-credit-card"/>${booking.total.toFixed(2)}</p>
                    }
                    {!booking.expensed ? <OpenModalButton
                                           buttonText="Add Expense"
                                           className='add-expense-button'
                                           modalComponent={<AddExpenseFromItinerary trip={trip} booking={booking}/>}
                                           />: <button onClick={(e)=> {
                                            e.preventDefault();
                                            history.push(`/trips/${tripId}/expenses/${booking.expense_id}`)
                                           }}
                                           className="view-expense-button"
                                           >View Expense</button>}
                    </div>
                </div>
             ))}
             {!bookings.length &&
             <div className='no-bookings'>
            <p>
                Ready to turn your trip into an unforgettable experience? Explore a world of possibilities by discovering and
                booking unique hotels, delightful restaurants, and exciting things to do. Your personalized adventure is just a click away.
            </p>
            <button onClick={(e)=> {
                    e.preventDefault();
                    history.push(`/trips/all`)
                }}>Start Planning Now</button>
            </div>}
        </div>
    )

}
export default UserBookings
