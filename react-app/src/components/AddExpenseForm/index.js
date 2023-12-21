import {useState,useEffect} from 'react';
import {useDispatch} from 'react-redux';
import './AddExpense.css'
import { addExpense, authenticate } from '../../store/session';
import {useModal} from '../../context/Modal';
import {useHistory} from 'react-router-dom';
import logo from '../../assets/images/add-expense.png';
import InviteOthers from "../AllTripsPage/InviteOthersModal";
import OpenModalButton from "../OpenModalButton";


function AddExpenseForm ({trip}) {
    const dispatch = useDispatch();
    const history = useHistory();
    const [usersInvolved,setUsers] = useState(['All']);
    const [allUsers,setDefine] = useState(true);
    const [errors, setErrors] = useState([]);
    const [name, setName] = useState("");
    const [expenseDate, setExpenseDate] = useState("");
    // const [image,setImage] = useState(null);
    // const [imageLoading, setImageLoading] = useState(false);
    const [splitType, setSplitType] = useState('Equal');
    const [splitTypeInfo, setSplitTypeInfo] = useState({});
    const [category, setCategory] = useState('General');
    const [total, setTotal] = useState(0);
    const [checkSplit,setCheckSplit] = useState(0);
    const {closeModal} = useModal();

    const categories=['General','Food and Drink','Transportation','Entertainment']
    // console.log(splitTypeInfo,usersInvolved,checkSplit,total)

    useEffect(()=> {
        let totalAssigned=0
        Object.values(splitTypeInfo).forEach(val=> {
            if (!isNaN(parseInt(val))) totalAssigned+=Number(val)
        })
        setCheckSplit(totalAssigned.toFixed(2))
    },[splitTypeInfo])

    //reset checkSplit if user changes split type
    useEffect(()=> {
        setSplitTypeInfo({})
        setCheckSplit(0)
    },[splitType,allUsers])

    useEffect(()=> {
        setSplitTypeInfo({})
    },[usersInvolved])

    useEffect(()=> {
        setUsers(['All'])
    },[allUsers])

    const handleSubmit = async(e)=> {
        e.preventDefault();
        const errorsList={};
        if (!name) errorsList.name = 'Name is required'
        //check if expense date is given and  in between trip start and end date
        if (!expenseDate) errorsList.expenseDate = 'Date is required'
        if (new Date(expenseDate) < new Date(trip.trip.start_date) ||new Date(expenseDate) > new Date(trip.trip.end_date)  ) errorsList.expenseDate = 'Expense must be made during trip duration'
        //check if total is given and greater than 0
        if (total<=0) errorsList.total = 'You must expense more than 0 dollars'
        //if splittype is percentage and checksplit is !==100 error
        if (splitType==='Percentages' && checkSplit!=='100.00') errorsList.splitType = 'You must allocate all of your expense'
        //if splittype is exact and checksplit is !==total error
        if (splitType==='Exact' && checkSplit!==total) errorsList.splitType = 'You must allocate all of your expense'
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
            // console.log('trip',trip)
            // console.log('user-info',UsersInfoSend);
            // console.log('split-info',SplitTypeInfoSend)
            const data = await dispatch(addExpense(trip.trip.id,trip.id,name,expenseDate,splitType,SplitTypeInfoSend,category,total,UsersInfoSend))
            if (data) {
                setErrors(data);
                console.log(data);
                return;
            } else {
                dispatch(authenticate())
                history.push(`/trips/${trip.trip.id}/expenses`)
                closeModal();
            }
        }

    }

    return (
        <div className='add-expense-modal'>
             <button onClick={closeModal} className='close-modal' id='update-trip-close'><i className="fa-solid fa-xmark fa-2xl"></i></button>
            <div>
            <h2>Add an Expense.</h2>
            <img src={logo} alt='money-owl'></img>
            </div>
            <form className='add-expense-form'>
                {/* <h3>Split expenses with anyone and everyone...</h3> */}

                <div className='choosing-users'>
                <p>Who is involved?</p>
                <div className='keep-min'>
                <label id='users-checkbox'> All Users  </label>
                    <input
                        type='checkbox'
                        value={allUsers}
                        defaultChecked={true}
                        onChange={()=> setDefine(!allUsers)}
                        id='checkbox'
                    />
                </div>

               <div  className={!allUsers ?'user-choices' : 'user-choices hidden'}>
                {trip.trip.users.length>1 ?
                <>
                <label> Select Users: </label>
                    <select
                        multiple={true}
                        value={usersInvolved}
                        onChange={(e)=>{
                            const options = [...e.target.selectedOptions];
                            const values = options.map(option => option.value);
                            setUsers(values);
                        }}
                        id="multiple-users"
                        >
                        <option value={''} disabled className='disabled-option'>Select Users Below</option>
                       {trip.trip.users.map(user =>  (
                       <option value={[user.user.id,user.user.first_name]} key={user.user.id}>{user.user.first_name} {user.user.last_name[0]}.</option>
                       ))}
                    </select>
                </> :
                <div className="invite-collaborators-option">
                    <p>You look a little lonely.. </p>
                    <OpenModalButton
                    onItemClick={(e)=> e.preventDefault()}
                    modalComponent={<InviteOthers tripId={trip.id}/>}
                    buttonText="Click here to invite collaborators to your trip."/>
                </div>
                }
                </div>
                </div>

                <div>
                <label>
                    Name <span className='required'>*</span>
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
                    Expense Date <span className='required'>*</span></label>
                <input
                type="date"
                onChange={(e)=> setExpenseDate(e.target.value)}
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
                    Total: ($) <span className='required'>*</span>
                </label>
                <input
                type="number"
                onChange={(e)=> setTotal(Number(e.target.value).toFixed(2))}
                placeholder='$0.00'
                />
                {errors.total ? <p className='errors'>{errors.total}</p>: <p className='errors'></p>}
                </div>

                <div>
                <label>
                    Paid by you and split: <span className='required'>*</span>
                </label>
                <select value={splitType} onChange={(e) => setSplitType(e.target.value)}>
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
                        <div className="split-type-info">
                            <p>Split by Percentage</p>
                            {
                                allUsers ?
                                trip.trip.users.map(user =>  (
                                    <div className='info-details' key={user.user.id}>
                                        <label  >
                                            {user.user.first_name}
                                        </label>
                                            <input
                                            type='number'
                                            min={0}
                                            onChange={(e)=> {
                                                const newInfo={...splitTypeInfo}
                                                newInfo[user.user.id]=e.target.value
                                                setSplitTypeInfo(newInfo)
                                            }}/>
                                    </div>

                                )):
                                usersInvolved.map(user =>  (
                                <div className='info-details'  key={user.split(',')[0]}>
                                    <label >
                                        {user.split(',')[1]}
                                    </label>
                                        <input
                                        type='number'
                                        min={0}
                                        onChange={(e)=> {
                                            const newInfo={...splitTypeInfo}
                                            newInfo[parseInt(user.split(',')[0])]=e.target.value
                                            setSplitTypeInfo(newInfo)
                                        }}/>
                                </div>
                            ))
                            }
                            <p>Total: {checkSplit}% </p>
                            <p> {100-checkSplit}% left </p>
                            {errors.checkSplit ? <p className='errors'>{errors.checkSplit}</p>: <p className='errors'></p>}
                            {errors.splitTypeError ? <p className='errors'>{errors.splitTypeError}</p>: <p className='errors'></p>}
                        </div>
                    )
                }

                {splitType==='Exact' && (
                        <div className="split-type-info">
                            <p>Split by Exact Amounts</p>
                            {
                                allUsers ?
                                trip.trip.users.map(user =>  (
                                    <div key={user.user.id}  className='info-details' >
                                        <label>
                                            {user.user.first_name}
                                        </label>
                                            <input
                                            type='number'
                                            step={0.01}
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
                                    </label>
                                        <input
                                        type='number'
                                        step={0.01}
                                        onChange={(e)=> {
                                            const newInfo={...splitTypeInfo}
                                            newInfo[parseInt(user.split(',')[0])]=e.target.value
                                            setSplitTypeInfo(newInfo)
                                        }}/>
                                    </div>

                            ))
                            }
                            <p>Total: ${checkSplit} </p>
                            <p> ${(total-checkSplit).toFixed(2)} left </p>
                            {errors.checkSplit ? <p className='errors'>{errors.checkSplit}</p>: <p className='errors'></p>}
                            {errors.splitTypeError ? <p className='errors'>{errors.splitTypeError}</p>: <p className='errors'></p>}
                        </div>
                    )
                        }


                <p>{splitType==='Equal' ? <>{allUsers ? `$ ${(total/trip.trip.users.length).toFixed(2)} per person`:  `$ ${(total/usersInvolved.length).toFixed(2)} per person`}</>
                : ''}</p>

            <div id='expense-action-buttons'>
            <button onClick={e=> {
              e.preventDefault();
              closeModal()
            }}
            id='cancel-button'
            >Cancel</button>
            <button onClick={handleSubmit} id='save-button'>Save</button>
            </div>

            </form>
        </div>
    )
}

export default AddExpenseForm
