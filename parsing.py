from bs4 import BeautifulSoup
import requests, sqlite3

conn = sqlite3.connect('contact.db')
curs = conn.cursor()
curs.execute("CREATE TABLE Information (Email NVARCHAR(50), Instagram NVARCHAR(100), Facebook NVARCHAR(100), Address NVARCHAR(100))")

response = requests.get('http://ninochkheidze.ge/contact-me/')

soup = BeautifulSoup(response.text, "html.parser")

section = soup.find('div', {'class':'entry-content'})
info = section.find_all("li")

email = info[0].text
instagram = info[1].text
facebook = info[2].text
address = info[3].text

curs.execute("INSERT INTO Information values (?, ?, ?, ?)", (email, instagram, facebook, address))
conn.commit()
conn.close()



