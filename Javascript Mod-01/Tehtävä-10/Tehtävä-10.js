const diceCount = Number(prompt("Enter the number of dice:"));
const targetSum = Number(prompt("Enter the desired sum of eye numbers:"));

const simulations = 10000;
let successfulRolls = 0;

for (let i = 0; i < simulations; i++) {
    let total = 0;

    for (let j = 0; j < diceCount; j++) {
        const diceRoll = Math.floor(Math.random() * 6) + 1;
        total += diceRoll;
    }

    if (total === targetSum) {
        successfulRolls++;
    }
}

const probability = (successfulRolls / simulations) * 100;

document.getElementById("result").textContent =
    "Probability to get sum " + targetSum + " with " + diceCount + " dice is " + probability.toFixed(2) + "%";