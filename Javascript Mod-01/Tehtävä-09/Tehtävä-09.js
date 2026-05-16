const number = Number(prompt("Enter an integer:"));

let isPrime = true;

if (number < 2) {
    isPrime = false;
} else {

    for (let i = 2; i < number; i++) {

        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }
}

const result = document.createElement("p");

if (isPrime) {
    result.textContent = number + " is a prime number.";
} else {
    result.textContent = number + " is not a prime number.";
}

document.body.appendChild(result);