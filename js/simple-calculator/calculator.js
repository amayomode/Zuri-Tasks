//user input
const num1 = parseFloat(prompt("Enter the first number: "))
const operator = prompt("Enter an operator (+, -, *, / or %): ")
const num2 = parseFloat(prompt("Enter the second number: "))

//hold result
let result

if(operator == "+"){
    result = num1 + num2
}
else if(operator == "-"){
    result = num1 - num2
}
else if(operator == "*"){
    result = num1 * num2
}
else if(operator == "/"){
    result = num1 / num2
}
else if(operator == "%"){
    result = num1 % num2
}
else{
    result = "Invalid Operation"
}

alert(`${num1} ${operator} ${num2} = ${result}`)