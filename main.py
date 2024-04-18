from flask import Flask, render_template, request, redirect, send_file
from extractors.extractors import get_jobs
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


app = Flask("Novel_Free")

@app.route("/")
def home():
  return render_template("home.html", name="yunjae")
db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword is None or keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = get_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

if __name__ == "__main__":
    app.run("0.0.0.0")
