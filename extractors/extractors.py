import requests
from bs4 import BeautifulSoup
import re
import urllib.request


# def get_jobs_naver(keywords):
#     url_naver = f'https://series.naver.com/search/search.series?t=all&fs=novel&q={keywords}'
#     response_naver = requests.get(url_naver)
#     soup_naver = BeautifulSoup(response_naver.content, "html.parser")
#     jobs_naver = soup_naver.find_all("div", class_="bs")
#     jobs_db_naver = []
#     for job in jobs_naver:
#         title_raw = job.find('a', class_="N=a:nov.title").text.strip()  # 제목 원본
#         title = re.sub(r'\([^)]*\)', '', title_raw).strip()  # (총 xxx화/미완결) 제거
#         stars = job.find("em", class_="score_num").text
#         author = job.find("span", class_="author").text           
#         series = job.find("span", class_="ellipsis").text
#         free = job.find('span', class_='free_info').find('span').text
#         image_tag = job.find('img', src=True)
#         image_url = image_tag['src']

#         job_data = {"image_url":image_url,"title": title, "stars": stars, "author": author,
#                     "series": series, "free": free
#                     }
#         jobs_db_naver.append(job_data)
#         return jobs_naver
    
    
def get_jobs_kakao(keywords):
    url_kakao = f'https://page.kakao.com/search/result?keyword={keywords}'
    response_kakao = requests.get(url_kakao)
    soup_kakao = BeautifulSoup(response_kakao.content, "html.parser")
    jobs_kakao = soup_kakao.find_all('div', class_="flex items-center")
    jobs_db_kakao = []
    for job in jobs_kakao:
        #title = job.find('a', class_="tit_main").text.strip()
        #author = job.find('div', class_="auth_main").text.strip()
        #series = job.find('div', class_="series_main").text.strip()
        #free = job.find('span', class_='tag_free').text.strip()
        img_tag = job.find("div",class_ = "jsx-3806193842 image-container relative h-full w-full").find("img",src=True)
        image_url=img_tag['src']
        # job_data = {
        #     "title": title,
        #     "author": author,
        #     "series": series,
        #     "free": free
        # }
        job_data = {
            "title": None,
            "author": None,
            "series": None,
            "free": None,
            "image_url":image_url
        }
        jobs_db_kakao.append(job_data)

    return jobs_db_kakao

print(get_jobs_kakao("명군이 되어보세"))