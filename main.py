from flask import Flask, render_template, request, redirect, send_file
from extractors.extractors import get_jobs_kakao
#from extractors.extractors import get_jobs_naver
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


app = Flask("Novel_Free")

@app.route("/")
def home():
  return render_template("home.html", name="yunjae")
db_naver = {}
db_kakao = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword is None or keyword == "":
        return redirect("/")
    if keyword in db_kakao:
        jobs_kakao = db_kakao[keyword]
    else:
        jobs_kakao = get_jobs_kakao(keyword)
        db_kakao[keyword] = jobs_kakao
    return render_template("search.html", keyword=keyword, jobs_naver=jobs_kakao)

if __name__ == "__main__":
    app.run("0.0.0.0")
