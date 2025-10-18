from flask import Flask, render_template, request
from bias_checker import bias_checker as bc
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/upload", methods = ['POST']) # should be changed to name of website used in html
def upload():
    # if 'text' not in request.files:
    #     return render_template('404.html')
    
    url = request.form.get("url") # gets the inputted url
    bc(url) # bias checking function, takes in a website url, and returns a 'bias value'
    
    
    return render_template('index.html')





if __name__ == "__main__":
    app.run()