import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { deleteTrip,authenticate } from "../../store/session";


function DeleteModal({trip}) {
    const dispatch=useDispatch();
    const history=useHistory();
    const {closeModal} = useModal();

    const handleDelete =async (e) => {
        e.preventDefault();
        console.log(trip);
        dispatch(deleteTrip(trip.trip.id,trip.id)).then(closeModal).then(()=> dispatch(authenticate())).catch(res=>res);
        history.push('/trips')
    }

    return (
        <div className='delete-modal'>
            <h2>Delete Trip?</h2>
        <p>Once you delete a trip, it can't be restored. Are you sure you want to delete {trip.trip.name}?</p>
        <button onClick={handleDelete}>Delete</button>
        <button onClick={closeModal}>Cancel</button>
        </div>
    )
}
export default DeleteModal;
