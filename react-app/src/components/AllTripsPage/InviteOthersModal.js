import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import {authenticate,addUsers } from "../../store/session";
import { useState } from "react";


function InviteOthers({tripId}) {
    const dispatch=useDispatch();
    const history=useHistory();
    const [email1,setEmail1] = useState('')
    const [email2,setEmail2] = useState('')
    const [email3,setEmail3] = useState('')
    const [error,setError] = useState({})
    const [hasSubmitted,setSubmitted]=useState(false)
    const user = useSelector(state=>state.session.user)
    console.log(user)
    console.log(tripId)

    const {closeModal} = useModal();

    const trip = user.trips[tripId]
    console.log(trip)

    //if user with email isn't found, no action is made
    const handleSubmit =async (e) => {
        e.preventDefault();
        setSubmitted(false)
        if (!email1) {
            setError({'email1':'Invite at least one collaborator'});
            return
        } else {
        const res=dispatch(addUsers(trip.trip.id,trip.id,email1,email2,email3)).catch(res=>res);
        if (res.errors) {
            return ['Error adding users']
        } else {
            await dispatch(authenticate());
            setSubmitted(true);
            setEmail1('')
            setEmail2('')
            setEmail2('')
        }
    }
    }

    return (
        <div className='invite-modal'>
            <button onClick={closeModal}><i className="fa-solid fa-xmark"></i></button>
            <h2>Trip collaboration</h2>
            <h4><i className="fa-solid fa-user-plus"/>Invite Collaborators</h4>
        <p>Add at least one email to invite collaborators. Anyone who is invited can edit and add to your trip.</p>
        <form>
        <label>Add Collaborator:
            <input
            type='email'
            value={email1}
            onChange={(e)=> {
                setEmail1(e.target.value)
            }}
            />
            {error.email1 ? <p className='errors'>{error.email1}</p>: <p className='errors'></p>}
        </label>

        <label>Add Collaborator:
            <input
            type='email'
            value={email2}
            onChange={(e)=> {setEmail2(e.target.value)}}
            />
        </label>

        <label>Add Collaborator:
            <input
            type='email'
            value={email3}
            onChange={(e)=> {setEmail3(e.target.value)}}
            />
        </label>
            <button onClick={handleSubmit}>Invite</button>
        </form>

        {hasSubmitted ? <p className='success'>Collaborators successfully added. If user added does not have a SplitTrip account, they will have to Sign Up first. <button onClick={(e)=>
        {
            e.preventDefault();
            history.push(`/trips/${trip.trip.id}/expenses`)
            dispatch(authenticate());
            closeModal()
        }}>Go to {trip.trip.name}</button></p>: <p className='success'></p>}

        <div>
            <h3>Collaborators</h3>
            {trip.trip.users.map(user =>(
                <li className="collaborators-detail" key={user.user.id}>
                   <p> {user.user.first_name} {user.user.last_name[0]} </p>
                   <p> {user.user.id===trip.user_id && trip.creator ? 'Owner': 'Can Edit'}</p>

                </li>
            ))}
        </div>

        </div>
    )
}
export default InviteOthers;
