import {useEffect, useState} from 'react';
import { useSelector } from "react-redux";
import { useHistory,Link } from "react-router-dom";
import './AllTrips.css'
import TripOptions from "./TripOptions";
import OpenModalButton from "../OpenModalButton";
import AddExpenseForm from "../AddExpenseForm"

const AllTrips = () => {
    const user = useSelector(state=>state.session.user);
    const history=useHistory();
    const [imageChoice,setImageChoice] = useState();
    const trips =user?.trips ? Object.values(user?.trips):null;
    const locations = [{city:'Aspen',state:'CO',image:"https://www.travelandleisure.com/thmb/Yiq3rXHGmHnDrgzBsGmEvqjHxSo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/aspen-colorado-lead-ASPENTG0122-3bd432152d1f4758b1b89fd8a3a231cc.jpg"},
    {city:'Miami',state:'FL',image:'https://www.mayflower.com/wp-content/uploads/2022/05/Miami-City-Guide_Header-scaled.jpg'},
    {city:'Napa',state:'CA',image:"https://falstaff.b-cdn.net/core/5039223/napa-valley_5039223.jpg"},
    {city:'Boston',state:'MA',image:"https://content.r9cdn.net/rimg/dimg/8d/d4/5837febe-city-25588-16b90081d43.jpg"},
    {city:'Jackson',state:'WY',image:"https://assets.vogue.com/photos/61d453c3069d2a61c3d376e1/master/w_2560%2Cc_limit/520395534"},
    {city:'Nashville',state:'TN',image:"https://i.natgeofe.com/n/070fbe2c-a644-4c62-aa76-bddf63dd6f10/broadway-record-shop-nashville-tennessee.jpg"},
    {city:'Washington',state:'DC',image:"https://www.thoughtco.com/thmb/_ZNhs9lhwfoos1WoYBygoL03g6c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-497322993-598b2ad403f4020010ae0a08.jpg"},
    {city:'Las Vegas',state:'NV',image:"https://media.cnn.com/api/v1/images/stellar/prod/180313182911-01-las-vegas-travel-strip.jpg"},
    ]
    const location_choice = Math.floor(Math.random()*locations.length)

    //calculate how many days until the trip
    trips?.forEach(trip=> {
        const today = new Date()
        const start = new Date(trip.trip.start_date)
        trip.until = Math.ceil((start.getTime()-today.getTime())/(1000*60*60*24))
        if (trip.until<0 && today<new Date(trip.trip.end_date)) trip.until='current'
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

    useEffect(()=> {
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
    const choice = Math.floor(Math.random()*images.length);
    if (!imageChoice) setImageChoice(choice);
    },[imageChoice])

    const options={}
    options.timeZone = "UTC";

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
                    history.push(`/explore/${locations[location_choice].city}`)
                }}>Explore places to go</button>
            </div>
           { trips.length ? trips.sort((obj1,obj2)=>new Date(obj1.trip.start_date)-new Date(obj2.trip.start_date)).map(trip=> (
            <div key={trip.id} className='individual-trip'>
            <div className='my_trips-left'>
            <img src={trip.trip.image?trip.trip.image:imageChoice} alt={trip.trip.name}
            onError={e => { e.currentTarget.src = "https://images.unsplash.com/photo-1522878129833-838a904a0e9e?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" }}
            ></img>
            {trip.until>=0 ? <p className='countdown'>In {trip.until} days</p>:<p className='countdown'><span> {trip.until==='current' ? "Happening Now" :"Past Trip"}</span></p>}
            </div>
            <div className='my_trips-right'>
                <TripOptions trip={trip} />
                <h3><Link to={`/trips/${trip.trip.id}/expenses`}>{trip.trip.name}</Link></h3>
                <div className='my-trips-details'>
                <p><i className="fa-solid fa-calendar-day"/> {new Date(trip.trip.start_date).toLocaleDateString('en-US',options)} - {new Date(trip.trip.end_date).toLocaleDateString('en-US',options)}</p>
                <p><i className="fa-solid fa-location-dot"/> {trip.trip.location[0]}, {trip.trip.location[1]}</p>
                </div>
                <div className='my-trips-expenses'>
                <p>{parseInt(trip.owe)<=0 ? <span className='owe'>{`You owe: $${(-1*Number(trip.owe)).toFixed(2)}`}</span>: <span className='owed'>{`You are owed: $${Number(trip.owe).toFixed(2)}`}</span> }</p>
                <p>You lent: ${trip.lent} </p>
                </div>
                <div className='action-buttons'>
                <OpenModalButton
                     buttonText="Add Expense"
                     modalComponent={<AddExpenseForm trip={trip}/>}
                 />
                </div>
            </div>
            </div>


           )) :
           <div className='no-trips'>
            <p>
                It seems you haven't joined or created any trips yet.
                Don't miss out on the adventure -
                Create a trip, invite friends, and let the planning begin. Your next unforgettable experience awaits, and it all begins with a single click.
            </p>

           </div>}
        </div>
    )
}
export default AllTrips
