import { useRef,useState } from "react";
import OpenModalButton from '../OpenModalButton';
import AddExpenseFromItinerary from "./AddExpenseFromItinerary";
import {useHistory,Link} from 'react-router-dom'

const Itinerary = ({trip}) => {
    const refs = useRef([]);
    const [visible,setVisible] = useState(0);
    //get a list of dates in between trip start and end date
    const daysOfWeek = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"};
    const months = {0:"January",1:"February",2:"March",3:"April",4:"May",5:"June",6:"July",7:"August",8:"September",9:"October",10:"November",11:"December"}
    const dates_between=[];
    const history = useHistory();
    let date = new Date(trip.trip.start_date);
    while (date<=new Date(trip.trip.end_date)) {
        dates_between.push(new Date(date));
        date.setUTCDate(date.getUTCDate()+1);

    }
    const options={}
    options.timeZone = "UTC";

    const attach_booking_to_date = {};
    trip.trip.bookings_itinerary?.forEach(itinerary => {
        //place to stay
        if (itinerary.booking_startdate!==itinerary.booking_enddate) {
            let date = new Date(itinerary.booking_startdate);
            while (date<=new Date(itinerary.booking_enddate)) {
                if (!attach_booking_to_date[new Date(date)]) {
                attach_booking_to_date[new Date(date)] = [itinerary];
                } else {
                    attach_booking_to_date[new Date(date)].push(itinerary);
                }
                date.setUTCDate(date.getUTCDate()+1);
            }
        } else {
            let date = new Date(itinerary.booking_startdate);
            if (!attach_booking_to_date[date]) {
                attach_booking_to_date[date] = [itinerary];
                } else {
                    attach_booking_to_date[date].push(itinerary);
                }


        }
    })

    const handleClick= (date,index) => {
        window.scrollTo({top: refs.current[date].offsetTop -100,
        behavior: "smooth"})
        setVisible(index);
    }

    return (
        <div className="trip-itinerary">
            <div className='date-button-container'>
                {
                    dates_between.map((date,index)=> (
                        <button key={date}
                        onClick={()=>handleClick(date.getUTCDate(),index)}
                        className='date-buttons'
                        >{date.toLocaleDateString('en-US',options).slice(0,-5)}</button>
                    ))
                }
            </div>
            <div>
                {
                    dates_between.map((date,index) => (
                        <div key={date} id={date.getUTCDate()} className="itineraries-by-date"
                        ref={el => refs.current[date.getUTCDate()] = el}
                        >
                            <h2>{daysOfWeek[date.getDay()]}, {months[date.getMonth()]} {date.getUTCDate()}
                            {visible!==index ?
                                <button onClick={(e)=> {
                                e.preventDefault();
                                setVisible(index);
                            }}
                            className="visibility-arrow"
                            ><i class="fa-solid fa-angle-down fa-xl"></i></button>:
                            <button onClick={(e)=> {
                                e.preventDefault();
                                setVisible();
                            }}
                            className="visibility-arrow"
                            >
                            <i class="fa-solid fa-angle-up fa-xl"></i>
                            </button>

                            }</h2>
                            <div className='booking-info hidden' id={visible===index ?"visible":""}>
                                {attach_booking_to_date[date] ?
                                <>
                                    {attach_booking_to_date[date].map((booking,index) => (
                                        <div key={booking.id} className="booking-detail-itinerary">
                                           <div className='booking-detail-it-left'>
                                           <h2>{index+1}</h2>
                                           {booking.booking_time!=='00:00' ?<i className="fa-regular fa-clock fa-xl"></i>:""}
                                           <h3>{booking.booking_time!=='00:00' ? `${booking.booking_time}` : ""}</h3>
                                           </div>
                                           <div className="booking-detail-it-right">
                                           <img src={booking.booking.image1} alt={booking.booking.name}></img>
                                           <div className='more-booking-right'>
                                           <h3><Link to={`/bookings/${booking.booking.id}`}>{booking.booking.name}</Link></h3>
                                           <p>{booking.booking.category}</p>
                                           <p>{booking.booking.features}</p>
                                           {booking.booking.category==='Hotel' ? <p> <i className="fa-regular fa-calendar"></i> Check-In: {new Date(booking.booking_startdate).toLocaleDateString('en-US',options)}</p>:<p> <i class="fa-regular fa-clock"></i> Reservation:{new Date(booking.booking_startdate).toLocaleDateString('en-US',options)} at {booking.booking_time}</p> }
                                           {booking.booking.category==='Hotel' ? <p> <i className="fa-regular fa-calendar"></i> Check-Out: {new Date(booking.booking_enddate).toLocaleDateString('en-US',options)}</p>: ""}
                                           {!booking.expensed ? <OpenModalButton
                                           buttonText="Add Expense"
                                           modalComponent={<AddExpenseFromItinerary trip={trip} booking={booking}/>}
                                           />: <button onClick={(e)=> {
                                            e.preventDefault();
                                            history.push(`/trips/${trip.id}/expenses/${booking.expense_id}`)
                                           }}
                                           className="view-expense-button"
                                           >View Expense</button>}
                                           </div>
                                           </div>
                                        </div>
                                    ))
                                }
                                </>:
                                <div className='no-itinerary'>
                                <p>Build your itinerary by exploring <Link to={`/explore/${trip.trip.location[0]}`}>{trip.trip.location[0]}</Link> now.</p>
                                </div>
                                }

                            </div>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}

export default Itinerary
