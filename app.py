from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    # A simple form to submit a URL
    return """
    <form action="/submit-url" method="post">
      <label for="url">Enter URL:</label>
      <input type="text" id="url" name="url_input" size="50">
      <button type="submit">Submit</button>
    </form>
    """

@app.route("/submit-url", methods=["POST"])
def submit_url():
    url = request.form.get("url_input")
    if url:
        return f"The submitted URL is: {url}"
    return "No URL submitted."

if __name__ == "__main__":
    app.run(debug=True)