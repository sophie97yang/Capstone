import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, } from "react-router-dom";
import { authenticate, editTrip } from "../../store/session";
import { useModal } from "../../context/Modal";

const UpdateTripModal = ({trip}) =>{
    const dispatch = useDispatch();
    const history = useHistory();
    const user = useSelector((state) => state.session.user);
    const {closeModal} = useModal();

    console.log(trip);
    // console.log(`${new Date(trip.trip.start_date).getFullYear()}-${new Date(trip.trip.start_date).getMonth()+1}-${new Date(trip.trip.start_date).getDate()}`)

    const [name, setName] = useState(trip.trip.name);
    const [description, setDescription] = useState(trip.trip.description ? trip.trip.description : "");
    const [location,setLocation]=useState(trip.trip.location.join(','));
    const [start_date, setStartDate] = useState(new Date(trip.trip.start_date).toLocaleDateString('en-CA'));
    const [end_date, setEndDate] = useState(new Date(trip.trip.end_date).toLocaleDateString('en-CA'));
    const [newImage, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);

    const [submitted, setSubmitted] = useState(false);
    const [errors, setErrors] = useState([]);

    console.log(start_date,end_date);
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
        if (newImage) {
            form.append("image", newImage);
        }

        setImageLoading(true);

        dispatch(editTrip(form,trip.trip.id,trip.id)).then((res) => {
          setImageLoading(false);
          if (res.errors) {
            setErrors(res.errors);
          } else {
            dispatch(authenticate())
            history.push(`/trips/${trip.trip.id}/expenses`);
            setSubmitted(true);
            closeModal();
            return "success";
          }
        });

      };

      return (
        <>
          <h1 className="add-trip-title">Update Trip Details</h1>
          <form className="trip-form" onSubmit={handleSubmit} encType="multipart/form-data">
            <div>
              <label>My trip shall be called...
              <input
                type="text"
                placeholder="Trip Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className=""
              />
              {errors.name ? <p className='errors'>{errors.name}</p>: <p className='errors'></p>}
              </label>
            </div>

            <label>Description
              <textarea
                type="textarea"
                placeholder="Description of Trip (i.e.Sean and Sophie's 50th Anniversary)"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="description-field"
              />
            {errors.description ? <p className='errors'>{errors.description}</p>: <p className='errors'></p>}
            </label>

            <label>Destination
            <select value={location} onChange={(e) => setLocation(e.target.value)}>
                <option value=''>Select a Destination</option>
                {locations.map(location => (
                    <option value={location} key={location[0]}>{location[0]},{location[1]}</option>
                ))}
            </select>
            {errors.location ? <p className='errors'>{errors.location}</p>: <p className='errors'></p>}
            </label>

            <label>Start Date
            <input
                type="date"
                onChange={(e)=> setStartDate(e.target.value)}
                value={start_date}
            />
            {errors.start_date ? <p className='errors'>{errors.start_date}</p>: <p className='errors'></p>}
            </label>

            <label>End Date
            <input
                type="date"
                onChange={(e)=> setEndDate(e.target.value)}
                value={end_date}
            />
            {errors.end_date ? <p className='errors'>{errors.end_date}</p>: <p className='errors'></p>}
            </label>

            <label>Update Image
              <input
                type="file"
                accept="image/*"
                onChange={(e) => setImage(e.target.files[0])}
             />
            </label>

            <button type="submit">Update Trip</button>
            <button onClick={e=> {
              e.preventDefault();
              closeModal()
            }}>Cancel</button>
            {imageLoading && <p>Loading...</p>}
          </form>
        </>
      )
}

export default UpdateTripModal;
