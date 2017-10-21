#-*- coding: UTF-8 -*-

import media
import fresh_tomatoes
import xl_import

movie_data = xl_import.movie_load()
# print movie_data
# print len(movie_data)
# print movie_data[1]
# print movie_data[1]['title']

movie = {}
for i in range(1, len(movie_data)+1):
    movie[i] = media.Movie(movie_data[i]['title'],
                           movie_data[i]['storyline'],
                           movie_data[i]['poster_image_url'],
                           movie_data[i]['trailer_url']
                           )
movies = []
for i in range(1, len(movie_data)+1):
    movies.append(movie[i])

print movies


fresh_tomatoes.open_movies_page(movies)

