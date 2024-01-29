import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import SignupFormModal from '../SignupFormModal'
import "./LoginForm.css";
import logo from '../../assets/images/SplitTrip-logo.png';
import google from '../../assets/images/google.png';


function LoginFormPage() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const history=useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
        history.push('/')
    }
  };

  const handleDemo = async(e) => {
    e.preventDefault();
    const email='demo@gmail.com'
    const password='password'
    const data = await dispatch((login(email, password)));
    if (data) {
      setErrors(data);
    } else {
        history.push('/')
    }
  }

  return (
    <div id='login-page'>
      <h1>Welcome back.</h1>
      <p className="redirection">
        {/* Not a member yet? <OpenModalButton
              buttonText="Sign Up"
              onButtonClick={()=> {history.push('/')}}
              modalComponent={<SignupFormModal />}
            /> */}
      </p>

      <div className="login-layout">
      <img src={logo} alt='logo' className="logo"></img>
      <form onSubmit={handleSubmit}>
        <h2>Log In to access the best of SplitTrip</h2>
        <div className='login-flex'>
        <label>
          Email
        </label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        {errors.email ? <p className='errors' id="login-errors-email">{errors.email}</p>: <p className='errors' id="login-errors-email"></p>}
        </div>
        <div className='login-flex'>
        <label>
          Password
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        {errors.password ? <p className='errors'id="login-errors-pass">{errors.password}</p>: <p className='errors' id="login-errors-pass"></p>}
        </div>
        <div className='action-buttons login-action'>
        <button type="submit" className='action-button-ls' id='longer'>Log In</button>
        <button onClick={handleDemo} className='action-button-ls'id='longer'>Log In as Demo User</button>
        <p id='login-or'>----------------------- OR ----------------------- </p>
        <a href={`${process.env.REACT_APP_BASE_URL}/api/auth/oauth_login`}><img src={google} alt='google' id='google'></img></a>
        </div>

      </form>
      </div>
    </div>
  );
}

export default LoginFormPage;
