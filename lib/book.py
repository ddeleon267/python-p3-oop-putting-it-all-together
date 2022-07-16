#!/usr/bin/env python3
class Book:
    def __init__(self, title):
        self.title = title

    def get_author_name(self):
        return self._author_name

    # def set_author_name(self, author_name):
    #     self._author_name = author_name

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        self._page_count = page_count

    # def get_genre(self):
    #     return self._genre

    # def set_genre(self, genre):
    #     self._genre = genre

    

    # author_name = property(get_author_name, set_author_name)
    page_count = property(get_page_count, set_page_count)
    # genre = property(get_genre, set_genre)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")