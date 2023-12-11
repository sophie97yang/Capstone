import logo from '../../assets/images/404.png';
import {Link} from 'react-router-dom';
import './PageNotFound.css'

function PageNotFound() {
    return (
        <div className='not-found'>
            <h1>Oops! Looks like you've taken a detour into uncharted territory.</h1>
            <p> Fear not, fellow explorer! While this page may be off the map, your travel adventure with SplitTrip is just a click away.</p>
            <p> <Link to='/'> Navigate back to our home page</Link> and resume your journey to seamless bookings, unforgettable experiences, and financial harmony.</p>
            <img src={logo} alt='not-found-owl'></img>
                <p> Bon voyage, and may your future clicks lead you to exciting destinations!</p>
        </div>
    )
}

export default PageNotFound;
