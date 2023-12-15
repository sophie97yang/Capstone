import { useRef } from "react";
const Itinerary = ({trip}) => {
    const refs = useRef([]);
    //get a list of dates in between trip start and end date
    const daysOfWeek = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"};
    const months = {0:"January",1:"February",2:"March",3:"April",4:"May",5:"June",6:"July",7:"August",8:"September",9:"October",10:"November",11:"December"}
    const dates_between=[];
    console.log(trip);
    let date = new Date(trip.trip.start_date);
    while (date<=new Date(trip.trip.end_date)) {
        dates_between.push(new Date(date));
        date.setUTCDate(date.getUTCDate()+1);

    }
    const options={}
    options.timeZone = "UTC";

    const attach_booking_to_date = {};
    trip.trip.bookings_itineraries?.map()

    const handleClick= (date) => {
        window.scrollTo({top: refs.current[date].offsetTop -100,
        behavior: "smooth"})
    }

    return (
        <div>
            <div>
                {
                    dates_between.map(date=> (
                        <button key={date}
                        onClick={()=>handleClick(date.getUTCDate())}
                        >{date.toLocaleDateString('en-US',options).slice(0,-5)}</button>
                    ))
                }
            </div>
            <div>
                {
                    dates_between.map(date => (
                        <div key={date} id={date.getUTCDate()} className="itineraries-by-date"
                        ref={el => refs.current[date.getUTCDate()] = el}
                        >
                            <h2>{daysOfWeek[date.getDay()]}, {months[date.getMonth()]} {date.getUTCDate()}</h2>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}

export default Itinerary
