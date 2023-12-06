import { normalizeObj } from "./normalize";
const ALL_BOOKINGS= "booking/ALL_BOOKINGS"

const allBookings = (bookings) => ({
	type: ALL_BOOKINGS,
	bookings: bookings,
});

const initialState = { bookings: {} };

//get all bookings
export const getBookings = () => async(dispatch) => {
    try {
    const res = await fetch('/api/bookings/all')
        if (res.ok) {
            const {bookings} = await res.json()
            dispatch(allBookings(bookings))
            return null
        } else {
            const data = await res.json();
            console.log("There was an error getting bookings")
            return data
        }
    } catch (error) {
        console.error('An error occurred', error);
        return ['An error occurred'];
    }

}

export default function reducer(state = initialState, action) {
	let newState
	switch (action.type) {
		case ALL_BOOKINGS:
			newState={...state};
			newState.bookings = normalizeObj(action.bookings);
			return newState
        default:
            return state;
    }
}
// export const getHotels = () => async(dispatch) => {
// 	try {
//         const options = {method: 'GET', headers: {accept: 'application/json'}};
//         const locations = [['Aspen','CO'],
//         ['Miami','FL'],
//         ['Napa','CA'],
//         ['Boston','MA'],
//         ['Moab','UT'],
//         ['Jackson','WY'],
//         ['Nashville','TN'],
//         ['Savannah','GA'],
//         ['Charleston','SC'],
//         ['Sedona','AZ'],
//         ['Washington','DC'],
//         ['New Orleans','LA'],
//         ['Chicago','IL'],
//         ['Orlando','FL'],
//         ['Las Vegas','NV'],
//         ['Oahu','HI'],
//         ['Maui','HI'],
//         ['New York City','NY']
//         ]

//         const hotels = []
//         for (let i=0;i<locations.length; i++) {
//             const location =locations[i]
//             const res = await fetch(`https://api.content.tripadvisor.com/api/v1/location/search?searchQuery=${location[0]}&category=hotels&language=en&key=2EAF174C416B4326B2B89E64EF8EC373`, options)

//         if (res.ok) {
//             const {data} = await res.json()
//             console.log(data);
//         } else {
//             const data = await res.json();
//             console.log("There was an error getting hotels")
//             return data
//         }
//     }
//     } catch (error) {
//         console.error('An error occurred', error);
//         return ['An error occurred'];
//     }
// }
