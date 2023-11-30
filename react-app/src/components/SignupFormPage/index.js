import React, { useState,useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect,useHistory } from "react-router-dom";
import { signUp } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [city,setCity]=useState("");
  const [state,setState]=useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const [hidden,setHidden] = useState(true)
  const [confirm,setConfirm] = useState(false);
  const history=useHistory();

  //input fields show up at specific times
  useEffect(()=> {
    if (firstName.length && lastName.length) setHidden(false)
  },[firstName,lastName])

  useEffect(()=> {
    if (password) setConfirm(true)
  },[password])

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();

    //validate user input
    let errorList = {};

    if (!firstName) errorList.firstName = "First Name is required";
    if (!lastName) errorList.lastName = "Last Name is required";

    if (!city) errorList.city = "City is required";
    if (!state) errorList.state = "Please select a state";
    if (!email || !email.includes("@"))
      errorList.email = "A valid email is required";
    if (!password || password.length<6) errorList.password = "Password must be 6 characters or more";

    if (Object.values(errorList).length > 0) {
      setErrors(errorList);
      return;
    }

    ///if there are no validation errors
    if (password === confirmPassword) {
        const data = await dispatch(signUp(firstName,lastName,email, password,city,state));
        if (data) {
          setErrors(data)
        }
    } else {
        setErrors({"confirmPassword":'Passwords must match'});
    }
  };

  return (
    <>
      <h1>INTRODUCE YOURSELF</h1>
      <p>Already a member?<OpenModalButton
              buttonText="Log In"
              onButtonClick={()=> {history.push('/')}}
              modalComponent={<LoginFormModal />}
            />
        </p>
      <form onSubmit={handleSubmit}>

        <div id='signup_first-half'>
         <h2> Hi there! My name is </h2>

          <label>
            First Name
          <input
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
          />
          {errors.firstName ? <p className='errors'>{errors.firstName}</p>: <p className='errors'></p>}
          </label>

          <label>
            Last Name
          <input
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
          />
          {errors.lastName ? <p className='errors'>{errors.lastName}</p>: <p className='errors'></p>}
         </label>
        </div>

        <div id='signup-second_half' className={!hidden ? '':'hidden'}>
        <div>
          <h2>I'm joining from</h2>

        <label>
            City
            <input
              type="text"
              value={city}
              onChange={(e) => setCity(e.target.value)}
            />
        {errors.city ? <p className='errors'>{errors.city}</p>: <p className='errors'></p>}
        </label>

        <label>
            State
            <select value={state} onChange={(e) => setState(e.target.value)}>
              <option value="">Select a State</option>
              <option value="AL">Alabama</option>
              <option value="AK">Alaska</option>
              <option value="AZ">Arizona</option>
              <option value="AR">Arkansas</option>
              <option value="CA">California</option>
              <option value="CO">Colorado</option>
              <option value="CT">Connecticut</option>
              <option value="DE">Delaware</option>
              <option value="DC">District Of Columbia</option>
              <option value="FL">Florida</option>
              <option value="GA">Georgia</option>
              <option value="HI">Hawaii</option>
              <option value="ID">Idaho</option>
              <option value="IL">Illinois</option>
              <option value="IN">Indiana</option>
              <option value="IA">Iowa</option>
              <option value="KS">Kansas</option>
              <option value="KY">Kentucky</option>
              <option value="LA">Louisiana</option>
              <option value="ME">Maine</option>
              <option value="MD">Maryland</option>
              <option value="MA">Massachusetts</option>
              <option value="MI">Michigan</option>
              <option value="MN">Minnesota</option>
              <option value="MS">Mississippi</option>
              <option value="MO">Missouri</option>
              <option value="MT">Montana</option>
              <option value="NE">Nebraska</option>
              <option value="NV">Nevada</option>
              <option value="NH">New Hampshire</option>
              <option value="NJ">New Jersey</option>
              <option value="NM">New Mexico</option>
              <option value="NY">New York</option>
              <option value="NC">North Carolina</option>
              <option value="ND">North Dakota</option>
              <option value="OH">Ohio</option>
              <option value="OK">Oklahoma</option>
              <option value="OR">Oregon</option>
              <option value="PA">Pennsylvania</option>
              <option value="RI">Rhode Island</option>
              <option value="SC">South Carolina</option>
              <option value="SD">South Dakota</option>
              <option value="TN">Tennessee</option>
              <option value="TX">Texas</option>
              <option value="UT">Utah</option>
              <option value="VT">Vermont</option>
              <option value="VA">Virginia</option>
              <option value="WA">Washington</option>
              <option value="WV">West Virginia</option>
              <option value="WI">Wisconsin</option>
              <option value="WY">Wyoming</option>
          </select>
          {errors.state ? <p className='errors'>{errors.state}</p>: <p className='errors'></p>}
        </label>
        </div>


        <label>
          <h2> This is my email address</h2>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          {errors.email ? <p className='errors'>{errors.email}</p>: <p className='errors'></p>}
        </label>

        <label>
        <h2> This is my password</h2>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          {errors.password ? <p className='errors'>{errors.password}</p>: <p className='errors'></p>}
        </label>

        <label className={confirm ? '': 'hidden'}>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </label>
        {errors.confirmPassword ? <p className='errors'>{errors.confirmPassword}</p>: <p className='errors'></p>}

        <button type="submit">Sign Up</button>

        </div>
      </form>
    </>
  );
}

export default SignupFormPage;
