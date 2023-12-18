import { useState,useEffect} from "react";
import {useSelector,useDispatch} from 'react-redux';
import { useHistory } from 'react-router-dom';
import { addItinerary,authenticate } from '../../store/session';
function RestaurantThingReservation ({trip,booking,closeModal}) {
    const [individuals,setIndividuals] = useState(2);
    const [reservationTime,setReservationTime]= useState();
    const [reservationDate,setReservationDate] = useState();
    const [price,setPrice] = useState();
    const [errors,setErrors] = useState({});
    const [hidden,setHidden] = useState(true);
    const user = useSelector(state=>state.session.user);
    const dispatch = useDispatch();
    const history = useHistory();
    const tripToAdd = user.trips[trip];
//make a list of reservation times based on opening and closing hours
//parse opening and closing hours
let parsedOpen;
let parsedClose;
let parsedOpenTime;
let parsedCloseTime;
if (booking.category==="Restaurants"){
    parsedOpen = booking.opening_hour.split(' ');
    parsedClose = booking.closing_hour.split(' ');
    parsedOpenTime=parsedOpen[0].split(':');
    parsedCloseTime = parsedClose[0].split(':')
    if (parsedOpen[1]==='AM') {
        parsedOpenTime[0] = Number(parsedOpenTime[0])
        parsedOpenTime[1] = Number(parsedOpenTime[1])
    } else {
        parsedOpenTime[0] = Number(parsedOpenTime[0])+12
        parsedOpenTime[1] = Number(parsedOpenTime[1])
    }

    if (parsedClose[1]==='AM') {
        parsedCloseTime[0] = Number(parsedCloseTime[0])
        parsedCloseTime[1] = Number(parsedCloseTime[1])
    } else {
        parsedCloseTime[0] = Number(parsedCloseTime[0])+12
        parsedCloseTime[1] = Number(parsedCloseTime[1])
    }
}
    const reservationTimes = [];
if (booking.category==="Restaurants"){
    const open = new Date();
    open.setHours(parsedOpenTime[0],parsedOpenTime[1],0);
    const close = new Date();
    close.setHours(parsedCloseTime[0],parsedCloseTime[1], 0);

    while (open < close) {
    reservationTimes.push(open.toLocaleString('en-US', {hour: '2-digit', minute: '2-digit'}));
    open.setMinutes(open.getMinutes() + 30);
    }
} else {
    const open = new Date();
    open.setHours(8,0,0);
    const close = new Date();
    close.setHours(17,0,0);

    while (open < close) {
    reservationTimes.push(open.toLocaleString('en-US', {hour: '2-digit', minute: '2-digit'}));
    open.setHours(open.getHours() + 1);
    }
}

    useEffect(()=> {
        if (reservationDate) setHidden(false);
        else setHidden(true);
    },[reservationDate])

    useEffect(()=> {
            setPrice((booking.price*individuals*1.14))
    },[individuals])

    const handleReservation = async(e) => {
        e.preventDefault();
        const validateErrors={}

        //check reservation date
        if (!reservationDate) validateErrors.date = "Reservation date is required";
        if (new Date(reservationDate)<new Date()) validateErrors.date = "Reservation date must be in the future ";
        if (new Date(reservationDate)<new Date(tripToAdd.trip.start_date)) validateErrors.date = "Reservation date cannot be before trip's start date";
        if (new Date(reservationDate)>new Date(tripToAdd.trip.end_date)) validateErrors.date = "Reservation date cannot be after the trip's end date";
        //check reservation time
        if (!reservationTime) validateErrors.time = "Reservation time is required";

        //check if trip already has a reservation on that same day and time
        const existingReservation= tripToAdd.trip.bookings_itinerary.filter(booking=> new Date(booking.booking_startdate).getTime()===new Date(reservationDate).getTime() && booking.booking_time===reservationTime);

        if (existingReservation.length) validateErrors.existing_time = `It looks like you already have a reservation at ${existingReservation[0].booking.name} on this day at ${reservationTime}. Please try a different time`

        if (Object.values(validateErrors).length) {
            setErrors(validateErrors);
            return;

        } else {
            setErrors({});
            const expensed=false;
            if (booking.category==='Restaurants') {
            setPrice(0);
            }
            const data = await dispatch(addItinerary(trip,tripToAdd.trip.id,booking.id,reservationDate,reservationDate,reservationTime,expensed,price));
            if (data) {
                setErrors(data);
                console.log(data);
                return;
            } else {
                dispatch(authenticate());
                history.push(`/trips/${tripToAdd.trip.id}/itineraries`);
                closeModal();
             }
        }


    }
    let counter=0
    return (
    <form>
        {booking.category ==='Restaurants' ? <h2>Make a Reservation at {booking.name}</h2>: <h2>Reserve a Spot at {booking.name}</h2>}
        {booking.category==='Restaurants' ?
        <div>
            <label><i className="fa-solid fa-people-group"></i>Party Size</label>
            <select defaultValue={2}>
                {
                    tripToAdd.trip.users.map(user=> {
                        counter++;
                        return <option value={counter}>{counter} {counter!==1 ? "people" :"person"}</option>

                })
                }
            </select>
            <p className='errors'></p>
        </div>
       :
       <div>
        <label><i className="fa-solid fa-people-group"></i></label>
            <select
            value={individuals}
            onChange={(e)=> setIndividuals(e.target.value)}
            >
            {
                tripToAdd.trip.users.map(user=> {
                    counter++;
                    return <option value={counter}>{counter} {counter!==1 ? "people" :"person"}</option>

            })
            }
            </select>
            <p className='errors'></p>
       </div>
    }

        <div>
            <label> <i className="fa-regular fa-calendar"></i>Reservation Date</label>
            <input
                type="date"
                value={reservationDate}
                onChange={(e)=> setReservationDate(e.target.value)}
            />
              {errors.date ? <p className='errors'>{errors.date}</p>: <p className='errors'></p>}
        </div>

        <div className={hidden ? "reservation-time hidden" : "reservation-time"}>
            <label><i className="fa-regular fa-clock"></i>Reservation Time</label>
            {reservationTimes.map(time => (
                <button key={time}
                onClick={(e)=> {
                    e.preventDefault();
                    setReservationTime(time);
                    setHidden(true);
                }}>
                    {time}
                </button>
            ))}
              {errors.time ? <p className='errors'>{errors.time}</p>: <p className='errors'></p>}
        </div>
        { reservationTime ?
        <div className="reservation-time-info">
            <p>Your selected reservation time: {reservationTime}</p>
            <button
            onClick={(e)=>{
                e.preventDefault();
                setReservationTime(null);
                setHidden(false);
            }}
            >Change Reservation Time</button>
            {errors.existing_time ? <p className='errors'>{errors.existing_time}</p>: <p className='errors'></p>}
        </div> :
        <></>
        }
        {
            booking.category==='Things To Do' ?
            <div>
            {reservationDate && reservationTime ?
            <>
            <p>$ {booking.price} per individual</p>
            <p>Total: $ {price?.toFixed(2)}</p>
            <p title="assuming 14% tax">including taxes and fees</p>

            </>
            :
            ""
            }
            </div>:<p></p>
        }

        <button onClick={handleReservation}>Reserve</button>
        <button onClick={(e)=> {
            e.preventDefault();
            closeModal()}} id='settle-cancel'>Cancel</button>

    </form>
    )

}

export default RestaurantThingReservation;
