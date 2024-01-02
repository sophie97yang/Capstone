import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { deleteExpense,authenticate } from "../../store/session";
import logo from '../../assets/images/delete.png'

function DeleteExpense({trip,expense}) {
    const dispatch=useDispatch();
    const history=useHistory();
    const {closeModal} = useModal();

    const handleDelete = (e) => {
        e.preventDefault();
        const response = dispatch(deleteExpense(trip.id,expense.id)).then(res=> {
            closeModal();
            console.log(res)
        }).catch(res=>res);
        dispatch(authenticate());
        history.push(`/trips/${trip.trip.id}/expenses`)

    }

    return (
        <div className='delete-modal'>
             <button onClick={closeModal} className='close-modal' id='update-trip-close'><i className="fa-solid fa-xmark fa-2xl"></i></button>
            <h2>Delete Expense?</h2>
            <img src={logo} alt='owl-trash'></img>
        <p>Once you delete an expense, it can't be restored.</p>
        <p>Are you sure you want to delete {expense.name}?</p>
        <div className='delete-action-buttons'>
        <button onClick={handleDelete} className='delete-expense'>Delete</button>
        <button onClick={closeModal} className='cancel-expense'>Cancel</button>
        </div>
        </div>
    )

}

export default DeleteExpense
