from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_page = response.text
soup = BeautifulSoup(yc_page, 'html.parser')

articles = soup.find_all(name='a', class_='titlelink')

up_votes = soup.find_all(name='span', class_='score')

article_text = [article_tag.getText() for article_tag in articles]
article_links = [article_tag.get('href') for article_tag in articles]
article_upvotes = [int(vote.getText().split()[0]) for vote in up_votes]

print(article_text)
print(article_links)
print(article_upvotes)

max_voted_article = article_text[article_upvotes.index(max(article_upvotes))]

print(f"Maximum voted article is : {max_voted_article} "
      f"the link is \n{article_links[article_upvotes.index(max(article_upvotes))]}")
