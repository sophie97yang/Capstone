import { useRef } from "react";

const Itinerary = ({trip}) => {
    const refs = useRef([]);
    //get a list of dates in between trip start and end date
    const daysOfWeek = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"};
    const months = {0:"January",1:"February",2:"March",3:"April",4:"May",5:"June",6:"July",7:"August",8:"September",9:"October",10:"November",11:"December"}
    const dates_between=[];
    console.log(trip);
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

    console.log(attach_booking_to_date);

    const handleClick= (date) => {
        window.scrollTo({top: refs.current[date].offsetTop -100,
        behavior: "smooth"})
    }

    return (
        <div>
            <div>
                {
                    dates_between.map(date=> (
                        <button key={date}
                        onClick={()=>handleClick(date.getUTCDate())}
                        >{date.toLocaleDateString('en-US',options).slice(0,-5)}</button>
                    ))
                }
            </div>
            <div>
                {
                    dates_between.map(date => (
                        <div key={date} id={date.getUTCDate()} className="itineraries-by-date"
                        ref={el => refs.current[date.getUTCDate()] = el}
                        >
                            <h2>{daysOfWeek[date.getDay()]}, {months[date.getMonth()]} {date.getUTCDate()}</h2>
                            <div className='booking-info'>
                                {
                                    attach_booking_to_date[date]?.map((booking,index) => (
                                        <div key={booking.id} >
                                           <h2>{index+1} {booking.booking_time!=='00:00' ? `: ${booking.booking_time}` : ""}</h2>
                                           <img src={booking.booking.image1} alt={booking.booking.name}></img>
                                           <h3> {booking.booking.name}</h3>
                                           <p>{booking.booking.category}</p>
                                           <p>{booking.booking.features}</p>
                                           <p>{booking.booking.category==='Hotel' ? `Check-In:${new Date(booking.booking_startdate).toLocaleDateString('en-US',options)}`: `Reservation:${new Date(booking.booking_startdate).toLocaleDateString('en-US',options)} @ ${booking.booking_time}`}</p>
                                           <p>{booking.booking.category==='Hotel' ? `Check-Out:${new Date(booking.booking_enddate).toLocaleDateString('en-US',options)}`: ""}</p>
                                           {!booking.expensed ? <button>Add Expense</button>: <button>View Expense</button>}
                                        </div>
                                    ))
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
