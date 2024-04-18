import requests
from bs4 import BeautifulSoup
import re
import urllib.request


def get_jobs(keywords):
    url_naver = f'https://series.naver.com/search/search.series?t=all&fs=novel&q={keywords}'
    response_naver = requests.get(url_naver)
    soup_naver = BeautifulSoup(response_naver.content, "html.parser")
    jobs = soup_naver.find_all("div", class_="bs")
    jobs_db = []
    for job in jobs:
        title_raw = job.find('a', class_="N=a:nov.title").text.strip()  # 제목 원본
        title = re.sub(r'\([^)]*\)', '', title_raw).strip()  # (총 xxx화/미완결) 제거
        stars = job.find("em", class_="score_num").text
        author = job.find("span", class_="author").text           
        series = job.find("span", class_="ellipsis").text
        free = job.find('span', class_='free_info').find('span').text
        image_tag = job.find('img', src=True)
        image_url = image_tag['src']

        job_data = {"image_url":image_url,"title": title, "stars": stars, "author": author,
                    "series": series, "free": free
                    }
        jobs_db.append(job_data)
        
    
    url_kakao = f'https://page.kakao.com/search/result?keyword={keywords}'
    response_kakao = requests.get(url_kakao)
    soup_kakao = BeautifulSoup(response_naver.content, "html.parser")
    jobs = soup_kakao.find_all("div", class_="bs")
    jobs_db = []
    for job in jobs:
        title_raw = job.find('a', class_="N=a:nov.title").text.strip()  # 제목 원본
        title = re.sub(r'\([^)]*\)', '', title_raw).strip()  # (총 xxx화/미완결) 제거
        stars = job.find("em", class_="score_num").text
        author = job.find("span", class_="author").text           
        series = job.find("span", class_="ellipsis").text
        free = job.find('span', class_='free_info').find('span').text
        image_tag = job.find('img', src=True)
        image_url = image_tag['src']

        job_data = {"image_url":image_url,"title": title, "stars": stars, "author": author,
                    "series": series, "free": free
                    }
        jobs_db.append(job_data)
    return jobs_db
