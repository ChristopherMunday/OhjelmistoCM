const num1 = Number(prompt("Enter first integer:"));
const num2 = Number(prompt("Enter second integer:"));
const num3 = Number(prompt("Enter third integer:"));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

const result = document.createElement("p");

result.innerHTML =
    "Sum: " + sum + "<br>" +
    "Product: " + product + "<br>" +
    "Average: " + average;

document.body.appendChild(result);