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