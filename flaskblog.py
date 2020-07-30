from flask import Flask, render_template, url_for
from util.jl_utility import get_jl_data
import re

app = Flask(__name__)

jl_data = get_jl_data('stats.jl')
for data in jl_data:
    site = re.split(r'\.',data['site'])[0]
    data['site'] = site
    print(site)



@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=jl_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/data')
def data():
    return render_template("data.html", posts = jl_data)

@app.route('/barchart')
def barchart():
    return render_template("barchart.html", posts = jl_data)

@app.route('/stackchart')
def stackchart():
    return render_template("stackchart.html", posts = jl_data)

@app.route('/date')
def dateSelector():
    return render_template("dateSelector.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)



