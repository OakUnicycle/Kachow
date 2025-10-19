document.addEventListener("DOMContentLoaded", () => {

    // Check if we have scores data. If we do, it means the page has been loaded
    // with data from the backend, so we should populate the sliders and cards.
    if (scores && Object.keys(scores).length > 0) {
        const politicalBias = (parseFloat(scores.political_bias_score) + 1) * 50;
        const sentiment = (parseFloat(scores.sentiment_score) + 1) * 50;
        const summedAffinities = Math.abs(parseFloat(scores.liberal_affinity)) + Math.abs(parseFloat(scores.conservative_affinity));
        const normalizedBias = summedAffinities / 2;
        const likelihoodOfBias = normalizedBias * 100;

        populate_sliders([
            {
                title: "Political Sway",
                min: "left",
                max: "right",
                value: politicalBias,
                leftColour: 'red',
                rightColour: 'blue'
            },
            {
                title: "Sentiment",
                min: "negative",
                max: "positive",
                value: sentiment,
                leftColour: 'red',
                rightColour: 'green'
            },
            {
                title: "Likelihood of Bias",
                min: "0%",
                max: "100%",
                value: likelihoodOfBias,
            }
        ]);

        populate_related_articles(related_articles);
    }

    function populate_sliders(sliders) {
        const container = document.querySelector('.side_bar');
        const template = document.getElementById('slider_template');

        sliders.forEach(slider => {
            const clone = template.content.cloneNode(true);

            clone.querySelector('.slider_title').textContent = slider.title;
            const valueElem = clone.querySelector('.slider_value');
            valueElem.textContent = Math.round(slider.value);

            const inputElem = clone.querySelector('.slider_input');
            inputElem.value = slider.value;
            inputElem.disabled = true; // Enable the slider

            clone.querySelector('.slider_min').textContent = slider.min;
            clone.querySelector('.slider_max').textContent = slider.max;

            const leftColour = slider.leftColour || 'white';
            const rightColour = slider.rightColour || 'white';

            inputElem.style.background = `linear-gradient(to right, ${leftColour} ${inputElem.value}%, ${rightColour} ${inputElem.value}%)`;

            inputElem.addEventListener('input', (e) => {
                valueElem.textContent = Math.round(e.target.value);
                e.target.style.background = `linear-gradient(to right, ${leftColour} ${e.target.value}%, ${rightColour} ${e.target.value}%)`;
            });

            container.appendChild(clone);
        });
    }

    function populate_related_articles(articles) {
        const section = document.getElementById("related-articles");
        section.innerHTML = ''; // Clear existing cards

        for (const article of articles) {
            const element = document.createElement('a');
            element.className = "article-card";
            element.href = article.link;
            element.target = "_blank"; // Open in new tab
            element.rel = "noopener noreferrer";
            element.innerHTML = `
                <div class="card-content">
                    <h1>${article.title}</h1>
                    <p>${article.snippet}</p>
                </div>
            `;
            section.append(element);
        }
    }
});