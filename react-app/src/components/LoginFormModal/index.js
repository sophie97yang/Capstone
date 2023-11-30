import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import SignupFormModal from '../SignupFormModal'
import "./LoginForm.css";
import logo from '../../assets/images/SplitTrip-logo.png';

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const history=useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
        closeModal()
    }
  };

  return (
    <div id='login-modal'>
      <h1>Welcome back.</h1>
      <img src={logo} alt='logo' className="logo"></img>
      <p>Not a member yet? <OpenModalButton
              buttonText="Sign Up"
              onButtonClick={()=> {history.push('/')}}
              modalComponent={<SignupFormModal />}
            />
      </p>

      <form onSubmit={handleSubmit}>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          {errors.email ? <p className='errors'>{errors.email}</p>: <p className='errors'></p>}
        </label>

        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          {errors.password ? <p className='errors'>{errors.password}</p>: <p className='errors'></p>}
        </label>
        <button type="submit">Log In</button>
      </form>
    </div>
  );
}

export default LoginFormModal;
