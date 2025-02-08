import { useState, useEffect } from 'react';
import './App.css';
import LocationInput from './LocationInput';
import ListComponent from './ListComponent';

function App() {
  const [openPopup, setOpenPopup] = useState(false);
  const [ingredients, setIngredients] = useState([]);
  useEffect(() => {
    console.log(openPopup);
  }, [openPopup])

  return (
    <div className="App">
      <LocationInput setOpenPopup={setOpenPopup} setIngredients={setIngredients} />
      {openPopup && <ListComponent setOpenPopup={setOpenPopup} ingredients={ingredients} />}
    </div>
  );
}

export default App;