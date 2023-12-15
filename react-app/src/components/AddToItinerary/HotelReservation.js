import {useSelector} from 'react-redux';
import {useState,useEffect} from 'react';

function HotelReservation ({trip,booking}) {
    const [checkIn,setCheckIn] = useState();
    const [checkOut,setCheckOut] = useState();
    const [Rooms,setRooms] = useState(1);
    const [price,setPrice] = useState(0);
    const [errors,setErrors] = useState({});
    const user = useSelector(state=>state.session.user);
    const tripToAdd = user.trips[trip];
    console.log(tripToAdd);
    const handleReservation = (e) => {
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
        if (Object.values(validateErrors).length) {
            setErrors(validateErrors);
            return;

        } else {
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
        <form>
        <h2>{booking.name}</h2>
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

        <h2>View Prices for your Travel Dates</h2>
        <p>$ {booking.price}</p>
        <p>Total: $ {price}</p>
          {checkIn && checkOut ?
            <p>including taxes and fees</p>:
            ""
        }

        <button
        onClick={handleReservation}>Reserve</button>
        </form>
    )

}
export default HotelReservation
