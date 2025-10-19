document.addEventListener("DOMContentLoaded", () => {
    // comparison_word, scores, and related_articles are globally available here

    if (scores && Object.keys(scores).length > 0) {
        
        // --- BASE SLIDER CALCULATIONS ---
        // Scale [-2.0, 2.0] to [0, 100]. Your scores are bounded by [-2, 2].
        const politicalBias = (parseFloat(scores.political_bias_score) + 2) * 25; 
        const sentiment = (parseFloat(scores.sentiment_score) + 2) * 25;         
        
        const liberalAffinity = parseFloat(scores.liberal_affinity);
        const conservativeAffinity = parseFloat(scores.conservative_affinity);
        const summedAffinities = Math.abs(liberalAffinity) + Math.abs(conservativeAffinity);
        const normalizedBias = summedAffinities / 2; 
        const likelihoodOfBias = normalizedBias * 100;
        
        // --- SLIDER ARRAY SETUP ---
        const sliders = [
            {
                title: "Political Sway",
                min: "Left",
                max: "Right",
                value: politicalBias,
                leftColour: 'red',
                rightColour: 'blue'
            },
            {
                title: "Sentiment",
                min: "Negative",
                max: "Positive",
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
        ];

        // 💡 ADD THE COMPARISON WORD SLIDER IF A WORD WAS PROVIDED AND SCORED
        if (comparison_word) {
            const comparisonScoreKey = comparison_word.toLowerCase();
            const rawScore = scores[comparisonScoreKey];
            
            if (rawScore) {
                const floatScore = parseFloat(rawScore);
                
                // Scale affinity score [-1.0, 1.0] to slider value [0, 100]
                const comparisonSliderValue = ((floatScore + 1.0) / 2.0) * 100; 
                
                sliders.push({
                    title: `Affinity with "${comparison_word}"`,
                    min: "Dissimilar (-1.0)",
                    max: "Similar (+1.0)",
                    value: comparisonSliderValue,
                    leftColour: '#ff9900', // Orange
                    rightColour: '#00ccff' // Light Blue
                });
            }
        }

        // --- POPULATE SLIDERS ---
        // This is the function that iterates over the array and creates the HTML using the template
        populate_sliders(sliders); 

        populate_related_articles(related_articles);
    }
    
    // ... (Your definitions for populate_sliders and populate_related_articles go here) ...
    // Note: You may want to ensure these functions are accessible/defined in this script.
});

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