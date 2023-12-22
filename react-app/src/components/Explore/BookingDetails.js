import { useDispatch,useSelector } from "react-redux";
import { useParams,Link,useHistory } from "react-router-dom";
import {getBookings} from '../../store/booking';
import { useEffect,useState,useRef } from "react";
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import AddToItinerary from "../AddToItinerary";
import LocationMap from "../GoogleMaps/bookingLocation";
import './Explore.css';
import '../Navigation/Navigation.css'

function BookingDetails() {
    const {id} = useParams()
    const dispatch = useDispatch();
    const bookings = useSelector(state=>state.bookings.bookings);
    const user = useSelector(state=>state.session.user);
    const ref=useRef();
    const history = useHistory();
    const booking = bookings[Number(id)];
    let stars=''
        for (let i=0;i<Math.round(booking?.rating);i++) {
            stars+='🟢'
        }
    if (booking) booking.stars=stars;
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
        if (new Date().getHours()>=parsedOpenTime[0] &&new Date().getHours()<=parsedCloseTime[0] ) setStatus('Open Now');
        else setStatus('Closed Now')

        }
    },[booking?.category, booking?.opening_hour, booking?.closing_hour])

    useEffect(()=> {
        setReviews(Math.floor(Math.random()*2000))
    },[])

    const handleClick= (ref) => {
        window.scrollTo({top: ref.current.offsetTop -100,
        behavior: "smooth"})
    }

    const renderRightArrow = (onClickHandler, hasNext, label) => hasNext && (
        <button type="button" onClick={onClickHandler} title={label} className='carousel-buttons button-right'>
            <i class="fa-solid fa-arrow-right fa-xl"></i>
        </button>
    )

    const renderLeftArrow = (onClickHandler, hasPrev, label) => hasPrev && (
    <button type="button" onClick={onClickHandler} title={label} className='carousel-buttons button-left'>
        <i class="fa-solid fa-arrow-left fa-xl"></i>
    </button>
)
    if (!booking) return null;

    return (
        <div className='explore-booking-details'>
            <h3 className='breadcrumb-container'><Link to={`/explore/${booking.city}`} className='breadcrumb'>Explore {booking.city} </Link> {`  >  `} {booking.name}</h3>
            <div className='booking-info-top'>
            <div className='left-booking'>
            <h2>{booking.name}</h2>
            <h3>{booking.stars} |  {reviews} reviews</h3>
            <h3 className='features'>{booking.features}</h3>
            {booking.opening_hour ? <h3> <span className={status==='Open Now' ? "open-status":"closed-status"}>{status}</span> | <i className='fa-regular fa-clock'></i> {booking.opening_hour} - {booking.closing_hour} </h3>:<></>}
            </div>
            { booking.category!=='Restaurants' ?
            <div className='price-booking'>
               <p>$ {booking.price.toFixed(2)} <span> {booking.category==='Hotel' ? 'per night' :<> {booking.category==='Things To Do' ?'per individual':""}</>}</span></p>
               {user ? <button onClick={ ()=> handleClick(ref)}>Reserve</button>:""}
            </div>
            :
            <></>
            }
            </div>
            <Carousel infiniteLoop={true}
            renderArrowNext={renderRightArrow} renderArrowPrev={renderLeftArrow}
            showStatus={false}
            className="explore-detail-carousel">
                <img src={booking.image1} alt='one' ></img>
                <img src={booking.image2} alt='two'></img>
                <img src={booking.image3} alt='three'></img>
            </Carousel>
            <div className='about-booking'>
            <h2>About</h2>
            <p>{booking.description}</p>
            </div>

            <div className='explore-details-bottom'>
            <div className='location-contact-booking'>
            <h2>Location and Contact</h2>
            <LocationMap city={booking.city} lat={booking.lat} lng ={booking.lng} name={booking.name}/>
            <div className='contact-info'>
            <p><i className='fa-solid fa-phone'></i> {booking.contact_info} </p>
            <p>•</p>
            <p><i className="fa-solid fa-up-right-from-square"></i> <a href={`https://www.${booking.website}`} target="_blank" rel="noreferrer" >{booking.website}</a></p>
            </div>
            </div>

            {user ?
            <div ref={ref} className='add-to-itinerary-explore-page'>
            <h2>Add <span> {booking.name} </span>to Your Trip</h2>
            <AddToItinerary booking={booking} detail={true}/>
            </div>:
            <div className='add-to-itinerary-explore-page no-user'>
                <h2>Log In to Unlock the Best of TripSplit</h2>
                <button onClick={(e)=> {
              			e.preventDefault();
              			history.push('/login');
            		}} id='longer' className='action-button-ls'>Log in</button>

            </div>
            }
            </div>
        </div>
    )
}

export default BookingDetails;
