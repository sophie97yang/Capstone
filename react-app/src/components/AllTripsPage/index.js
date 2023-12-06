import { useSelector } from "react-redux";
import { useHistory,Link } from "react-router-dom";
import './AllTrips.css'
import TripOptions from "./TripOptions";
import OpenModalButton from "../OpenModalButton";
import AddExpenseForm from "../AddExpenseForm"

const AllTrips = () => {
    const user = useSelector(state=>state.session.user);
    const history=useHistory();
    const trips =user?.trips ? Object.values(user?.trips):null;

    //calculate how many days until the trip
    trips?.forEach(trip=> {
        const today = new Date()
        const start = new Date(trip.trip.start_date)
        trip.until = Math.ceil((start.getTime()-today.getTime())/(1000*60*60*24))
        //calculate general overview of what is owed by you and how much you spent
        let owed=0;
        let owe=0
        //for each trip's expense
        trip.trip.expenses.forEach(expense => {
            //user expense detail for specific trip
            const detail = expense.details.filter(detail=>detail.user.id===user.id)
            //if user is the payer
            if(expense.payer.id===user.id) {
                //and is involved in the expense
                if (detail.length){
                    owed+=expense.total-(detail[0].price)
                    //if user is the payer and is not involved in the expense
                } else {
                    owed+=expense.total
                }
            }
            //if user is not the payer but is involved in the expense
            else if (detail.length) {
                owe+=detail[0].price
            }
        })
        trip.lent=owed.toFixed(2);
        trip.owe=(owed-owe).toFixed(2);
    })

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

    return (
        <div className='all-trips'>
            <h2 className='breadcrumb-container'><Link to='/' className='breadcrumb'>Home </Link> {`  >`}  My Trips</h2>
            <div className='all-trips-buttons'>
                <button onClick={(e)=> {
                    e.preventDefault();
                    history.push('/trips/new')
                }}>Create a New Trip</button>
                <button onClick={(e)=> {
                    e.preventDefault();
                    history.push('/bookings')
                }}>Explore places to go</button>
            </div>
           { trips?.map(trip=> (
            <div key={trip.id} className='individual-trip'>
            <div className='my_trips-left'>
            <img src={trip.trip.image?trip.trip.image:images[choice]} alt={trip.trip.name}></img>
            {trip.until>0 ? <p className='countdown'>In {trip.until} days</p>:<p className='countdown'>Past Trip</p>}
            </div>
            <div className='my_trips-right'>
                <TripOptions trip={trip} />
                <h3><Link to={`/trips/${trip.trip.id}/expenses`}>{trip.trip.name}</Link></h3>
                <div className='my-trips-details'>
                <p><i className="fa-solid fa-calendar-day"/> {new Date(trip.trip.start_date).toLocaleDateString()} - {new Date(trip.trip.end_date).toLocaleDateString()}</p>
                <p><i className="fa-solid fa-location-dot"/> {trip.trip.location[0]}, {trip.trip.location[1]}</p>
                </div>
                <div className='my-trips-expenses'>
                <p>{parseInt(trip.owe)<0 ? `You owe:$ ${-1*Number(trip.owe)}`: `You are owed:${trip.owe}` }</p> <p>You lent:${trip.lent} </p>
                </div>
                <div className='action-buttons'>
                <OpenModalButton
                     buttonText="Add Expense"
                     modalComponent={<AddExpenseForm trip={trip}/>}
                 />
                </div>
            </div>
            </div>


           ))}
        </div>
    )
}
export default AllTrips
