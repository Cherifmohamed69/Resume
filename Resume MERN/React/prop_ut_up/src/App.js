import React, { useState } from "react";
import PersonCard from "./components/PersonCard";

function App() {
  const [users, setUsers] = useState([
    {
      id: 1,
      first_name: "Doe",
      last_name: "Jane",
      age: 45,
      hair_color: "black",
    },
    {
      id: 2,
      first_name: "Smith",
      last_name: "John",
      age: 88,
      hair_color: "brown",
    },
    {
      id: 3,
      first_name: "Fillmore",
      last_name: "Millard",
      age: 50,
      hair_color: "brown",
    },
    {
      id: 4,
      first_name: "Smith",
      last_name: "Maria",
      age: 62,
      hair_color: "brown",
    },
  ]);

  const handleIncrement = (userId) => {
    setUsers((prevUsers) =>
      prevUsers.map((user) =>
        user.id === userId ? { ...user, age: user.age + 1 } : user
      )
    );
  };

  return (
    <div className="App">
      {users.map((user) => (
        <div key={user.id}>
          <PersonCard
            first_name={user.first_name}
            last_name={user.last_name}
            age={user.age}
            handleIncrement={() => handleIncrement(user.id)}
            hair_color={user.hair_color}
          />
        </div>
      ))}
    </div>
  );
}

export default App;
