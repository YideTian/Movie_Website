#-*- coding: UTF-8 -*-
import sys

import webbrowser
import os
import re

reload(sys)
sys.setdefaultencoding('utf-8')

# A single movie entry html template
movie_tile_content = '''
   <div class="col-md-4 col-lg-3 movie-tile " data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" width="250" height="386" class="reflex itiltnone" alt="" />
        <h2 class="movie-title">{movie_title}</h2>
</div>
'''
movie_list_content = '''
    <ul class="nav bs-docs-sidenav  movie-nav"> 
        <li>{movie_title}</li>
    </ul>
'''

def create_movie_tiles_content(movies):
    """The HTML content for this section of the page, identified the movie id from the imdb source """

    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=vi)[0-9]+', movie.trailer_url)
        #Modified: 20171027 Change the regular expression to math the imdb trailer_url.
        #Also changed the <iframe> block of the Template.html
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def create_movie_list_content(movies):
    """The HTML content for this section of the page"""
    content = ''
    for movie in movies:
        content += movie_list_content.format(
            movie_title=movie.title
        )
    return content


def open_movies_page(movies):
    """Create or overwrite the output file"""

    output_file = open('fresh_tomatoes.html', 'w')
    html_file = open('Template.html', 'r').read()

    # Replace the movie tiles placeholder generated content
    rendered_content = html_file.format(movie_tiles=create_movie_tiles_content(movies),
                                        movie_list=create_movie_list_content(movies))
    print (rendered_content)
    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)



