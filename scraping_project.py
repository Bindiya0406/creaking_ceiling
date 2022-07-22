from bs4 import BeautifulSoup
import requests
from random import choice

base_url="http://quotes.toscrape.com"

url="/page/1/"
counter=1
quotes_data=[]
while url:
	response=requests.get(base_url+url)
	soup=BeautifulSoup(response.text,"html.parser")
	quotes=soup.find_all(class_="quote")
	
	for quote in quotes:
		quotes_data.append({
			"quote_text":quote.find(class_="text").get_text(),
			"author":quote.find(class_="author").get_text(),
			"author_link":quote.find("a")["href"]


			})
	next_page=soup.find(class_="next")
	
	url=next_page.find("a")["href"] if next_page else None



def game():
	quote=choice(quotes_data)
	guess=''
	remaining_guesses=4
	print("Here's a quote")
	print(quote["quote_text"])
	print(quote["author"])
	while guess.lower()!=quote["author"].lower() and remaining_guesses>0:
		guess=input(f"who said this quote? Remaining Guesses:{remaining_guesses}\n")
		remaining_guesses=remaining_guesses-1
		if guess.lower()==quote["author"].lower():
			print("YAY you got it right")
		elif remaining_guesses==3:
			response=requests.get(base_url+quote["author_link"])
			soup=BeautifulSoup(response.text,"html.parser")
			birth_date=soup.find(class_="author-born-date").get_text()
			birth_place=soup.find(class_="author-born-location").get_text()
			print(f"Here's a hint:The author was born on {birth_date} {birth_place}")
		elif remaining_guesses==2:
			first_letter=quote["author"][0]
			print(f"Here's a hint:the author's first name starts with {first_letter}")
		elif remaining_guesses==1:
			first_letter=quote["author"].split(" ")[1][0]
			print(f"Here's a hint:the author's last name starts with {first_letter}")
		else:
			author=quote["author"]
			print(f"You lost....The anuthor was:{author}")
			
	again=''
	while again.lower() not in ("y","yes","n","no"):
	 again=input("Do you want to play again y/n?")
	if again.lower() in ("y","yes"):
		print("OK YOU PLAY AGAIN")
		game()
	    
	
	else:
		print("OK,BYE")
	

game()


	








		
	


