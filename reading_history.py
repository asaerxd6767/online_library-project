from basemodel import BaseModel
from datetime import datetime

class ReadingHistory(BaseModel):
    def __init__(self, user_id, book_id, date, status):
        self._user_id = user_id
        self._book_id = book_id
        self._date = date or datetime.now().strftime("%Y-%m-%d")
        self._status = status
    
    def to_dict(self):
        return {
            'user_id': self._user_id,
            'book_id': self._book_id,
            'status': self._status,
            'date': self._date
        }