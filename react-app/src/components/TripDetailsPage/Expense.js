import {useSelector} from 'react-redux';
import OpenModalButton from '../OpenModalButton';
import AddExpenseForm from '../AddExpenseForm';
import { Link } from 'react-router-dom';

const Expense = ({trip}) => {
    const user = useSelector(state=>state.session.user)
    const user_expense_detail = {};
    //images to display depending on expense category
    const category_images = {
        "General":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/uncategorized/general@2x.png",
        "Transportation":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/transportation/other@2x.png",
        "Food and Drink":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/food-and-drink/other@2x.png",
        "Entertainment":"https://s3.amazonaws.com/splitwise/uploads/category/icon/square_v2/entertainment/other@2x.png"
    }
    //organize expenses by timeframe - year and month
    const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
    ];
    const expense_by_year = {}
    trip.trip.expenses.forEach(expense => {
        const year = new Date(expense.expense_date).getFullYear()
        const month = monthNames[new Date(expense.expense_date).getMonth()]
        if (!(year in expense_by_year)) {
            const expense_by_month = {}
            if (!(month in expense_by_month)) {
                expense_by_month[month]=[expense]
            } else {
                expense_by_month[month] = [...expense_by_month[month],expense]
            }
            expense_by_year[year] = expense_by_month
        } else {
            const yearly_expenses = expense_by_year[year]
            if (!(month in yearly_expenses)) {
                yearly_expenses[month]=[expense]
            } else {
                yearly_expenses[month] = [...yearly_expenses[month],expense]
             }
        }
        //filter out expense detail relavent to user
        user_expense_detail[expense.id]=expense.details.filter(detail => detail.user.id===user.id)[0]
    })

    console.log(expense_by_year)
    console.log(user_expense_detail)


    return (
        <div className='expense-overview'>
            <div className='expense-action-buttons'>
            <OpenModalButton
                     buttonText="Add Expense"
                     modalComponent={<AddExpenseForm trip={trip}/>}
                 />
            <button>Settle Up</button>
            </div>

            {
                Object.keys(expense_by_year).map(year => (
                    <div key={year} className='yearly_expenses'>
                        <h4>{year}</h4>
                        {
                             Object.keys(expense_by_year[year]).map(month => (
                                <div key={month} className='monthly_expenses'>
                                <h4>{month}</h4>
                                {
                                    expense_by_year[year][month].map(expense => (
                                        <div key={expense.id} className='expense-detail'>
                                            <p>{month} {new Date(expense.expense_date).getDate()}</p>
                                            <img src={category_images[expense.category]} alt={expense.category}></img>
                                            <h4><Link to={`/trips/${trip.id}/expenses/${expense.id}`}>{expense.name}</Link></h4>


                                            <div>
                                            {user.id===expense.payer.id ? <p> You paid </p> : <p>{expense.payer.first_name} {expense.payer.last_name} paid</p>}
                                            <p>$ {expense.total.toFixed(2)}</p>
                                            </div>


                                         <div>
                                           {user.id===expense.payer.id ? <p> You lent </p> : <>{ user_expense_detail[expense.id] ? <p>{expense.payer.first_name} lent</p>: 'not involved' }</>}

                                           {user.id===expense.payer.id ? <p>{user_expense_detail[expense.id] ? `$ ${(expense.total-user_expense_detail[expense.id].price).toFixed(2)}`: `$ ${expense.total.toFixed(2)}`}</p>
                                           : <p>{user_expense_detail[expense.id] ? `$ ${user_expense_detail[expense.id].price.toFixed(2)}`:''}</p>}
                                           </div>
                                        </div>
                                    ))
                                }
                                </div>
                             ))
                        }
                    </div>
                ))
            }

        </div>
    )
}

export default Expense
