const candidateCount = Number(prompt("Enter number of candidates:"));

const candidates = [];


for (let i = 0; i < candidateCount; i++) {
    const name = prompt("Name for candidate " + (i + 1) + ":");

    candidates.push({
        name: name,
        votes: 0
    });
}


const voterCount = Number(prompt("Enter number of voters:"));


for (let i = 0; i < voterCount; i++) {
    const vote = prompt("Voter " + (i + 1) + ", enter candidate name:");

    if (vote === "" || vote === null) {
        continue;
    }

    for (let j = 0; j < candidates.length; j++) {
        if (candidates[j].name === vote) {
            candidates[j].votes++;
            break;
        }
    }
}


candidates.sort(function (a, b) {
    return b.votes - a.votes;
});


const winner = candidates[0];


console.log("The winner is " + winner.name + " with " + winner.votes + " votes.");
console.log("results:");

for (let i = 0; i < candidates.length; i++) {
    console.log(candidates[i].name + ": " + candidates[i].votes + " votes");
}