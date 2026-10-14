from basemodel import BaseModel

class Book(BaseModel):
    def __init__(self, id, title, author, category, available_copies):
        self._id = id
        self._title = title
        self._author = author
        self._category = category
        self._available_copies = available_copies
    
    def to_dict(self):
        return {
            "book_id": self._id,
            "title": self._title,
            "author": self._author,
            "category": self._category,
            "available_copies": self._available_copies
        }