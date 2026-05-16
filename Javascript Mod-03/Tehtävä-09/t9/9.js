const button = document.getElementById("start");

button.addEventListener("click", function () {

    const calculation = document.getElementById("calculation").value;

    let result;

    if (calculation.includes("+")) {

        const numbers = calculation.split("+");

        const num1 = Number(numbers[0]);
        const num2 = Number(numbers[1]);

        result = num1 + num2;

    } else if (calculation.includes("-")) {

        const numbers = calculation.split("-");

        const num1 = Number(numbers[0]);
        const num2 = Number(numbers[1]);

        result = num1 - num2;

    } else if (calculation.includes("*")) {

        const numbers = calculation.split("*");

        const num1 = Number(numbers[0]);
        const num2 = Number(numbers[1]);

        result = num1 * num2;

    } else if (calculation.includes("/")) {

        const numbers = calculation.split("/");

        const num1 = Number(numbers[0]);
        const num2 = Number(numbers[1]);

        result = num1 / num2;
    }

    document.getElementById("result").textContent =
        "Result: " + result;
});