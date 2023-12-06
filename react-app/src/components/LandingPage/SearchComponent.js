import { useState } from 'react';
import {Link} from 'react-router-dom';
import '../Navigation/Navigation.css'

function SearchComponent ({className}) {
    const [searchInput, setSearchInput] = useState("");
    const [hidden,setHidden] = useState(true);
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

    let locations_match=[]

    if (searchInput.length > 0) {
        locations_match = locations.filter((location) => {
            return location.city.match(searchInput);
        })
        if (hidden===true) {
        setHidden(false)
        }
    } else {
        if (hidden===false) {
        setHidden(true)
        }
    }

    return (
<div className='search-bar'>
{!className ? <i className="fa-solid fa-magnifying-glass fa-lg"></i>:<></>}
<input
    type="search"
    placeholder="Search for places to go on your next trip..."
    onChange={(e)=>setSearchInput(e.target.value)}
    value={searchInput}
    id={className ? className :""}
     />

<table className={hidden ? "hidden":"search-output"}>
<tbody className='populate-search'id={className ? "landing-page-results" :""}>
{locations_match.length ? locations_match.map((location) => (
    <Link to={`/explore/${location.city}`} key={location.city}>
<tr>
        <td>{location.city},</td>
        <td>{location.state}</td>
</tr>
    </Link>

)): <tr><td>No results found. Please try again.</td></tr>
}
</tbody>
</table>
</div>
    )
}

export default SearchComponent;
