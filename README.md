# Split Trip

[SplitTrip](https://split-trip.onrender.com), a revolutionary travel application, blending the functionalities of Trip Advisor and Splitwise. Discover and book adventures with ease and split expenses effortlessly among your travel group. No more awkward calculations or misunderstandings – SplitTrip ensures that every trip is not just memorable but financially stress-free, making it the ultimate travel companion. Embark on your next journey with confidence, where exploration and expense management can coexist seamlessly.

## Tech Stack
 ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
 ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
 ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
 ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
 ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
 ![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
 ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
 ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## Installation Instructions
1. Clone the repository: git clone `https://github.com/sophie97yang/SplitTrip.git`
2. Set up .env file, see .env.example for assistance
3. Install Dependencies: `pip install -r requirements.txt`
4. Set up virtual environment: `pipenv shell`
5. Database and Server setup, run the following commands
  * `flask db upgrade`
  * `flask seed all`
  * `flask run`
6. Open a New Terminal, navigate to the react-app folder: `cd react-app`
7. Install Dependencies: `npm install`
8. Run application: `npm start`
9. Visit http://localhost:3000 in your browser to see the React application running.

## How To Use: Features
### Landing
<img width="600" height="600" alt="Screenshot 2024-01-03 at 9 24 17 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/15546e13-520c-42cb-941b-29d521639399">

<br>
Explore here to your heart's desire. You must be logged in in order to create trips, initiate bookings/reservations, add collaborators, and split expenses. If you do not have an account with SplitTrip, you can sign up or log in as a Demo User.

### User Trips
<img width="600" height="600"  alt="Screenshot 2023-12-11 at 5 33 23 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/f7f3fa98-42f1-45f8-9197-765665a3336c">
<br>
Here, you are able to view a general overview of the trips that you have created or have been invited to. You are greeted with the option to create a new trip, make edits to a trip(update details, invite collaborators, delete trip,add expenses) or to view a specific trip's details. When you are directed to the trips details page, you will have the ability to create,view and settle expenses.

### User Bookings
<img width="600" height="500" alt="Screenshot 2024-01-03 at 9 26 24 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/f6885543-47e6-4d0e-9df5-8e03eae910bc">
<br>
Here, you are able to view all of the bookings you have made to your trips' itineraries. You are able to access the attraction's details by clicking on the attraction name and access the specific trip's details by clicking on the trip's name. 

### Trip Details - Expenses
<img width="600" height="500" alt="Screenshot 2023-12-11 at 6 00 51 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/e955ef2d-e6e2-4e53-8b42-b40384536b7d">
<br>
When accessing trip details, you are met with 2 options - to view trip expenses or to view the trip's itinerary. On both pages, you are able to edit trip information (by clicking on trip name), explore the city of your destination (by clicking on location), and invite collaborators to the trip. 
On the expenses page, you are able to view all of your trips expenses as well as add and edit expenses created within the trip's duration. Additionally, you are able to view the details of who you owe money to and what individuals owe money based on what they have paid for throughout the trip. You can settle these expenses as well at any point during the trip.

### Trip Details - Itineraries 
<img width="600" height="400"  alt="Screenshot 2024-01-03 at 8 56 31 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/e7c49ee8-e4aa-4e5d-afb7-f2f25b20b07a">
<br>
On the itinerary page,you are able to view a day by day breakdown of your trip. If you have not planned your day itinerary through SplitTrip, you will be greeted with the option to explore the trip destination and make bookings as necessary. If you have made bookings through SplitTrip, you will be able to access details of the reservation here as well as the location of all of the bookings on the maps feature. If you have not expensed your booking yet, you are met with the option to add the expense to the trip. IF you have added the expense, you will be able to view details of the expense and edit it as you wish.

### Expense Details 
<img width="600" height="500" alt="Screenshot 2024-01-03 at 9 19 39 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/f5cda042-fc05-465f-9ca3-6b044aaa4f86">
<br>
Here, you are able to view the details of an expense that was created, make edits if necessary, view edit history, and have the option to delete the expense (if you created the expense).


### Explore Cities 
<img width="600" height="700"  alt="Screenshot 2024-01-03 at 6 39 42 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/673dfd67-bf31-4459-a652-4dd49d8b9fbc">
<img width="600" height="600"  alt="Screenshot 2024-01-03 at 6 39 49 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/396e0636-7ba2-4bab-b5b3-b561900a81ea">
<img width="600" height="400" alt="Screenshot 2024-01-04 at 9 15 54 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/2f17a588-1be4-40eb-98e6-dd03ff880fb8">

<br>
Here, you are able to explore everything that the destination of your choice has to offer! On this page, you are given the option directly create a trip for this specific destination and given a general overview of the different attractions grouped by places to stay, restaurants, and things to do. You can click on the attraction to get more details or click on the "Add to Itinerary" button in order to book the itinerary for your upcoming trip. If you have no upcoming trips at this destination, you will have to create a trip first.
At the top of the explore page, you also will be able to filter the attractions by category: Hotel, Restaurants, Things To Do. Selecting the attraction will allow you to make a reservation for your upcoming trip or by clicking on the name of the attraction, you are able to be navigated to the attraction details page.


### Attraction Details 
<img width="600" height="500" alt="Screenshot 2024-01-03 at 8 58 06 AM" src="https://github.com/sophie97yang/SplitTrip/assets/129304831/20331c6e-1bd1-4154-a089-5edb5c432c3b">
Here, you are able to view all details of the specific attraction and make a reservation for one of your upcoming trips!

## Future Implementations
Although this application has a robust amount of features, there is still a bright future of new features to be added. 
I look forward to:
- Allowing users to modify their reservation and itinerary
    - Modifying reservation time, modifying party size, canceling reservation
- Creating more interactions between collaborators of trips - allowing ocllaborators to pitch potential ideas/bookings to trip members and being able to release a poll to vote on the attraction of their choice that they would like to make the reservation for
- Allowing users to be able to search for bookings or specific attractions. Currently, they are only able to search for potential destinations
- Making the interface more responsive, allowing users to interact with the application on mobile devices
