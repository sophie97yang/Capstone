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
import Footer from "./components/Footer";
import ProtectedRoute from "./components/ProtectedRoute";
import PageNotFound from "./components/404/404";

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
          <ProtectedRoute path='/trips/new'>
            <CreateTripForm />
            </ProtectedRoute>
          <ProtectedRoute exact path='/trips/:tripId/expenses/:expenseId'>
            <ExpenseDetail />
          </ProtectedRoute>
          <ProtectedRoute exact path='/trips/:id/expenses'>
            <TripDetails type='expense'/>
          </ProtectedRoute>
          <ProtectedRoute exact path='/trips/:id/itineraries'>
            <TripDetails type='itinerary'/>
          </ProtectedRoute>
          <ProtectedRoute path='/trips'>
            <AllTrips />
          </ProtectedRoute>
          <Route path='/bookings'>
            <UserBookings />
          </Route>
          <Route exact path='/'>
            <LandingPage isLoaded={isLoaded}/>
          </Route>
          <Route path='*'>
          <PageNotFound />
          </Route>
        </Switch>

      )}
      <Footer />
    </>
  );
}

export default App;
