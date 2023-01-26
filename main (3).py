import requests
from bs4 import BeautifulSoup as Soup
import os

counter = 0
link = input("Введите ссылку на статью: ")
urls = []

folderName = link.split("/")[-1]
os.mkdir(str(folderName))

response = requests.get(link)
soup = Soup(response.content, 'html.parser')

listLink = soup.find_all('img')
for links in listLink:
    urls.append(str(links["src"]))
urls.remove(urls[-0])

print(f"Found {len(urls)} images!")

def get_file(url):
    name = url.split('/')[-2]
    response = requests.get(url, stream=True)
    return name, response

def save_data(name, file_data,folderName):
    print(f"Image - {name} saving!")
    file = open(f"{folderName}/{name}", 'bw')
    for chunk in file_data.iter_content(4096):
        file.write(chunk)
    print(f"Image - {name} saved!")

for url in urls:
    name, response = get_file(url)
    save_data(name,response,folderName)
    print()
    counter += 1

print(f"Finished succesfuly! {counter} images downloaded!")