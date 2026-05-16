const name = prompt("Enter your name:");

const result = document.createElement("p");
result.textContent = "Hello, " + name + "!";

document.body.appendChild(result);