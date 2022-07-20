import requests
from bs4 import BeautifulSoup
from csv import writer
base_url="https://www.rithmschool.com"

counter=1

url=base_url+'/blog'
with open("blog_data_full.csv","w") as csv_file:
		csv_writer=writer(csv_file)
		csv_writer.writerow(["Title","Date","Link"])
		while counter!=0:

			response=requests.get(url)
			soup=BeautifulSoup(response.text,"html.parser")
			if soup.find(class_="next"):
				url_next=soup.find(class_="next").findChild("a")["href"]
			else:
				counter=0
				
			
			
			articles=soup.find_all("article")
			#print(articles)
			for article in articles:
					title=article.find("a").get_text()
					link=article.find("a")["href"]
					date=article.find("time")["datetime"]
					csv_writer.writerow([title,date,link])
			url=base_url+url_next
			
			

				
		            
		    

	
	



	