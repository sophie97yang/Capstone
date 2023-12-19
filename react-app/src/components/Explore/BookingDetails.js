import { useDispatch,useSelector } from "react-redux";
import { useParams,Link } from "react-router-dom";
import {getBookings} from '../../store/booking';
import { useEffect,useState } from "react";
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import AddToItinerary from "../AddToItinerary";

function BookingDetails() {
    const {id} = useParams()
    const dispatch = useDispatch();
    const bookings = useSelector(state=>state.bookings.bookings);
    const user = useSelector(state=>state.session.user);
    const booking = bookings[Number(id)];
    const [status,setStatus] = useState();
    const [reviews,setReviews] = useState();

    useEffect(()=> {
        dispatch(getBookings())
    },[dispatch])

    useEffect(()=> {
        if (booking?.category==="Restaurants"){
            let parsedOpen = booking.opening_hour.split(' ');
            let parsedClose = booking.closing_hour.split(' ');
            let parsedOpenTime=parsedOpen[0].split(':');
            let parsedCloseTime = parsedClose[0].split(':')
            if (parsedOpen[1]==='AM') {
                parsedOpenTime[0] = Number(parsedOpenTime[0])
            } else {
                parsedOpenTime[0] = Number(parsedOpenTime[0])+12
            }

            if (parsedClose[1]==='AM') {
                parsedCloseTime[0] = Number(parsedCloseTime[0])
            } else {
                parsedCloseTime[0] = Number(parsedCloseTime[0])+12
            }

        if (new Date().getHours()>=parsedOpenTime[0] &&new Date().getHours()<=parsedCloseTime[0] ) setStatus('Open now');
        else setStatus('Closed')

        }
    },[booking?.category, booking?.opening_hour, booking?.closing_hour])

    useEffect(()=> {
        setReviews(Math.floor(Math.random()*2000))
    },[])

    if (!booking) return null;

    return (
        <div>
            <h3 className='breadcrumb-container'><Link to={`/explore/${booking.city}`} className='breadcrumb'>Explore {booking.city} </Link> {`  >  `} {booking.name}</h3>
            <h2>{booking.name}</h2>
            <h3>{booking.stars} |  {reviews} reviews</h3>
            <h3>{booking.features}</h3>
            {booking.opening_hour ? <h3> <i className='fa-regular fa-clock'></i> {booking.opening_hour} - {booking.closing_hour} | {status}</h3>:<></>}
            <p>{booking.description}</p>
            <p><i className='fa-solid fa-phone'></i> {booking.contact_info} </p>
            <p><i className="fa-solid fa-up-right-from-square"></i> <a href={`https://www.${booking.website}`}>{booking.website}</a></p>
            <Carousel infiniteLoop={true}>
                <img src={booking.image1} alt='one' ></img>
                <img src={booking.image2} alt='two'></img>
                <img src={booking.image3} alt='three'></img>
            </Carousel>

            {user &&
            <div>
            <h2>Add <span> {booking.name} </span>to Your Trip</h2>
            <AddToItinerary booking={booking} detail={true}/>
            </div>
            }
        </div>
    )
}

export default BookingDetails;
