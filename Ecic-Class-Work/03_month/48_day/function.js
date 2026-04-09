function greetUsers(user){
    let greetings = [];
    for(let i = 0; i < user.length; i++){
        let users = user[i];
        if (users.age >= 18){
            let message = "Hello, " + users.name + "! You are an adult.";
            greetings.push(message);
        } else {
            let message = "Hey, " + users.name + "! You are a minor.";
            greetings.push(message);
        }
    }
    return greetings;
}

let user = [
    { name: "Hamza", age: 20 },
    { name: "Sara",  age: 15 },
  
  
    { name: "Ali",   age: 25 },
];

let results = greetUsers(user);
console.log(results);

function add(a, b){
    return a + b
}

console.log(add(10, 20));

function sub(a, b){
    return a - b 
}

console.log(sub(10, 5))

function mul(a, b){
    return a * b
}

console.log(mul(10, 5))

function div(a, b){
    return a / b
}

console.log(div(10, 5))

let num = 5

function isSquare(num){
    return num * num
}

console.log(isSquare(num))

function percentage(num){
    let result = (num / 600) * 100
    return result
}

console.log(percentage(450) + "%") 


function calculateGrade(score){
    if (score >= 90){
        return "A"
    } else if (score >= 80){
        return "B"
    } else if (score >= 70){
        return "C"
    } else if (score >= 60){
        return "D"
    } else {
        return "F"
    }
}

console.log(calculateGrade(85))


