from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

greatest_100_films = []

for films in movies:
    greatest_films = films.getText()
    greatest_100_films.append(greatest_films)

#get_position = [int(pos.split()[0].split(")")[0]) for pos in greatest_100_films]

greatest_100_films.reverse()
#print(greatest_100_films)

with open(file="movies.txt", mode="w") as movies:

    for i in greatest_100_films:
        movies.write(i + "\n")