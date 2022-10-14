from django.core.management.base import BaseCommand
from home_work27_django.ads.models import Ad
import json



class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('../ads.json', 'rb') as f:
            data = json.load(f)

            for i in data:
                print(i)
                ad = Ad()
                ad.name = i
                ad.save()

        print('finished')

# import sqlite3
#
# # Если в текущей директории нет файла db.sqlite -
# # он будет создан; сразу же будет создано и соединение с базой.
# # Если файл существует, функция connect просто подключится к базе.
# con = sqlite3.connect('db.sqlite')
#
# # Создаём специальный объект cursor для работы с БД.
# # Вся дальнейшая работа будет вестись через методы этого объекта.
# cur = con.cursor()
#
# # Готовим SQL-запросы.
# # Для читаемости кода запрос обрамлён в тройные кавычки и разбит построчно.
# cur.execute('''
# CREATE TABLE IF NOT EXISTS ads(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     bithday_year INTEGER
# );
# ''')
# cur.execute('''
# CREATE TABLE IF NOT EXISTS movies(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     type TEXT,
#     release_year INTEGER
# );
# ''')
#
# # Применяем запросы.
# # Запросы, переданные в cur.execute(), не будут выполнены до тех пор,
# # пока не вызван метод commit().
# con.commit()
# # Закрываем соединение с БД.
# con.close()



# import urllib.request
#
# con = sqlite3.connect("db.sqlite3")
#
#
# def get_feed(feed_url):
#     req = urllib.request.Request(feed_url, headers={"User-Agent": "Xe/feedfetch"})
#     with urllib.request.urlopen(req) as response:
#         cur = con.cursor()
#         body = response.read()
#         cur.execute("""
#            INSERT INTO jsonfeed_raw
#              (feed_url, raw)
#            VALUES
#              (?, json(?))
#         """, (feed_url, body))
#         con.commit()
#         print("got feed %s" % (feed_url))
#
# get_feed("https://christine.website/blog.json")