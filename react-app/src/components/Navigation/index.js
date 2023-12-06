import React from 'react';
import { NavLink,useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import logo from '../../assets/images/logo-nav.png';
import SearchComponent from '../LandingPage/SearchComponent';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	const history = useHistory()
	return (
		<nav>
			<li className='logo-nav'>
				<NavLink exact to="/"><img src={logo} alt='logo'/></NavLink>
			</li>
			<li className='search-bar-nav'>
					<SearchComponent />
			</li>
			{isLoaded &&
				sessionUser?
				<li className='action-button-nav'>
					<ProfileButton user={sessionUser} />
				</li> :
				<div className='auth-action-buttons'>
				<li className='action-button-nav'>
					<button onClick={(e)=> {
              			e.preventDefault();
              			history.push('/login');
            		}} id='login-button'>Log in</button>
				</li>
				<li className='action-button-nav'>
					<button onClick={(e)=> {
              			e.preventDefault();
              			history.push('/signup');
            		}}id='signup-button'>Sign Up</button>
				</li>
				</div>
			}

		</nav>
	);
}

export default Navigation;
