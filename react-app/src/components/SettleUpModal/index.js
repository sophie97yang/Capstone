import { useDispatch, useSelector } from "react-redux";
import settleup from '../../assets/images/settleup.png'
import './SettleUpModal.css'
import { useHistory } from "react-router-dom";
import { authenticate,settleUp } from "../../store/session";
import { useModal } from "../../context/Modal";

function SettleUp({group_balances,total_info,trip}) {
    const user = useSelector(state=>state.session.user);
    const dispatch = useDispatch();
    const history = useHistory()
    const {closeModal} = useModal()
    // const user_settlements = relationships.filter(relationship=> { return (relationship.user_one.id===user.id || relationship.user_two.id===user.id) && !(relationship.user_one.id===user.id && relationship.user_two.id===user.id)} )
    const user_settlements = group_balances[user.id]
    const user_total = total_info[user.id]
    const to_pay = user_settlements.filter(settlement => settlement.type==='payee')
    // console.log('settlements',user_settlements,'total',user_total,'to_pay',to_pay,'trip',trip);

    const handleSettle = async () => {
        const data = await dispatch(settleUp(trip.id,trip.trip.id))
        if (data) {
            console.log(data)
            return data
        } else {
            dispatch(authenticate())
            history.push(`/trips/${trip.trip.id}/expenses`)
            closeModal()
        }

    }


    return (
        <div className='settle-up-modal'>
        <button onClick={closeModal} className='close-modal' id='update-trip-close'><i className="fa-solid fa-xmark fa-2xl"></i></button>
        <h2>Settle Up</h2>
        <img src={settleup} alt='settle-up'></img>
        <p>You are settling these expenses:</p>
        { to_pay.length ?
        <ul>
            {
                to_pay.map(settlement => (
                    <li key={settlement.id}>
                        {`You paid ${settlement.user.first_name} $ ${settlement.settlement}`}
                    </li>
                ))
            }
        </ul>:
        <ul>
            {user_settlements.length ?
                user_settlements.map(settlement=> (
                    <li key={settlement.id}>{
                        `${settlement.user.first_name} paid you $ ${settlement.settlement}`
                    }
                    </li>
                ))
                :
                <li>
                    You have no expenses to settle.
                </li>

            }
        </ul>
        }
        {to_pay.length || user_settlements.length ?
        <div className='settle-action-buttons'>
            <button onClick={closeModal} id='settle-cancel'>Cancel</button>
        <button onClick={handleSettle}>Record Cash  Payment</button>

        </div>
        :
        <></>
        }
        </div>

    )

}

export default SettleUp
