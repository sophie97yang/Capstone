import {useParams} from 'react-router-dom';
import {useSelector} from 'react-redux';
import { Link } from 'react-router-dom';
import OpenModalButton from '../OpenModalButton';
import InviteOthers from '../AllTripsPage/InviteOthersModal';
import UpdateTripModal from '../UpdateTripForm/Modal';
import Expense from './Expense';
import Itinerary from './Itinerary';
import './TripDetails.css'

const TripDetails = ({type}) => {
    const {id} = useParams();
    const user = useSelector(state=>state.session.user);
    let trip_found;

    user?.trips && ( Object.values(user?.trips).forEach(trip=> {
        if (trip.trip.id===parseInt(id)) {
            trip_found = trip;
            return
        }
    }))

    const trip_details = trip_found.trip

    return (
        <div className='trip-details'>
            <Link to='/trips' className='breadcrumb'>{'<'} All Trips </Link>

            <div className='trip-detail-universal'>
           <img src={trip_details.image} alt={trip_details.name}></img>

           <OpenModalButton modalComponent={<UpdateTripModal trip={trip_found}/>} buttonText={`${trip_details.name}`} />

            <p><i className="fa-solid fa-calendar-day"/> {new Date(trip_details.start_date).toLocaleDateString()} - {new Date(trip_details.end_date).toLocaleDateString()}</p>
            <p><i className="fa-solid fa-location-dot"/> {trip_details.location[0]}, {trip_details.location[1]}</p>

            <i className="fa-solid fa-user-plus"/>
            <OpenModalButton
              buttonText="Invite"
              modalComponent={<InviteOthers trip={trip_found}/>}
            />
            </div>

            <div>
                <Link to={`/trips/${id}/itineraries`} className={type==='itinerary' ? 'td-active' : 'td-passive'}>Itinerary</Link>
                <Link to={`/trips/${id}/expenses`}  className={type==='expense' ? 'td-active' : 'td-passive'}>Expenses</Link>
            </div>
            {
                type==='expense' ?
                 <Expense trip={trip_found}/>
                :
                <Itinerary />
            }

        </div>
    )


}

export default TripDetails;
