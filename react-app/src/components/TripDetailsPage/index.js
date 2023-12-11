import {useParams} from 'react-router-dom';
import {useSelector} from 'react-redux';
import { Link,useHistory } from 'react-router-dom';
import {useState} from 'react';
import OpenModalButton from '../OpenModalButton';
import InviteOthers from '../AllTripsPage/InviteOthersModal';
import UpdateTripModal from '../UpdateTripForm/Modal';
import DeleteModal from '../AllTripsPage/DeleteModal';
import Expense from './Expense';
import Itinerary from './Itinerary';
import './TripDetails.css'

const TripDetails = ({type}) => {
    const {id} = useParams();
    const user = useSelector(state=>state.session.user);
    const history=useHistory();
    const [hidden,setHidden] = useState('hidden')
    let trip_found;

    user?.trips && ( Object.values(user?.trips).forEach(trip=> {
        if (trip.trip.id===parseInt(id)) {
            trip_found = trip;
            return
        }
    }))
    if (!trip_found){
        history.push('/404');
        return null;
    }
    const images=['https://images.unsplash.com/photo-1522878129833-838a904a0e9e?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1433838552652-f9a46b332c40?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1475503572774-15a45e5d60b9?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTR8fHxlbnwwfHx8fHw%3D',
    'https://images.unsplash.com/photo-1515859005217-8a1f08870f59?q=80&w=2820&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1482192505345-5655af888cc4?q=80&w=2728&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1532274402911-5a369e4c4bb5?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2673&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NDV8fHxlbnwwfHx8fHw%3D',
    'https://images.unsplash.com/photo-1519451241324-20b4ea2c4220?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NDd8fHxlbnwwfHx8fHw%3D',
    'https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NTZ8fHxlbnwwfHx8fHw%3D',
    'https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8NTV8fHxlbnwwfHx8fHw%3D',
    'https://images.unsplash.com/photo-1440778303588-435521a205bc?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Njd8fHxlbnwwfHx8fHw%3D',
    'https://images.unsplash.com/photo-1505778276668-26b3ff7af103?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8ODF8fHxlbnwwfHx8fHw%3D'
    ]
    const choice = Math.floor(Math.random()*images.length)

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
            "type": relationship.owed===0 && relationship.owes===0 ? 'settled' :( relationship.user_one.id===user.user.id && relationship.owed-relationship.owes>0 && relationship.owed-relationship.owes!==0) || (relationship.user_one.id!==user.user.id && relationship.owed-relationship.owes<0 && relationship.owed-relationship.owes!==0) ? "payer" : "payee",
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
    const options={}
    options.timeZone = "UTC";
    return (
        <div className='trip-details'>
            <div className='trip-detail-left'>
           <h2><Link to='/trips' className='breadcrumb'> All Trips </Link> {'>'} {trip_details.name}</h2>
            <div className='trip-detail-universal'>
           <img src={trip_details.image ? trip_details.image : images[choice] } alt={trip_details.name} className='trip-detail-image'
           onError={e => { e.currentTarget.src = "https://images.unsplash.com/photo-1522878129833-838a904a0e9e?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"}}
           ></img>

           <OpenModalButton modalComponent={<UpdateTripModal trip={trip_found}/>} buttonText={`${trip_details.name}`} className='update-trip-button' /><i className="fa-regular fa-pen-to-square update-trip-button fa-sm" id='dont-change'></i>

            <p className="trip-info-date"><i className="fa-solid fa-calendar-day"/> {new Date(trip_details.start_date).toLocaleDateString('en-US',options)} - {new Date(trip_details.end_date).toLocaleDateString('en-US',options)}</p>
            <p className="trip-info-location"><i className="fa-solid fa-location-dot"/> {trip_details.location[0]}, {trip_details.location[1]}</p>

            <i className="fa-solid fa-user-plus invite-button-trip" id='dont-change'/>
            <OpenModalButton
              buttonText="Invite"
              modalComponent={<InviteOthers tripId={trip_found.id}
              />}
              className='invite-button-trip'
            />

           { trip_found.creator ?
           <>
            <i className="fa-solid fa-trash-can delete-button-trip" id='dont-change'/>
            <OpenModalButton
              buttonText="Delete"
              modalComponent={<DeleteModal trip={trip_found} />}
              className="delete-button-trip"
            />
            </>
            :
            <></>
          }
            </div>

            <div className="trip-toggle">
                <Link to={`/trips/${id}/itineraries`} className={type==='itinerary' ? 'td-active' : 'td-passive'}>Itinerary</Link>
                <span> | </span>
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
                        <button className="see-more"
                                onClick={(e)=> {
                                    e.preventDefault();
                                    if (hidden==="hidden") {
                                        setHidden("display-details")
                                    } else {
                                        setHidden("hidden")
                                    }
                                }}
                        > {hidden==="hidden" ?<i className="fa-solid fa-angle-down fa-2xl"></i> : <i className="fa-solid fa-angle-up fa-2xl"></i>} </button>
                        {
                            trip_details.users.map(user=> (
                                <div key={user.user.id}>
                                <div className='group-detail-top'>
                                <img src='https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-teal22-100px.png' alt='profile' className='expense-profile'></img>
                                <h3>{user.user.first_name} {user.user.last_name}</h3>
                                </div>
                               {total_info[user.user.id] && total_info[user.user.id]!==0 ? <h4 className='group-detail-balance'>{(total_info[user.user.id] >0 ? <span className='is-owed'>{`gets back $ ${total_info[user.user.id].toFixed(2)}`}</span>: <span className='owes'>{`owes $ ${Math.abs(total_info[user.user.id].toFixed(2))}`}</span>)}</h4>: <h4 className='group-detail-balance'>Settled Up</h4>}
                                { settled[user.user.id] ?
                                    <ul className={hidden}>
                                        {
                                            settled[user.user.id].map(settlement => (
                                                <li key={settlement.id}>  {user.user.first_name} {user.user.last_name[0]} is settled up with {settlement.user.first_name} {settlement.user.last_name[0]}. </li>
                                            ))
                                        }
                                    </ul> :
                                    <></>
                                }
                                {
                                     <ul className={hidden}>
                                   {group_balances[user.user.id] ? group_balances[user.user.id].map(detail => (
                                    <div key={detail.id}>
                                    { detail.type!=='settled' ?
                                       <li className={detail.type==='payee' ? "owes" : "is-owed"}>
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
