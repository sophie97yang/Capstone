import {useSelector} from 'react-redux';
import { useState } from 'react';
import {Link} from 'react-router-dom';

function LandingPage () {
    const user = useSelector(state=>state.session.user)
    const [searchInput, setSearchInput] = useState("");
    const locations = [{city:'Aspen',state:'CO'},
    {city:'Miami',state:'FL'},
    {city:'Napa',state:'CA'},
    {city:'Boston',state:'MA'},
    {city:'Moab',state:'UT'},
    {city:'Jackson',state:'WY'},
    {city:'Nashville',state:'TN'},
    {city:'Savannah',state:'GA'},
    {city:'Charleston',state:'SC'},
    {city:'Sedona',state:'AZ'},
    {city:'Washington',state:'DC'},
    {city:'New Orleans',state:'LA'},
    {city:'Chicago',state:'IL'},
    {city:'Orlando',state:'FL'},
    {city:'Las Vegas',state:'NV'},
    {city:'Oahu',state:'HI'},
    {city:'Maui',state:'HI'},
    {city:'New York City',state:'NY'}
    ]

    // const locations = {1:{city:'Aspen',state:'CO'},
    // 2:{city:'Miami',state:'FL'},
    // 3:{city:'Napa',state:'CA'},
    // 4:{city:'Boston',state:'MA'},
    // 5:{city:'Moab',state:'UT'},
    // 6:{city:'Jackson',state:'WY'},
    // 7:{city:'Nashville',state:'TN'},
    // 8:{city:'Savannah',state:'GA'},
    // 9:{city:'Charleston',state:'SC'},
    // 10:{city:'Sedona',state:'AZ'},
    // 11:{city:'Washington',state:'DC'},
    // 12:{city:'New Orleans',state:'LA'},
    // 13:{city:'Chicago',state:'IL'},
    // 14:{city:'Orlando',state:'FL'},
    // 15:{city:'Las Vegas',state:'NV'},
    // 16:{city:'Oahu',state:'HI'},
    // 17:{city:'Maui',state:'HI'},
    // 18:{city:'New York City',state:'NY'}
    // }
    let locations_match=[]

    if (searchInput.length > 0) {
            locations_match = locations.filter((location) => {
            return location.city.match(searchInput);
        })
    }

    return (
        <div>
            <div className='headings'>
            <h1>Where to?</h1>
            <h2>SplitTrip is here for you from start to finish.</h2>
            </div>
            <div className='search-bar'>
            <input
                type="search"
                placeholder="Search for places to go on your next trip"
                onChange={(e)=>setSearchInput(e.target.value)}
                value={searchInput} />

            <table>
            <tr>
                <th>City</th>
                <th>State</th>
            </tr>
            {locations_match.map((location) => (
                <Link to={`/explore/${location.city}`} key={location.city}>
                <tr>
                    <td>{location.city}</td>
                    <td>{location.state}</td>
                </tr>
                </Link>

        ))}
    </table>
    </div>
    </div>
    )
}

export default LandingPage
