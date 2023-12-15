/*---------------------------------------------------Problem 1-----------------------------------------------*/

// const cars = ['Tesla', 'Mercedes', 'Honda']
// const [ randomCar ] = cars
// const [ ,otherRandomCar ] = cars
// console.log(randomCar)
// console.log(otherRandomCar)

//output : =================tesla - mercedes======================

/*----------------------------------------------------Problem 2-----------------------------------------------*/

// const employee = {
//   name: "Elon",
//   age: 47,
//   company: "Tesla",
// };
// const { name: otherName } = employee; //the "key" name change to "otherName" and the value is the same "Elon"
// //========================================Predict the output=============================
// // console.log(name); // Error message
// console.log(otherName); // Elon

/*----------------------------------------------------Problem 3------------------------------------------------*/

// const password = "12345";
// const person = {
//   name: "Phil Smith",
//   age: 47,
//   height: "6 feet",
// };
// const { password: hashedPassword } = person;
// //Predict the output
// console.log(password); // 12345
// console.log(hashedPassword); // undefined------------because the 'person' object does not have a 'password' property.

/*-----------------------------------------------------Problem 4-------------------------------------------------*/

// const numbers = [8, 2, 3, 5, 6, 1, 67, 12, 2];
// const [, first] = numbers; //first= 2
// const [, , , second] = numbers; // second= 5
// const [, , , , , , , , third] = numbers; // third= 2
// //Predict the output
// console.log(first == second); //false ------because first= 2 and second= 5
// console.log(first == third); //true ---------because first= 2 and third= 2

/*----------------------------------------------------------------Problem 5--------------------------------------------------*/
// const lastTest = {
//   key: "value",
//   secondKey: [1, 5, 1, 8, 3, 3],
// };
// const { key } = lastTest;
// const { secondKey } = lastTest;
// const [, willThisWork] = secondKey;
// //Predict the output
// console.log(key); // value
// console.log(secondKey); // [1, 5, 1, 8, 3, 3]
// console.log(secondKey[0]); // 1
// console.log(willThisWork); // 5
