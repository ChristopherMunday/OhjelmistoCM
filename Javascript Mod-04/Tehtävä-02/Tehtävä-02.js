const form = document.getElementById("search-form");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const query = document.getElementById("query").value;

    const response = await fetch(
        "https://api.tvmaze.com/search/shows?q=" + query
    );

    const jsonData = await response.json();

    console.log(jsonData);
});