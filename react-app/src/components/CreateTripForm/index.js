import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { createTrip } from "../../store/session";
import { Link } from "react-router-dom";
import logo from '../../assets/images/create-trip-logo.png';
import './CreateTrip.css'

const CreateTripForm = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector((state) => state.session.user);

    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [location,setLocation]=useState('');
    const [start_date, setStartDate] = useState('');
    const [end_date, setEndDate] = useState('');
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);

    const [submitted, setSubmitted] = useState(false);
    const [errors, setErrors] = useState([]);
    const [hidden,setHidden] = useState(true);

    useEffect(()=> {
      if (name.length) setHidden(false)
    },[name])

    useEffect(() => {
        setSubmitted(false);
        setErrors({});
      }, [submitted]);

    if (!user) {
        history.push("/login");
        return null;
    }
    const locations = [['Aspen','CO'],
    ['Miami','FL'],
    ['Napa','CA'],
    ['Boston','MA'],
    ['Moab','UT'],
    ['Jackson','WY'],
    ['Nashville','TN'],
    ['Savannah','GA'],
    ['Charleston','SC'],
    ['Sedona','AZ'],
    ['Washington','DC'],
    ['New Orleans','LA'],
    ['Chicago','IL'],
    ['Orlando','FL'],
    ['Las Vegas','NV'],
    ['Oahu','HI'],
    ['Maui','HI'],
    ['New York City','NY']
    ]
    const handleSubmit = async (e) => {
        e.preventDefault();
        let errorList = {};

        if (!name.length || name.length > 30)
          errorList.name = "Name must be between 1 and 30 characters";
        if (description.length > 500)
          errorList.description =
            "Description must be less than 500 characters";
        if (!location) errorList.location='Destination is required'
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
        form.append("description", description);
        form.append("city", location.split(',')[0]);
        form.append("state", location.split(',')[1]);
        form.append("start_date", start_date);
        form.append("end_date", end_date);
        if (image) {
            form.append("image", image);
        }

        setImageLoading(true);

        dispatch(createTrip(form)).then((res) => {
          setImageLoading(false);
          if (res.errors) {
            setErrors(res.errors);
          } else {
            history.push(`/trips`);
            setSubmitted(true);
            return "success";
          }
        });

      };

      return (
        <div className='create-trip'>
          <h2 className="add-trip-title"> <Link to='/trips' className='breadcrumb'> My Trips </Link> {'>'} Create a Trip</h2>
          <div>
          <div className='create-trip-left'>
          <h2 className='ct-heading'>Let's Go Somewhere.</h2>
          <img src={logo} alt='flying-owl'></img>
          </div>
          <form id="trip-form" onSubmit={handleSubmit} encType="multipart/form-data">
            <div id="create-trip_first">
              <label>My trip shall be called...<span className='required'>*</span></label>
              <input
                type="text"
                placeholder="Trip Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className=""
              />
              {errors.name ? <p className='errors'>{errors.name}</p>: <p className='errors'></p>}
            </div>

            <div id='create-trip-second_half' className={!hidden ? '':'hidden'}>

            <div>
            <label>Description </label>
              <textarea
                type="textarea"
                placeholder="Description of Trip (i.e.Sean and Sophie's 50th Anniversary)"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="description-field"
              />
            {errors.description ? <p className='errors'>{errors.description}</p>: <p className='errors'></p>}
            </div>

            <div>
            <label>Destination <span className='required'>*</span> </label>
            <select value={location} onChange={(e) => setLocation(e.target.value)}>
                <option value=''>Select a Destination</option>
                {locations.map(location => (
                    <option value={location} key={location[0]}>{location[0]},{location[1]}</option>
                ))}
            </select>
            {errors.location ? <p className='errors'>{errors.location}</p>: <p className='errors'></p>}
            </div>

            <div>
            <label>Start Date <span className='required'>*</span> </label>
            <input
                type="date"
                onChange={(e)=> setStartDate(e.target.value)}
            />
            {errors.start_date ? <p className='errors'>{errors.start_date}</p>: <p className='errors'></p>}
            </div>
            <div>
            <label>End Date <span className='required'>*</span> </label>
            <input
                type="date"
                onChange={(e)=> setEndDate(e.target.value)}
            />
            {errors.end_date ? <p className='errors'>{errors.end_date}</p>: <p className='errors'></p>}
            </div>

            <div id='image-input'>
            <label>Image</label>
              <input
                type="file"
                accept="image/*"
                onChange={(e) => setImage(e.target.files[0])}
             />
             </div>

            <div>
            <button type="submit" className="action-button-ls">Create Trip</button>
            </div>
            {imageLoading && <p>Loading...</p>}
           </div>
          </form>
          </div>
        </div>
      )
}

export default CreateTripForm;
