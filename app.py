from flask import Flask, render_template, request

app = Flask(__name__)

import pyshorteners

def short_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

def expand_url(url):
    s1 = pyshorteners.Shortener()
    expanded_url = s1.tinyurl.expand(url)
    return expanded_url

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        url = request.form["url"]
        if request.form.get("action") == "shorten":
            result = short_url(url)
        elif request.form.get("action") == "expand":
            result = expand_url(url)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
