import React, { useState, useCallback } from 'react';
import { GoogleMap, useJsApiLoader, Marker } from '@react-google-maps/api';

function LocationMap({city,lat,lng,name}) {
    const booking_city_map = {
        "Aspen":{lat:39.1910983,lng:-106.8175387},
        "Boston":{lat:42.3600825,lng:-71.0588801},
        "Napa":{lat:38.2975381,lng:-122.286865},
        "Miami":{lat:25.7616798,lng:-80.1917902},
        "Jackson":{lat:43.582767,lng:-110.821999},
        "Washington":{lat:38.9072,lng:-77.0369},
        "Las Vegas":{lat:36.1716,lng:-115.1391},
    }

    const [currentPosition, setCurrentPosition] = useState(booking_city_map[city]);
    const { isLoaded } = useJsApiLoader({
        id: 'google-map-script',
        googleMapsApiKey: process.env.REACT_APP_MAPS_KEY
      })

    const containerStyle = {
        width: '400px',
        height: '300px'
      };

      const [map, setMap] = useState(null)
    const onUnmount = useCallback(function callback(map) {
        setMap(null)
      }, [])


      return (

        <div className="map_page__container">

          <div style={{ height: '300px', width: '250px' }}>
              {isLoaded && <GoogleMap
                mapContainerStyle={containerStyle}
                zoom={14}
                center={{lat:lat, lng:lng}}
                onUnmount={onUnmount}
                >
                <Marker
                key={1}
                position={{lat:lat, lng:lng}}
                title={name}
                streetView={false}
                />
              </GoogleMap>}
          </div>

        </div>
      );

}

export default LocationMap;
