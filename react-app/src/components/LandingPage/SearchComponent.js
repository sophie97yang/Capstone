import { useState,useEffect } from 'react';
import {useHistory} from 'react-router-dom';
import '../Navigation/Navigation.css'

function SearchComponent ({className}) {
    const [searchInput, setSearchInput] = useState("");
    const [hidden,setHidden] = useState(true);
    const history = useHistory();
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
    const [searchResults,setResults] = useState(locations);

    const handleChange = (e) => {
        e.preventDefault();
        setSearchInput(e.target.value);
        setHidden(false);
        const locations_match = locations.filter((location) => location.city.toLowerCase().includes(searchInput.toLowerCase()))
        setResults(locations_match);

        };

    useEffect(()=> {
        if (searchInput.length===0) {
            setResults(locations)
            setHidden(true);
        }
        },[searchInput])

    return (
<div className='search-bar'>
{!className ? <i className="fa-solid fa-magnifying-glass fa-lg"></i>:<></>}
{/* {!className ? <></>:
<select>
    <option>Cities</option>
</select>
} */}
<input
    type="search"
    placeholder="Search for places to go on your next trip..."
    onChange={handleChange}
    value={searchInput}
    id={className ? className :""}
     />

<ul className={hidden ? "hidden":"search-output"} id={className ? "landing-page-results" :""}>
{/* <tbody className='populate-search'> */}
{searchResults.length ? searchResults.map((location) => (
    <button key={location.city} className='search-list-item'
    onClick={(e)=>{
        e.preventDefault();
        setHidden(true);
        history.push(`/explore/${location.city}`);
        setSearchInput('');
    } }>
        {location.city},{location.state}
    </button>


)): <li>No results found. Please try again.</li>
}
</ul>
</div>
    )
}

export default SearchComponent;
