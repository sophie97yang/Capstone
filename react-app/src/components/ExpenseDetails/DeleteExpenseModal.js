import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { deleteExpense,authenticate } from "../../store/session";

function DeleteExpense({trip,expense}) {
    const dispatch=useDispatch();
    const history=useHistory();
    const {closeModal} = useModal();

    const handleDelete = (e) => {
        e.preventDefault();
        dispatch(deleteExpense(trip.id,expense.id)).then(closeModal).catch(res=>res);
        dispatch(authenticate());
        history.push(`/trips/${trip.trip.id}/expenses`)

    }

    return (
        <div className='delete-modal'>
            <h2>Delete Expense?</h2>
        <p>Once you delete an expense, it can't be restored. Are you sure you want to delete {expense.name}?</p>
        <button onClick={handleDelete}>Delete</button>
        <button onClick={closeModal}>Cancel</button>
        </div>
    )

}

export default DeleteExpense
