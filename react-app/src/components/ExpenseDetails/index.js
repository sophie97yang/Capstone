import { useParams,Link } from "react-router-dom";
import { useSelector } from "react-redux";
import OpenModalButton from "../OpenModalButton";
import './ExpenseDetail.css'
import UpdateExpenseModal from "../UpdateExpenseModal";

function ExpenseDetail() {
    const {tripId,expenseId} = useParams();
    const user = useSelector(state=>state.session.user)
    // const [payerInvolved,setInvolve] = useState(false)
    const trip = user.trips[tripId]
    const expense = trip.trip.expenses.filter(expense=> expense.id===parseInt(expenseId))[0]
    console.log(trip,expense)
    //find payer expense detail
    const expense_details = [...expense.details]
    let payer_detail_index;
    for (let i=0;i<expense_details.length;i++) {
        let user = expense_details[i]
        if (user.user.id===expense.payer.id) {
            payer_detail_index= i
        }
    }
    const payer_detail = expense_details.splice(payer_detail_index,1)
    console.log(payer_detail,expense_details)
    const category_images = {
        "General":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/uncategorized/general@2x.png",
        "Transportation":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/transportation/other@2x.png",
        "Food and Drink":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@2x.png",
        "Entertainment":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@2x.png"
    }
    return (
        <div className='expense-details'>
           <h2> <Link to={`/trips/${trip.trip.id}/expenses`} className='breadcrumb'> {trip.trip.name}{'<'} </Link> Expense Details </h2>
           <div>
                <img src={category_images[expense.category]} alt={expense.category}></img>
                <h2>{expense.name}</h2>
                <h2>$ {expense.total.toFixed(2)}</h2>
                <p>Added by {expense.payer.first_name} {expense.payer.last_name[0]}. on {new Date(expense.expense_date).toLocaleDateString()}</p>
                <OpenModalButton
                modalComponent={<UpdateExpenseModal trip={trip} expense={expense}/>}
                buttonText='Edit Expense'/>

                <OpenModalButton
                buttonText='Delete Expense'/>
           </div>
           <div>
            <div>
            <img src='https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-teal22-100px.png' alt='profile' className='expense-profile'></img>
            {payer_detail.length ? `${payer_detail[0].user.first_name} paid $ ${expense.total.toFixed(2)} and owes $ ${payer_detail[0].price.toFixed(2)}`:
            `${payer_detail.user.first_name} paid $ ${expense.total.toFixed(2)}`}
            </div>
            {
                expense_details.map(user=> (
                    <div key={user.user.id}>
                        <img src='https://s3.amazonaws.com/splitwise/uploads/user/default_avatars/avatar-teal22-100px.png' alt='profile' className='expense-profile'></img>
                        <p>{`${user.user.first_name} owes $ ${user.price.toFixed(2)}`}</p>
                    </div>
                ))
            }
           </div>
        </div>
    )
}

export default ExpenseDetail
