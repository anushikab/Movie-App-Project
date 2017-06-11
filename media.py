# media.py is the classMedia() file, a blueprint for the review website.
# This code was tested by PEP8, a de facto standard of Python

import webbrowser
"""provides interface to allow displaying Web-based documents to users"""


class Movie():
    """This class provides a way to store more related information
    We will define a function for the class Movie that creates a new
    instance of the class. The __init__ function creates space
    for that instance. The instance will have the format:
    movie_title, movie_storyline, poster_image and trailer_youtube.
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
