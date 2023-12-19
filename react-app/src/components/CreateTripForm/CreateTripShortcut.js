import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { createTrip } from "../../store/session";

const CreateTripShortcut = ({city,state,closeModal}) => {
    const dispatch = useDispatch();
    const history = useHistory();

    const [name, setName] = useState("");
    const [start_date, setStartDate] = useState('');
    const [end_date, setEndDate] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [errors, setErrors] = useState([]);

    useEffect(() => {
        setSubmitted(false);
        setErrors({});
      }, [submitted]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        let errorList = {};

        if (!name.length || name.length > 30)
          errorList.name = "Name must be between 1 and 30 characters";
        //start date can be in the past
        //end date cannot be less than start date
        if(!start_date) errorList.start_date = 'Date is required'
        if (!end_date || new Date(end_date)< new Date(start_date))
            errorList.end_date='Your trip must be at least one day long'

        if (Object.values(errorList).length > 0) {
          setErrors(errorList);
          return;
        }

        const form = new FormData();
        form.append("name", name);
        form.append("city", city);
        form.append("state", state);
        form.append("start_date", start_date);
        form.append("end_date", end_date);

        dispatch(createTrip(form)).then((res) => {
          if (res.errors) {
            setErrors(res.errors);
          } else {
            history.push(`/trips`);
            closeModal();
            setSubmitted(true);
            return "success";
          }
        });

      };

      return (
          <form onSubmit={handleSubmit} encType="multipart/form-data" className='shortcut-trip-form'>
              <label>My trip shall be called...</label>
              <input
                type="text"
                placeholder="Trip Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className=""
              />
              {errors.name ? <p className='errors'>{errors.name}</p>: <p className='errors'></p>}


            <div>
            <label>Destination </label>
            <select>
                <option value={`${[city,state]}`}>{city},{state}</option>
            </select>
            </div>

            <div>
            <label>Start Date </label>
            <input
                type="date"
                onChange={(e)=> setStartDate(e.target.value)}
            />
            {errors.start_date ? <p className='errors'>{errors.start_date}</p>: <p className='errors'></p>}
            </div>

            <div>
            <label>End Date </label>
            <input
                type="date"
                onChange={(e)=> setEndDate(e.target.value)}
            />
            {errors.end_date ? <p className='errors'>{errors.end_date}</p>: <p className='errors'></p>}
            </div>

            <button type="submit" className="action-button-ls">Create Trip</button>
          </form>
          )}


export default CreateTripShortcut;
