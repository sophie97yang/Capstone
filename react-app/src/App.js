import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import AllTrips from "./components/AllTripsPage";
import CreateTripForm from "./components/CreateTripForm";
import TripDetails from "./components/TripDetailsPage";
import ExpenseDetail from "./components/ExpenseDetails";
import LandingPage from "./components/LandingPage/LandingPage";
import Explore from "./components/Explore";
import UserBookings from './components/UserBookingsPage'

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path='/explore/:city'>
            <Explore />
          </Route>
          <Route path='/trips/new'>
            <CreateTripForm />
            </Route>
          <Route exact path='/trips/:tripId/expenses/:expenseId'>
            <ExpenseDetail />
          </Route>
          <Route exact path='/trips/:id/expenses'>
            <TripDetails type='expense'/>
          </Route>
          <Route exact path='/trips/:id/itineraries'>
            <TripDetails type='itinerary'/>
          </Route>
          <Route path='/trips'>
            <AllTrips />
          </Route>
          <Route path='/bookings'>
            <UserBookings />
          </Route>
          <Route path='/404'>
          <h2>404 Not Found</h2>
        </Route>
          <Route path='/'>
            <LandingPage isLoaded={isLoaded}/>
          </Route>
        </Switch>

      )}
    </>
  );
}

export default App;
