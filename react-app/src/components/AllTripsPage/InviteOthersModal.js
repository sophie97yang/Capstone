import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import {authenticate,addUsers } from "../../store/session";
import { useState } from "react";
import logo from '../../assets/images/invite-others.png'


function InviteOthers({tripId}) {
    const dispatch=useDispatch();
    const history=useHistory();
    const [email1,setEmail1] = useState('')
    const [email2,setEmail2] = useState('')
    const [email3,setEmail3] = useState('')
    const [error,setError] = useState({})
    const [hasSubmitted,setSubmitted]=useState(false)
    const user = useSelector(state=>state.session.user)

    const {closeModal} = useModal();

    const trip = user.trips[tripId]


    //if user with email isn't found, no action is made
    const handleSubmit =async (e) => {
        e.preventDefault();
        setSubmitted(false)
        if (!email1) {
            setError({'email1':'Invite at least one collaborator'});
            return
        } else {
        const res=await dispatch(addUsers(trip.trip.id,trip.id,email1,email2,email3));
        if (res.errors) {
            setError({"email":`${res.errors}`})
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

    console.log(error)
    return (
        <div className='invite-modal'>
            <button onClick={closeModal} className='close-modal'><i className="fa-solid fa-xmark fa-2xl"></i></button>
            <div className='invite-modal-top'>
            <div className='invite-left'>
            <h2>Trip collaboration</h2>
            <img src={logo} alt='two-owls'></img>
            </div>

            <div className='invite-right'>
            <h3><i className="fa-solid fa-user-plus"/> Invite Collaborators</h3>
            <p>Add at least one email to invite collaborators. Anyone who is invited can edit and add to your trip.</p>
            </div>

            </div>

        <form className="invite-modal-form">
            <div id="collaborator-one">
        <label>Add Collaborator:</label>
            <input
            type='email'
            value={email1}
            onChange={(e)=> {
                setEmail1(e.target.value)
            }}
            />
            {error.email1 ? <p className='errors'>{error.email1}</p>: <p className='errors'></p>}
            </div>
            {/* <span className='required'>*</span> */}

            <div>
        <label>Add Collaborator: </label>
            <input
            type='email'
            value={email2}
            onChange={(e)=> {setEmail2(e.target.value)}}
            />
            </div>

        <div>
        <label>Add Collaborator: </label>
            <input
            type='email'
            value={email3}
            onChange={(e)=> {setEmail3(e.target.value)}}
            />
            </div>

            <button onClick={handleSubmit} className="action-button-io">Invite</button>
            {error.email ? <p className='errors'>{error.email}</p>: <p className='errors'></p>}
        </form>

        {hasSubmitted ? <p className='success'>Collaborators successfully added. If user added does not have a SplitTrip account, they will have to sign up first. <button onClick={(e)=>
        {
            e.preventDefault();
            history.push(`/trips/${trip.trip.id}/expenses`)
            dispatch(authenticate());
            closeModal()
        }}>Go to {trip.trip.name} </button></p>: <p className='success' id='hidden'></p>}

        <div className="collaborators">
            <h3> <i className="fa-solid fa-users"></i> Current Collaborators</h3>
            {trip.trip.users.map(user =>(
                <li className="collaborators-detail" key={user.user.id}>
                   <p className="user-collaborator"> {user.user.first_name} {user.user.last_name[0]}. : </p>
                    {user.user.id===trip.user_id && trip.creator ? <p className='owner'> Owner</p>: <p className='editor'> Can Edit</p>}

                </li>
            ))}
        </div>

        </div>
    )
}
export default InviteOthers;
