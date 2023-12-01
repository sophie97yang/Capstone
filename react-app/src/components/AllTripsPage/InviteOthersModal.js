import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import {authenticate,addUsers } from "../../store/session";
import { useState } from "react";


function InviteOthers({trip}) {
    const dispatch=useDispatch();
    const history=useHistory();
    const [email1,setEmail1] = useState('')
    const [email2,setEmail2] = useState('')
    const [email3,setEmail3] = useState('')
    const [error,setError] = useState({})
    const [hasSubmitted,setSubmitted]=useState(false)

    const {closeModal} = useModal();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!email1) {
            setError({'email1':'Invite at least one collaborator'});
            return
        } else {
        const res=dispatch(addUsers(trip.trip.id,trip.id,email1,email2,email3)).catch(res=>res);
        if (res.errors) {
            return ['Error adding users']
        } else {
            dispatch(authenticate());
            setSubmitted(true);
        }
    }
    }

    return (
        <div className='invite-modal'>
            <h2>Trip collaboration</h2>
            <h4><i className="fa-solid fa-user-plus"/>Invite Collaborators</h4>
        <p>Add at least one email to invite collaborators. Anyone who is invited can edit and add to your trip.</p>
        <form>
        <label>Add Collaborator:
            <input
            type='email'
            value={email1}
            onChange={(e)=> {setEmail1(e.target.value)}}
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

        {hasSubmitted ? <p className='success'>Collaborators successfully added. <button onClick={(e)=>
        {
            e.preventDefault();
            history.push('/trips')
            closeModal()
        }}>Go to your trips</button></p>: <p className='success'></p>}

        <div>
            <h3>Collaborators</h3>
            {trip.trip.users.map(user =>(
                <li className="collaborators-detail" key={user.user.id}>
                   <p> {user.user.first_name} {user.user.last_name[0]} </p>
                   <p> {user.user.id==trip.user_id && trip.creator ? 'Owner': 'Can Edit'}</p>

                </li>
            ))}
        </div>

        </div>
    )
}
export default InviteOthers;
