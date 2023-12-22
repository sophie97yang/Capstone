import {useSelector,useDispatch} from 'react-redux';
import {useState,useEffect} from 'react';
import { addItinerary,authenticate } from '../../store/session';
import { useHistory } from 'react-router-dom';

function HotelReservation ({trip,booking,closeModal,detail}) {
    const [checkIn,setCheckIn] = useState();
    const [checkOut,setCheckOut] = useState();
    const [Rooms,setRooms] = useState(1);
    const [price,setPrice] = useState(0);
    const [expensed,setExpensed] = useState(false);
    const [errors,setErrors] = useState({});
    const user = useSelector(state=>state.session.user);
    const dispatch = useDispatch();
    const history = useHistory();
    const options={}
    options.timeZone = "UTC";

    const tripToAdd = user.trips[trip];

    const handleReservation = async(e) => {
        e.preventDefault();
        const validateErrors = {};
        //check the check in and check out dates
        if (!checkIn) validateErrors.checkIn = "Check-In date is required"
        if (!checkOut) validateErrors.checkOut = "Check-Out date is required"
        if (new Date(checkIn) < new Date(tripToAdd.trip.start_date)) validateErrors.checkIn = "Check-In cannot be before trip's start date";
        if (new Date(checkIn) < new Date()) validateErrors.checkIn = "Check-In cannot be in the past";
        if (new Date(checkOut) > new Date(tripToAdd.trip.end_date)) validateErrors.checkIn = "Check-Out cannot be after trip's end date";
        if (new Date(checkOut) < new Date()) validateErrors.checkOut = "Check-Out cannot be in the past";
        //number of rooms cannot exceed number of guests involved in trip
        if (Rooms>tripToAdd.trip.users.length) validateErrors.Rooms = "Number of rooms cannot exceed the number of trip members";
        if (Rooms<1) validateErrors.Rooms="You must reserve at least 1 room"

        //check if there is already an existing reservation
        const existingReservation= tripToAdd.trip.bookings_itinerary.filter(booking=> {
            //reservation start date is between check in and check out
            const instance1 = new Date(booking.booking_startdate).getTime()>= new Date(checkIn).getTime() && new Date(booking.booking_startdate).getTime()<= new Date(checkOut).getTime();
            //reservation end date is between check in and check out
            const instance2 = new Date(booking.booking_enddate).getTime()>= new Date(checkIn).getTime() && new Date(booking.booking_enddate).getTime()<= new Date(checkOut).getTime();
            //check in is between reservation start and end date
            const instance3 = new Date(checkIn).getTime()>= new Date(booking.booking_startdate).getTime() && new Date(checkIn).getTime()<= new Date(booking.booking_enddate).getTime();
            //check out is between reservation start and end date
            const instance4 = new Date(checkOut).getTime()>= new Date(booking.booking_startdate).getTime() && new Date(checkOut).getTime()<= new Date(booking.booking_enddate).getTime();
            return (booking.booking.category==='Hotel' && (instance1||instance2||instance3||instance4))
        });

        if (existingReservation.length) validateErrors.existing_stay = `It looks like you already have a reservation at ${existingReservation[0].booking.name} from ${new Date(existingReservation[0].booking_startdate).toLocaleDateString('en-US',options)}-${new Date(existingReservation[0].booking_enddate).toLocaleDateString('en-US',options)}. Please try again.`;

        if (Object.values(validateErrors).length) {
            setErrors(validateErrors);
            return;

        } else {
            setErrors({})
            const reservation = "00:00";
            const data = await dispatch(addItinerary(trip,tripToAdd.trip.id,booking.id,checkIn,checkOut,reservation,expensed,price,Rooms));
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

    useEffect(()=> {
        if (checkIn && checkOut) {
            setPrice((new Date(checkOut).getTime()- new Date(checkIn).getTime())/(1000*60*60*24)*booking.price*Rooms*1.14)
        } else {
            setPrice(0)
        }
    },[checkIn,checkOut,Rooms])


    return (
        <form className='reservation-form hotel-form'>
        {!detail ? <h2>{booking.name}</h2>:""}
            <div id='checkin-out'>
            <div>
            <label>Check-In </label>
            <input
                type="date"
                value={checkIn}
                onChange={(e)=> setCheckIn(e.target.value)}
            />
            {errors.checkIn ? <p className='errors'>{errors.checkIn}</p>: <p className='errors'></p>}
            </div>
            <div>
            <label>Check-Out </label>
            <input
                type="date"
                value={checkOut}
                onChange={(e)=> setCheckOut(e.target.value)}
            />
            {errors.checkOut ? <p className='errors'>{errors.checkOut}</p>: <p className='errors'></p>}
            </div>
            </div>

            <div>
            <label>Rooms</label>
            <input
            type='number'
            value={Rooms}
            onChange={(e)=> setRooms(e.target.value)}
            >
            </input>
            {errors.Rooms ? <p className='errors'>{errors.Rooms}</p>: <p className='errors'></p>}
            </div>
        <div className='itinerary-price-details'>
        <h4>VIEW PRICES FOR YOUR TRAVEL DATES</h4>
        <h3 id='price-per-night'>$ {booking.price} / night</h3>
        <h3 id='total-itinerary'>Total: $ {price.toFixed(2)}</h3>
          {checkIn && checkOut ?
            <p title="assuming 14% tax" id='tax'>**including taxes and fees</p>:
            <p></p>
        }
        </div>

        {/* <div id='expense-itinerary'>
        <label>Expense this itinerary?</label>
        <input
        type="checkbox"
        value= {expensed}
        onChange={(e)=> setExpensed(!expensed)}
        ></input>
        </div> */}

        {errors.existing_stay ? <p className='errors'>{errors.existing_stay}</p>: <p className='errors'></p>}

        <div id='itinerary-buttons'>
        <button onClick={(e)=> {
            e.preventDefault();
            closeModal()}} id='settle-cancel'>Cancel</button>
        <button
        onClick={handleReservation}
        className='submit-button'
        >Reserve</button>
        </div>
        </form>
    )

}
export default HotelReservation
