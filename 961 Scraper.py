import bs4
import requests
import time

r = requests.get('https://www.the961.com/latest-news/lebanon-news/').text

soup = bs4.BeautifulSoup(r, 'lxml')
count = 0
for article in soup.find_all('article'):
    count += 1

    title = article.h3.text
    print(f'Title: {title}')

    date = article.find('span', class_='byline-part date')
    if date: print('Date:', date.text)

    author = article.find('span', class_="byline-part author")
    if author: print('Author:', author.text)

    link = article.find('h3', class_='title').a['href']
    link_r = requests.get(link).text

    soup_link = bs4.BeautifulSoup(link_r, 'lxml')
    for page in soup_link.select(".entry-content > p, .entry-content li"):
        print(page.get_text(strip=True, separator=' '))
    print()
    print(f'Article({count}): {link}')
    print("-" * 80)
    time.sleep(0.5)
