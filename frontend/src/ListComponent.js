const ListComponent = ({ setOpenPopup, ingredients }) => {
    return (
      <div className="popup-overlay">
        <div className="popup-container">
          <h2>Grocery List</h2>
          <ul className="grocery-list">
            {ingredients.map((ingredient) => {
                return <li>{ingredient}</li>
            })}
          </ul>
          <button className="close-btn" onClick={() => setOpenPopup(false)}>Close</button>
        </div>
      </div>
    );
};
export default ListComponent;