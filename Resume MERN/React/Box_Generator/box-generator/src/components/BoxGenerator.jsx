import { useState } from 'react';

const BoxGenerator = () => {
  const [boxes, setBoxes] = useState([]);
  const [color, setColor] = useState('');

  const handleColorChange = (e) => {
    setColor(e.target.value);
  };



  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (color) {
      setBoxes((prevBoxes) => [
        ...prevBoxes,
        { color, size:'300px' },
      ]);
      setColor('');
    }
  };

  return (
    <div>
      <form onSubmit={handleFormSubmit}>
        <label  >
          Color:
          <input type="color" value={color} onChange={handleColorChange} />
        </label>

        <button type="submit"> Add Box </button>
      </form>
      <div>
        {boxes.map((box, index) => (
          <div
            key={index}
            style={{
              backgroundColor: box.color,
              width: box.size,
              height: box.size,
              display: 'inline-block',
              margin: '5px',
            }}
          ></div>
        ))}
      </div>
    </div>
  );
};

export default BoxGenerator;
