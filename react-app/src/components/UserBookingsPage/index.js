import './UserBookings.css';
import {Link} from 'react-router-dom';

function UserBookings() {
    return (
        <div className='user-bookings'>
             <h3 className='breadcrumb-container'><Link to='/' className='breadcrumb'>Home </Link> {`  >`} Your Bookings</h3>
            <h2>Your Bookings</h2>
            <p>Feature coming soon. Please try again later.</p>
        </div>
    )

}
export default UserBookings
