#-*- coding: UTF-8 -*-

import webbrowser


class Movie():
    """Creating the structure of the movie database for this program"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer):
        # 构造函数，self即被创建的实例本身
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer

    # def show_title(self):
    #     """show_title definition is currently not using for this program"""
    #     print self.title
    #
    # def show_trailer(self):
    #     """show_trailer definition is currently not using for this program"""
    #     webbrowser.open(self.trailer_url)

