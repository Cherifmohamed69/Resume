import React, { Component } from 'react';
// import classes from './MyNewComponent.module.css';
import classes from './style.module.css'
class PersonComponent extends Component{
    render(){
        return(
            <div className={classes.card}>
                <div className={classes.content}>
                    <h1>{this.props.lastName}, {this.props.firstName}</h1>
                    <p>Age: {this.props.age}</p>
                    <p>Hair Color: {this.props.hairColor}</p>
                    <button>birthday button for {this.props.firstName} 
                    {this.props.lastName}</button>

                </div>
            </div>
        );

    }
}

export default PersonComponent;