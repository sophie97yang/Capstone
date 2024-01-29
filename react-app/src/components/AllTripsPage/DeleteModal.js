import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { deleteTrip,authenticate } from "../../store/session";
import logo from '../../assets/images/delete.png'


function DeleteModal({trip}) {
    const dispatch=useDispatch();
    const history=useHistory();
    const {closeModal} = useModal();

    const handleDelete =async (e) => {
        e.preventDefault();
        dispatch(deleteTrip(trip.trip.id,trip.id)).then(closeModal).then(()=> dispatch(authenticate())).catch(res=>res);
        history.push('/trips')
    }

    return (
        <div className='delete-modal'>
             <button onClick={closeModal} className='close-modal' id='update-trip-close'><i className="fa-solid fa-xmark fa-2xl"></i></button>
            <h2>Delete Trip?</h2>
            <img src={logo} alt='owl-trash'></img>
        <p>Once you delete a trip, it can't be restored.</p>
        <p>Are you sure you want to delete {trip.trip.name}?</p>
        <div className='delete-action-buttons'>
        <button onClick={closeModal}  class='cancel-expense'>Cancel</button>
        <button onClick={handleDelete} className='delete-expense'>Delete</button>
        </div>
        </div>
    )
}
export default DeleteModal;
