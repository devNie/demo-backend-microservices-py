from datetime import date
from enum import Enum


class Book:
    class Errors(Enum):
        NoSuchAuthor = 0

    def __init__(self, title: str, authors: list[str], desc: str, published_date: date, price: float):
        self._title = title
        self._authors = authors
        self._desc = desc
        self._pub_date = published_date
        self._price = price

    # getters and setters

    def change_title(self, new_title: str) -> None:
        self._title = new_title

    def get_title(self) -> str:
        return self._title.title()

    def change_authors(self, new_authors: list[str]) -> None:
        self._authors = new_authors

    def add_author(self, new_author: str) -> None:
        self._authors.append(new_author)

    def remove_author(self, author: str) -> type[Errors.NoSuchAuthor] | None:
        try:
            self._authors.remove(author)
        except ValueError:
            return Book.Errors.NoSuchAuthor

    def get_authors(self) -> list[str]:
        return self._authors

    def change_desc(self, new_desc: str) -> None:
        self._desc = new_desc

    def get_desc(self) -> str:
        return self._desc.strip()

    def change_publishing_date(self, new_date: date) -> None:
        self._pub_date = new_date

    def get_publishing_date(self) -> date:
        return self._pub_date

    def change_price(self, new_price: float) -> None:
        self._price = new_price

    def get_price(self) -> float:
        return self._price
