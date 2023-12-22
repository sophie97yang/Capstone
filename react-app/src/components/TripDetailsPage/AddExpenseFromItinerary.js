import {useState,useEffect} from 'react';
import {useDispatch} from 'react-redux';
import '../AddExpenseForm/AddExpense.css'
import { ExpenseItinerary, addExpense, authenticate} from '../../store/session';
import {useModal} from '../../context/Modal';
import {useHistory} from 'react-router-dom';
import "../UpdateExpenseModal/UpdateExpense.css"
import logo from '../../assets/images/add-expense.png'

function AddExpenseFromItinerary ({trip,booking}) {
    const booking_category_maps = {"Hotel":"Transportation","Things To Do":"Entertainment","Restaurants":"Food and Drink"}
    const dispatch = useDispatch();
    const history = useHistory();

    const [usersInvolved,setUsers] = useState(['All']);
    const [allUsers,setDefine] = useState(true);
    const [errors, setErrors] = useState([]);
    const [name, setName] = useState(booking.booking.name.slice(0,40));
    const options={}
    options.timeZone = "UTC";
    const [expenseDate, setExpenseDate] = useState(new Date(booking.booking_date).toLocaleDateString('en-CA',options));
    const [splitType, setSplitType] = useState('Equal');
    const [splitTypeInfo, setSplitTypeInfo] = useState({});
    const [category, setCategory] = useState(booking_category_maps[booking.booking.category]);
    const [total, setTotal] = useState(booking.total);
    const [checkSplit,setCheckSplit] = useState(0);
    const {closeModal} = useModal();

    const categories=['General','Food and Drink','Transportation','Entertainment']

    //anytime that splittypeinfo changes (user inputs prices for the splits), compare to the total
    useEffect(()=> {
        let totalAssigned=0
        if (splitTypeInfo) {
            Object.values(splitTypeInfo).forEach(val=> {
            if (!isNaN(parseInt(val))) totalAssigned+=Number(val)
        })
        setCheckSplit(totalAssigned.toFixed(2))}
    },[splitTypeInfo])

    //if user toggles between all users and not, make sure to reset users involved accordingly
    useEffect(()=> {
        if (allUsers) setUsers(['All'])
    },[allUsers])

    const handleSubmit = async(e)=> {
        e.preventDefault();
        const errorsList={};
        if (!name) errorsList.name = 'Name is required'
        //check if expense date is given and  in between trip start and end date
        if (!expenseDate) errorsList.expenseDate = 'Date is required'
        //check if total is given and greater than 0
        if (total<=0) errorsList.total = 'You must expense more than 0 dollars'
        //if splittype is percentage and checksplit is !==100 error
        if (splitType==='Percentages' && checkSplit!=='100.00') errorsList.splitType = 'You must allocate all of your expense'
        //if splittype is exact and checksplit is !==total error
        if (splitType==='Exact' && checkSplit!==parseInt(total).toFixed(2)) errorsList.splitType = 'You must allocate all of your expense'
        //usersinvolved does not match up with splittype info throw error
        if (usersInvolved[0]==='All' && splitType!=='Equal' && Object.values(splitTypeInfo).length!==trip.trip.users.length) errorsList.checkSplit = 'You must allocate your expense to all people involved.'
        if (usersInvolved[0]!=='All' && splitType!=='Equal' && Object.values(splitTypeInfo).length!==usersInvolved.length) errorsList.checkSplit = 'You must allocate your expense to all people involved.'
        //no inputs for splits can be negative
        if (splitTypeInfo) {
        Object.values(splitTypeInfo).forEach(val=> {
            if (Number(val)<=0) errorsList.splitTypeError = 'Expense allocated must be greater than $0.00'
        })
    }
        if (Object.values(errorsList).length) {
            setErrors(errorsList);
            return;

        } else {
            setErrors({})
            //rework data to be ready to send
            let UsersInfoSend='All'
            let SplitTypeInfoSend=null;
            if (usersInvolved[0]!=='All') {
            const users = {}
            usersInvolved.forEach(user => {
                                users[user.split(',')[0]]=user.split(',')[1]
                            })

            UsersInfoSend = Object.keys(users).join(',')
            if (splitType!=='Equal') SplitTypeInfoSend = Object.values(splitTypeInfo).join(',')
            } else {
                if (splitType!=='Equal') SplitTypeInfoSend = Object.values(splitTypeInfo).join(',')
            }
            const data = await dispatch(addExpense(trip.trip.id,trip.id,name,expenseDate,splitType,SplitTypeInfoSend,category,total,UsersInfoSend))

            if (data.errors) {
                setErrors(data.errors);
                console.log(data.errors);
                return;
            } else {
                const expense=data;
                await dispatch(ExpenseItinerary(trip.id,trip.trip.id,booking.id,expense.id))
                dispatch(authenticate())
                history.push(`/trips/${trip.trip.id}/expenses`)
                closeModal();
            }
        }

    }

    return (
        <div className='update-expense-modal'>
             <button onClick={closeModal} className='close-modal' id='update-trip-close'><i className="fa-solid fa-xmark fa-2xl"></i></button>
            <div>
            <h2>Add an Expense</h2>
            <img src={logo} alt='money-owl'></img>
            </div>
            <form className='add-expense-form'>
                <div className='choosing-users'>
                <p>Who is Involved?</p>
                <div className='keep-min'>
                <label > All Users </label>

                    <input
                        type='checkbox'
                        value={allUsers}
                        defaultChecked={allUsers}
                        onChange={()=> {
                            setDefine(!allUsers)
                            setSplitTypeInfo({})
                            setCheckSplit(0)
                        }}
                        id='checkbox'
                    />
                </div>


                <div  className={!allUsers ?'user-choices' : 'user-choices hidden'}>
                <label className='select-users'> Select Users: </label>
                    <select
                        multiple={true}
                        value={usersInvolved}
                        onChange={(e)=>{
                            const options = [...e.target.selectedOptions];
                            const values = options.map(option => option.value);
                            setUsers(values);
                            setSplitTypeInfo({})
                        }}
                        id="multiple-users"
                        >
                        <option value={''} disabled className='disabled-option'>Select Users Below</option>
                       {trip.trip.users.map(user =>  (
                       <option value={[user.user.id,user.user.first_name]} key={user.user.id}>{user.user.first_name} {user.user.last_name[0]}.</option>
                       ))}
                    </select>
                </div>
                </div>

               <div>
                <label>
                    Name
                </label>
                <input
                type="text"
                placeholder="ex. Uber to airport"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className=""
              />
              {errors.name ? <p className='errors'>{errors.name}</p>: <p className='errors'></p>}
              </div>

                <div>
                <label>
                    Expense Date
                </label>
                <input
                type="date"
                onChange={(e)=> setExpenseDate(e.target.value)}
                value={expenseDate}
                />
                {errors.expenseDate ? <p className='errors'>{errors.expenseDate}</p>: <p className='errors'></p>}
                </div>

                <div>
                <label>
                    Category
                </label>
                <select value={category} onChange={(e) => setCategory(e.target.value)}>
                    {categories.map(cat => (
                        <option value={cat} key={cat}>
                            {cat}
                        </option>
                    ))}
                </select>
                <p className='errors'></p>
                </div>


                <div>
                <label>
                    Total: ($)
                </label>
                <input
                type="number"
                onChange={(e)=> setTotal(Number(e.target.value))}
                value={total.toFixed(2)}
                />
                {errors.total ? <p className='errors'>{errors.total}</p>: <p className='errors'></p>}
                </div>

                <div>
                <label>
                    Paid by you and split:
                </label>
                <select value={splitType} onChange={(e) =>{
                    setSplitType(e.target.value)
                    setSplitTypeInfo({})
                    setCheckSplit(0)
                    }}>
                    <option value='Equal'>
                        Equally
                    </option>

                    <option value='Percentages'>
                        By Percentage
                    </option>

                    <option value='Exact'>
                        Exact Amount
                    </option>
                </select>
                {errors.splitType ? <p className='errors'>{errors.splitType}</p>: <p className='errors'></p>}
                </div>

                {splitType==='Percentages' && (
                        <div className="split-type-info" id='update-split-type-info'>
                            <p className='split-type'>Split by Percentage</p>
                            {
                                allUsers ?
                                trip.trip.users.map(user =>  (
                                    <div className='info-details' key={user.user.id}>
                                        <label>
                                            {user.user.first_name}
                                        </label>
                                            <input
                                            type='number'
                                            min={0}
                                            value={splitTypeInfo[user.user.id]}
                                            onChange={(e)=> {
                                                const newInfo={...splitTypeInfo}
                                                newInfo[user.user.id]=e.target.value
                                                setSplitTypeInfo(newInfo)
                                            }}/>

                                    </div>
                                )):
                                usersInvolved.map(user =>  (
                                    <div key={user.split(',')[0]} className='info-details'>
                                    <label  >
                                        {user.split(',')[1]}
                                        <input
                                        type='number'
                                        min={0}
                                        value={splitTypeInfo[parseInt(user.split(',')[0])]}
                                        onChange={(e)=> {
                                            const newInfo={...splitTypeInfo}
                                            newInfo[parseInt(user.split(',')[0])]=e.target.value
                                            setSplitTypeInfo(newInfo)
                                        }}/>
                                    </label>
                                    </div>
                            ))
                            }
                            <div id='split-info-details'>
                            <p>Total: {checkSplit}% </p>
                            <p> {100-checkSplit}% left </p>
                            </div>
                            {errors.checkSplit ? <p className='errors'>{errors.checkSplit}</p>: <p className='errors'></p>}
                            {errors.splitTypeError ? <p className='errors'>{errors.splitTypeError}</p>: <p className='errors'></p>}
                        </div>
                    )
                }

                {splitType==='Exact' && (
                        <div className="split-type-info" id='update-split-type-info'>
                            <p className='split-type'>Split by Exact Amounts</p>
                            {
                                allUsers ?
                                trip.trip.users.map(user =>  (
                                    <div key={user.user.id} className='info-details'>
                                        <label  >
                                            {user.user.first_name}
                                            <input
                                            type='number'
                                            step={0.01}
                                            value={splitTypeInfo[user.user.id]}
                                            onChange={(e)=> {
                                                const newInfo={...splitTypeInfo}
                                                newInfo[user.user.id]=e.target.value
                                                setSplitTypeInfo(newInfo)
                                            }}/>
                                        </label>
                                    </div>
                                )):
                                usersInvolved.map(user =>  (
                                    <div key={user.split(',')[0]} className='info-details'>
                                    <label  >
                                        {user.split(',')[1]}
                                        <input
                                        type='number'
                                        step={0.01}
                                        value={splitTypeInfo[parseInt(user.split(',')[0])]}
                                        onChange={(e)=> {
                                            const newInfo={...splitTypeInfo}
                                            newInfo[parseInt(user.split(',')[0])]=e.target.value
                                            setSplitTypeInfo(newInfo)
                                        }}/>
                                    </label>
                                    </div>
                            ))
                            }
                            <div id='split-info-details'>
                            <p>Total: ${checkSplit} </p>
                            <p> ${(total-checkSplit).toFixed(2)} left </p>
                            </div>
                            {errors.checkSplit ? <p className='errors'>{errors.checkSplit}</p>: <p className='errors'></p>}
                            {errors.splitTypeError ? <p className='errors'>{errors.splitTypeError}</p>: <p className='errors'></p>}
                        </div>
                    )
                        }


                <p className='owe-details'>{splitType==='Equal' ? <>{allUsers ? `$ ${(total/trip.trip.users.length).toFixed(2)} per person`:  `$ ${(total/usersInvolved.length).toFixed(2)} per person`}</>
                : ''}</p>

                <div id='update-expense-action-buttons'>
                <button onClick={handleSubmit}
                id='update-save-button'
                >Save</button>
                <button onClick={(e=> {
                    e.preventDefault();
                    closeModal()})}
                    id='update-cancel-button'
                    >Cancel</button>
                </div>

            </form>
        </div>
    )
}

export default AddExpenseFromItinerary;
