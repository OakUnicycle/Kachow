document.addEventListener("DOMContentLoaded", () => {


    const slider_template = document.getElementById("slider_template");
    

    const intro_container = document.getElementById("intro-container");
    const intro_form = document.getElementById("intro-form");
    const intro_url = document.getElementById("intro-url");
    const split_screen = document.getElementById("split_screen");
    const main_form = document.getElementById("main_form");

    intro_form.addEventListener("submit", (e) => {

        e.preventDefault();
        const url = intro_url.value;

        //intro_container.style.display = "none";
        //split_screen.style.display = "flex";
        intro_container.style.opacity = '0';
        // Disable mouse clicks on the intro screen while it's fading
        intro_container.style.pointerEvents = 'none';

        split_screen.style.display = "flex";

        setTimeout(() => {
            intro_container.style.display = "none";
            split_screen.style.opacity = "1";
        }, 500);

        populate_sliders([
            {
                title: "Political Sway",
                min: "left",
                max: "right",
                value: 50,
                leftColour: 'red',
                rightColour: 'blue'
            },
            {
                title: "Sentiment",
                min: "negative",
                max: "positive",
                value: 50,
                leftColour: 'red',
                rightColour: 'green'
            },
            {
                title: "Likelihood of Bias",
                min: "0%",
                max: "100%",
                value: 50,
            }
        ]);

        populate_related_articles([
            {
                title: "New AI Model Challenges Industry Giants",
                snippet: "A small startup has released a new language model that performs surprisingly well against competitors...",
                link: "#"
            },
            {
                title: "The Ethics of Artificial Intelligence in Media",
                snippet: "Experts debate the implications of AI-generated content and its potential impact on public discourse.",
                link: "#"
            },
            {
                title: "How Public Policy is Scrambling to Catch Up to Tech",
                snippet: "Governments around the world are facing new challenges as technology outpaces regulation.",
                link: "#"
            }
        ]);


        //main_form.submit();
    })


    function populate_sliders(sliders) {
        const container = document.querySelector('.side_bar');
        const template = document.getElementById('slider_template');

        sliders.forEach(slider => {
            // Clone the template
            const clone = template.content.cloneNode(true);

            // Populate title
            const titleElem = clone.querySelector('.slider_title');
            titleElem.textContent = slider.title;

            // Populate input
            const inputElem = clone.querySelector('.slider_input');
            
            inputElem.value = slider.value;
            inputElem.disabled = false;

            // Populate min/max labels
            clone.querySelector('.slider_min').textContent = slider.min;
            clone.querySelector('.slider_max').textContent = slider.max;

            // Determine colors (default to white)
            const leftColour = slider.leftColour || 'white';
            const rightColour = slider.rightColour || 'white';

            // Apply background gradient to the slider
            inputElem.style.background = `linear-gradient(to right, ${leftColour} 50%, ${rightColour} 50%)`;

            // Update gradient dynamically as slider moves
            inputElem.addEventListener('input', (e) => {
                e.target.style.background = `linear-gradient(to right, ${leftColour} 50%, ${rightColour} 50%)`;
            });

            console.log(clone.querySelector('.slider_input'));

            // Append to container
            container.appendChild(clone);
        });
    }

    function populate_related_articles(articles) {
        const section = document.getElementById("related-articles");

        for (article of articles) {
            const element = document.createElement('a');
            element.className = "article-card";
            element.href = article.url;
            element.innerHTML = `
                <div class="card-content">
                    <h1>${article.title}</h1>
                    <p>${article.snippet}</p>
                </div>
            `;
            section.append(element);
        }
    }
})



