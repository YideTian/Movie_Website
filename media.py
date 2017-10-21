#-*- coding: UTF-8 -*-
import webbrowser

class Movie():

#构造函数，self即被创建的实例本身
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer

    def show_title(self):
        print self.title

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

    # def show_poster(self):
    #     webbrowser.open(self.poster_image_url)
