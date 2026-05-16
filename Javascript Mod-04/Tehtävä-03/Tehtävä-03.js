const form = document.getElementById("search-form");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const query = document.getElementById("query").value;

    const response = await fetch(
        "https://api.tvmaze.com/search/shows?q=" + query
    );

    const jsonData = await response.json();

    console.log(jsonData);

    const results = document.getElementById("results");

    // Clear old results
    results.innerHTML = "";

    // Loop through shows
    for (let i = 0; i < jsonData.length; i++) {

        const tvShow = jsonData[i];

        // Create article
        const article = document.createElement("article");

        // Create title
        const title = document.createElement("h2");
        title.textContent = tvShow.show.name;

        // Create link
        const link = document.createElement("a");
        link.href = tvShow.show.url;
        link.target = "_blank";
        link.textContent = "Show Details";

        // Create image
        const image = document.createElement("img");
        image.src = tvShow.show.image?.medium;
        image.alt = tvShow.show.name;

        // Create summary
        const summary = document.createElement("div");
        summary.innerHTML = tvShow.show.summary;

        // Add elements to article
        article.appendChild(title);
        article.appendChild(link);
        article.appendChild(image);
        article.appendChild(summary);

        // Add article to results
        results.appendChild(article);
    }
});