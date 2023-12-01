import React from 'react';
import { NavLink,useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import logo from '../../assets/images/logo-nav.png';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	const history = useHistory()
	return (
		<nav>
			<li>
				<NavLink exact to="/"><img src={logo} alt='logo'/></NavLink>
			</li>
			{isLoaded && (
				sessionUser?
				<li>
					<ProfileButton user={sessionUser} />
				</li> :
				<>
				<li>
					<button onClick={(e)=> {
              			e.preventDefault();
              			history.push('/login');
            		}}>Log in</button>
				</li>
				<li>
					<button onClick={(e)=> {
              			e.preventDefault();
              			history.push('/signup');
            		}}>Sign Up</button>
				</li>
				</>
			)}

		</nav>
	);
}

export default Navigation;
