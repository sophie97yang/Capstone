import {useSelector} from 'react-redux';
import {Link} from 'react-router-dom'

function LandingPage () {
    const user = useSelector(state=>state.session.user)
    return (
        <div>
            <h1>Hello from SplitTrip!</h1>
           { !user ? <h2>Log In or Sign Up to get started</h2> :<h2>Go to <Link to='/trips'>Your Trips</Link> to get started</h2>}
        </div>
    )
}

export default LandingPage
