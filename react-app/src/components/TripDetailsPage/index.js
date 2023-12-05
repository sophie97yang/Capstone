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
    console.log('between_user_expenses',trip_details.between_user_expenses)
    //handle information for group balances
    const group_balances={}
    const total_info={}
    const settled = {}
    trip_details.users.forEach(user=> {
        let total=0
        const relationships =trip_details.between_user_expenses.filter(relationship=> { return (relationship.user_one.id===user.user.id || relationship.user_two.id===user.user.id) && !(relationship.user_one.id===user.user.id && relationship.user_two.id===user.user.id)} )
         const relationship_info = relationships.map(relationship => {
           return {
            "id":relationship.id,
            "user":relationship.user_one.id===user.user.id ? relationship.user_two : relationship.user_one,
            "type": relationship.owed===0 && relationship.owes===0 ? 'settled' : relationship.user_one.id===user.user.id && relationship.owed-relationship.owes>0 && relationship.owed-relationship.owes!==0 ? "payer" : "payee",
            "settlement":Math.abs(relationship.owed-relationship.owes).toFixed(2)
        }
         })

         const settled_expenses= relationship_info.filter(relationship=> relationship.type === 'settled')

         relationship_info.forEach(relationship=> {
            relationship.type==='payer' ? total+=Number(relationship.settlement) : total-=Number(relationship.settlement)
         })





         group_balances[user.user.id]=relationship_info
         total_info[user.user.id]=total
         settled[user.user.id] = settled_expenses.length ? settled_expenses : null
    })

    console.log('group_balances',group_balances,'total',total_info,'settled',settled)
    return (
        <div className='trip-details'>
            <div className='trip-detail-left'>
           <h2><Link to='/trips' className='breadcrumb'> All Trips </Link> {'<'} {trip_details.name}</h2>
            <div className='trip-detail-universal'>
           <img src={trip_details.image} alt={trip_details.name} className='trip-detail-image'></img>

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
                 <Expense trip={trip_found} group_balances={group_balances} total_info={total_info}/>
                :
                <Itinerary />
            }
            </div>
            <div className='trip-detail-right'>
                {
                    type==='expense' ?
                    <div>
                        <h2>Group Balances</h2>
                        {
                            trip_details.users.map(user=> (
                                <div key={user.user.id}>
                                <h3>{user.user.first_name} {user.user.last_name}</h3>
                               {total_info[user.user.id] && total_info[user.user.id]!==0 ? <h4>{(total_info[user.user.id] >0 ? `gets back $ ${total_info[user.user.id].toFixed(2)}`: `owes $ ${Math.abs(total_info[user.user.id].toFixed(2))}`)}</h4>: <h4>Settled Up</h4>}
                                { settled[user.user.id] ?
                                    <ul>
                                        {
                                            settled[user.user.id].map(settlement => (
                                                <li key={settlement.id}>  {user.user.first_name} {user.user.last_name[0]} is settled up with {settlement.user.first_name} {settlement.user.last_name[0]}. </li>
                                            ))
                                        }
                                    </ul> :
                                    <></>
                                }
                                {
                                     <ul>
                                   {group_balances[user.user.id] ? group_balances[user.user.id].map(detail => (
                                    <div key={detail.id}>
                                    { detail.type!=='settled' ?
                                       <li>
                                        {user.user.first_name} {user.user.last_name[0]}. {detail.type==='payee' ? "owes" : "is owed"} ${detail.settlement} {detail.type==='payee' ? "to" : "by"} {detail.user.first_name}  {detail.user.last_name[0]}.
                                       </li> :<></>

                                    }
                                     </div>
                                    )): "settled up"
                                }
                                    </ul>
                                }

                                </div>
                            ))
                        }
                    </div>
                    :
                    <div>
                        <h2>Google Maps</h2>
                    </div>
                }

            </div>
        </div>
    )


}

export default TripDetails;
