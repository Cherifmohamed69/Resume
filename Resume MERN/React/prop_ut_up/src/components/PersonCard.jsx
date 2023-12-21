import React, { Component } from 'react';
import './card.css';

class PersonCard extends Component {
  render() {
    const { first_name, last_name, age, hair_color, handleIncrement } = this.props;

    return (

      <div className='card'>
        <h1>{first_name}, {last_name}</h1>
        <br/>Age: {age} <button onClick={handleIncrement}>
          Increment Age
        </button>

        <br /> Hair Color: {hair_color}
      </div>
    );
  }
}

export default PersonCard;
