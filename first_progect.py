import requests
from bs4 import BeautifulSoup
import json

HOST = "https://www.asos.com/ru/women/" # константа домин который парсим
URL = "https://www.asos.com/ru/women/dzhinsy/cat/?cid=3630&currentpricerange=550-19490&nlid=ww%7C%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0%7C%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D0%BF%D0%BE%20%D1%82%D0%B8%D0%BF%D1%83%20%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B0%7C%D0%B4%D0%B6%D0%B8%D0%BD%D1%81%D1%8B&refine=attribute_10155:6764|attribute_1047:8393|brand:401" #константа, адрес который передается на сервер
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
} # чтобы сайт не подумал что я бот, мне нужно пробрасывать заголовки  заголовки, что это такое?
# Парсинг в функциональном стиле так как это проще. Без классов ООП
def get_html(url): # обращение к странице, чтобы получить содержимое страницы HTML
    response = requests.get(url, headers=HEADERS) # используется когда js не мешает функционалу сайта
    return response

def get_content(html): # получает контент(картинку)
    soup = BeautifulSoup(html, "html.parser")
    conteiner = soup.find_all("a", class_ = "_3TqU78D")#soup.select("a._3TqU78D")
    res = []
    for image in conteiner:
        res.append(image.get("href"))
        return res

html = get_html(URL)
get_content(html.text)


