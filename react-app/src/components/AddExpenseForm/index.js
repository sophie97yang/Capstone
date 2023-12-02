import {useState,useEffect} from 'react';
import './AddExpense.css'

function AddExpenseForm ({trip}) {
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

    const categories=['General','Food and Drink','Transportation','Entertainment']
    console.log(splitTypeInfo,usersInvolved)

    useEffect(()=> {
        let totalAssigned=0
        Object.values(splitTypeInfo).forEach(val=> {
            if (!isNaN(parseInt(val))) totalAssigned+=parseInt(val)
        })
        setCheckSplit(totalAssigned)
    },[splitTypeInfo])

    //reset checkSplit if user changes split type
    useEffect(()=> {
        setSplitTypeInfo({})
        setCheckSplit(0)
    },[splitType,allUsers])

    const handleSubmit = async(e)=> {
        e.preventDefault();
        const errorsList={};
        if (!name) errorsList.name = 'Name is required'
        //check if expense date is given and  in between trip start and end date
        //check if total is given and greater than 0
        //if splittype is percentage and checksplit is !==100 error
        //if splittype is exact and checksplit is !==total error
        //usersinvolved does not match up with splittype info throw error

    }

    return (
        <div className='add-expense-modal'>
            <h2>Add an Expense</h2>
            <form className='add-expense-form'>
                <p>With you and:</p>
                <label className='keep-min'> All Users
                    <input
                        type='checkbox'
                        value={allUsers}
                        defaultChecked={true}
                        onChange={()=> setDefine(!allUsers)}
                    />
                </label>

                <label className={!allUsers ?'user-choice' : 'user-choices hidden'}> Select Users:
                    <select
                        multiple={true}
                        value={usersInvolved}
                        onChange={(e)=>{
                            const options = [...e.target.selectedOptions];
                            const values = options.map(option => option.value);
                            setUsers(values);
                        }}
                        >
                        <option value={''}>Select Users Below</option>
                       {trip.trip.users.map(user =>  (
                       <option value={[user.user.id,user.user.first_name]} key={user.user.id}>{user.user.first_name}</option>
                       ))}
                    </select>
                </label>

                <label>
                    Name
                <input
                type="text"
                placeholder="ex. Uber to airport"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className=""
              />
              {errors.name ? <p className='errors'>{errors.name}</p>: <p className='errors'></p>}
                </label>

                <label>
                    Expense Date
                <input
                type="date"
                onChange={(e)=> setExpenseDate(e.target.value)}
                />
                {errors.expenseDate ? <p className='errors'>{errors.expenseDate}</p>: <p className='errors'></p>}
                </label>

                <label>
                    Category
                <select value={category} onChange={(e) => setCategory(e.target.value)}>
                    {categories.map(cat => (
                        <option value={cat}>
                            {cat}
                        </option>
                    ))}
                </select>
                {errors.splitType ? <p className='errors'>{errors.splitType}</p>: <p className='errors'></p>}
                </label>


                <label>
                    Total
                <input
                type="number"
                onChange={(e)=> setTotal(e.target.value)}
                />
                {errors.total ? <p className='errors'>{errors.total}</p>: <p className='errors'></p>}
                </label>

                <label>
                    Paid by you and split:
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
                </label>
                {splitType==='Percentages' && (
                        <div>
                            <p>Split by Percentage</p>
                            {
                                allUsers ?
                                trip.trip.users.map(user =>  (
                                        <label key={user.user.id} >
                                            {user.user.first_name}
                                            <input
                                            type='number'
                                            min={0}
                                            onChange={(e)=> {
                                                const newInfo={...splitTypeInfo}
                                                newInfo[user.user.id]=e.target.value
                                                setSplitTypeInfo(newInfo)
                                            }}/>
                                        </label>
                                )):
                                usersInvolved.map(user =>  (
                                    <label key={user.split(',')[0]} >
                                        {user.split(',')[1]}
                                        <input
                                        type='number'
                                        min={0}
                                        onChange={(e)=> {
                                            const newInfo={...splitTypeInfo}
                                            newInfo[parseInt(user.split(',')[0])]=e.target.value
                                            setSplitTypeInfo(newInfo)
                                        }}/>
                                    </label>
                            ))
                            }
                            <p>Total: {checkSplit}% </p>
                            <p>Total: {100-checkSplit}% left </p>
                        </div>
                    )
                }

                {splitType==='Exact' && (
                        <div>
                            <p>Split by Exact Amounts</p>
                            {
                                allUsers ?
                                trip.trip.users.map(user =>  (
                                        <label key={user.user.id} >
                                            {user.user.first_name}
                                            <input
                                            type='number'
                                            step={0.01}
                                            onChange={(e)=> {
                                                const newInfo={...splitTypeInfo}
                                                newInfo[user.user.id]=e.target.value
                                                setSplitTypeInfo(newInfo)
                                            }}/>
                                        </label>
                                )):
                                usersInvolved.map(user =>  (
                                    <label key={user.split(',')[0]} >
                                        {user.split(',')[1]}
                                        <input
                                        type='number'
                                        step={0.01}
                                        onChange={(e)=> {
                                            const newInfo={...splitTypeInfo}
                                            newInfo[parseInt(user.split(',')[0])]=e.target.value
                                            setSplitTypeInfo(newInfo)
                                        }}/>
                                    </label>
                            ))
                            }
                            <p>Total: ${checkSplit} </p>
                            <p>Total: ${total-checkSplit} left </p>
                        </div>
                    )
                        }


                <p>{splitType==='Equal' ? <>{allUsers ? `$ ${(total/trip.trip.users.length).toFixed(2)} per person`:  `$ ${(total/usersInvolved.length).toFixed(2)} per person`}</>
                : `You get back ${0}`}</p>

            </form>
        </div>
    )
}

export default AddExpenseForm
