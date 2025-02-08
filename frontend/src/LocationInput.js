import React, { useState } from "react";
import axios from "axios";
import "./LocationInput.css";  // Import the CSS file for styling

const LocationInput = ({ setOpenPopup, setIngredients }) => {
  const [pincode, setPincode] = useState("");
  const [dish, setDishName] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  const handleFetchTime = async () => {
    try {
      setError("");
      const response = await axios.get(`http://127.0.0.1:8000/get_time?pincode=${pincode}`);
    //   setData(response.data);
    } catch (err) {
      setError("Failed to fetch data. Please try again.");
    }
  };

  const sendDishName = async () => {
    try{
        setError("");
        const response = await axios.get(`http://127.0.0.1:8000/get_dishname?dishname=${dish}`);
        console.log(response);
        if(response.data.message){
            // setData(response.message);
            setIngredients(response.data.ingredients);
            setOpenPopup(true);
        }
    }
    catch{}{
        console.log('here.......');
        setError("Failed to fetch data. Please try again.");
    }
  }

  return (
    <div className="location-container">
      <div className="location-input">
        <h2>Where are you located? (Enter Pincode)</h2>
        <input
          type="text"
          value={pincode}
          onChange={(e) => setPincode(e.target.value)}
          placeholder="Enter your pincode"
          className="input-field"
        />
        <button onClick={handleFetchTime} className="button">
          Get Time
        </button>
      </div>

      <div className="food-input">
        <h2>What do you want to eat?</h2>
        <input
          type="text"
          value={dish}
          onChange={(e) => setDishName(e.target.value)}
          className="input-field"
        />
        <button className="button" onClick={sendDishName}>Submit</button>
      </div>

    </div>
  );
};

export default LocationInput;