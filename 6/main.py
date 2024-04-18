from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time 
import csv
class Job:
    def __init__(self,keywords):
        self.keywords=keywords
        self.p=sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto(f'https://www.wanted.co.kr/search?query={self.keywords}&tab=position')
        for i in range(4):
            time.sleep(1)
            self.page.keyboard.down("End")
        self.content=self.page.content()
        self.p.stop()

    def find(self):
        self.soup = BeautifulSoup(self.content,"html.parser")
        self.jobs = self.soup.find_all("div",class_ = "JobCard_container__FqChn")
        self.jobs_db=[]
        for job in self.jobs:
            self.link =f"https://www.wanted.co.kr{job.find('a')['href']}"
            self.title = job.find("strong", class_ ="JobCard_title__ddkwM").text
            self.company_name = job.find("span",class_="JobCard_companyContent__zUT91").text
            self.reward= job.find("span",class_="JobCard_reward__sdyHn").text
            self.job={ " title ": self.title, "company_name":self.company_name,"reard ": self.reward,"link ": self.link}
            self.jobs_db.append(self.job)
        print(self.jobs_db)   
        print(len(self.jobs_db))
        
    def write(self):
        file =open(f'{self.keywords}s.csv','w',encoding='utf-8')
        writter =csv.writer(file)
        writter.writerow(["Title","Company","Reward","Link"])
        for job in self.jobs_db:
            writter.writerow(job.values())
        file.close()
    
    
job_instance = Job("flutter")
job_instance.find()
job_instance.write()

