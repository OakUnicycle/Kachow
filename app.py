from flask import Flask, render_template, request
from bias_checker import bias_checker as bc
app = Flask(__name__)


url = 'hello'
@app.route("/", methods=['GET', 'POST'])
def index():
    url = request.form.get('url')


    return render_template('index.html', url = url)

if __name__ == "__main__":
    app.run()