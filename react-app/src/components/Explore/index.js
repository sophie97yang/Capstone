import { useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import {getBookings} from '../../store/booking';
import { useEffect } from "react";
// import { useEffect } from "react";
// import { getHotels } from "../../store/booking";
function Explore () {
    const dispatch = useDispatch();
    const {city} = useParams();


    useEffect(()=> {
        dispatch(getBookings())
    },[dispatch])


    return (
        <h2>Hello from {city}</h2>
    )
}
export default Explore;
