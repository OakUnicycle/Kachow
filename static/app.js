document.addEventListener("DOMContentLoaded", () => {
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






function create_slider(slider) {
  const template = document.getElementById("slider_template");
  
  const clone = template.content.cloneNode(true);

  clone.querySelector(".slider_title").textContent = slider.title;

  const sliderInput = clone.querySelector(".slider_input");
  sliderInput.value = slider.value;

  clone.querySelector(".slider_min").textContent = slider.min;
  clone.querySelector(".slider_max").textContent = slider.max;

  sliderInput.style.background = slider.gradient;

  return clone;
}

const example_data = [
  {
    title: "Likelihood of Bias",
    value: 50,
    min: "0%",
    max: "100%",
    gradient: "linear-gradient(to right, white 100%)"
  },
  {
    title: "Political Leaning",
    value: 50,
    min: "Left",
    max: "Right",
    gradient: "linear-gradient(to right, blue 50%, red 50%)"
  }
];

const sideBar = document.getElementById("side_bar");

example_data.forEach(example => {
  const clone = create_slider(example)
  console.log(clone);
  sideBar.appendChild(clone);
});