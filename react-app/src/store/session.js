import { normalizeObj } from "./normalize";
// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const ADD_TRIP = "session/ADD_TRIP";
const REMOVE_TRIP ='session/REMOVE_TRIP';

const setUser = (user) => ({
	type: SET_USER,
	payload: user,
});

const removeUser = () => ({
	type: REMOVE_USER,
});

const addTrip = (trip) => ({
	type:ADD_TRIP,
	trip:trip
})

const removeTrip = (tripDetailId) => ({
	type:REMOVE_TRIP,
	tripId:tripDetailId
})

const initialState = { user: null };

export const authenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const login = (email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			email,
			password,
		}),
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

export const logout = () => async (dispatch) => {
	const response = await fetch("/api/auth/logout", {
		headers: {
			"Content-Type": "application/json",
		},
	});

	if (response.ok) {
		dispatch(removeUser());
	}
};

export const signUp = (firstName,lastName,email, password,city,state) => async (dispatch) => {
	const response = await fetch("/api/auth/signup", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			"first_name":firstName,
			"last_name":lastName,
			email,
			password,
			city,
			state
		}),
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

//ADD A TRIP TO USER'S TRIPS
export const createTrip = (formData) => async(dispatch) => {
	try {
        const res = await fetch('/api/trips/new', {
            method: "POST",
            body: formData
        })

        if (res.ok) {
            const {trip} = await res.json()
            dispatch(addTrip(trip))
            return trip
        } else {
            const data = await res.json();
            console.log("There was an error creating trip")
            return data
        }
    } catch (error) {
        console.error('An error occurred', error);
        return ['An error occurred'];
    }
}
//DELETE TRIP
export const deleteTrip = (tripId,tripDetailId)=> async(dispatch) => {
	try {
        const res = await fetch(`/api/trips/${tripId}/delete`, {
            method: "DELETE"
        })
        if (res.ok) {
			const data = await res.json();
            dispatch(removeTrip(tripDetailId));
            return data
        } else {
            const data = await res.json();
            console.log("There was an error removing trip")
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
		case SET_USER:
			newState={...state};
			newState.user = action.payload;
			newState.user.trips= normalizeObj(action.payload.trips)
			return newState
		case REMOVE_USER:
			return { user: null };
		case ADD_TRIP:
			newState={...state};
			newState.user.trips[action.trip.id] = action.trip
			return newState
		case REMOVE_TRIP:
			newState={...state};
			delete newState.trips[action.tripDetailId];
			return newState
		default:
			return state;
	}
}
