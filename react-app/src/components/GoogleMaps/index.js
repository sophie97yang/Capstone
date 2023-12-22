import React, { useState, useCallback } from 'react';
import { GoogleMap, useJsApiLoader, Marker } from '@react-google-maps/api';
import foodIcon from "../../assets/images/food-icon-maps.png";
import hotelIcon from "../../assets/images/hotel-icon-maps.png";
import thingsIcon from "../../assets/images/hotel-icon-maps.png";

function Map({trip}) {
    const booking_city_map = {
        "Aspen":{lat:39.1910983,lng:-106.8175387},
        "Boston":{lat:42.3600825,lng:-71.0588801},
        "Napa":{lat:38.2975381,lng:-122.286865},
        "Miami":{lat:25.7616798,lng:-80.1917902},
        "Jackson":{lat:43.582767,lng:-110.821999},
        "Washington":{lat:38.9072,lng:-77.0369},
        "Las Vegas":{lat:36.1716,lng:-115.1391},

    }
    const icons_category_map = {
        "Hotel":hotelIcon,
        "Restaurants":foodIcon,
        "Things To Do":thingsIcon
    }
    const [currentPosition, setCurrentPosition] = useState(booking_city_map[trip.trip.location[0]]);
    const { isLoaded } = useJsApiLoader({
        id: 'google-map-script',
        key: process.env.REACT_APP_MAPS_KEY
      })

    const containerStyle = {
        width: '500px',
        height: '1200px'
      };

      const [map, setMap] = useState(null)
    const onUnmount = useCallback(function callback(map) {
        setMap(null)
      }, [])

    return (

        <div className="map_page__container">

          <div style={{ height: '1200px', width: '600px' }}>
              {isLoaded && <GoogleMap
                mapContainerStyle={containerStyle}
                zoom={10}
                center={currentPosition}
                onUnmount={onUnmount}
                >
            {trip.trip.bookings_itinerary?.map(itinerary =>(
                <Marker
                key={itinerary.id}
                position={{lat:itinerary.booking.lat, lng:itinerary.booking.lng}}
                title={itinerary.booking.name}
                streetView={false}
                />
            )
            )}
              </GoogleMap>}
          </div>

        </div>
      );


}

export default Map;
