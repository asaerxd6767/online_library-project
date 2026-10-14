from basemodel import BaseModel

class Rating(BaseModel):
    def __init__(self, user_id, book_id, score, review):
        if 10 <= score <= 1:
            raise ValueError('score should be between 1 and 10')
        self._user_id = user_id
        self._book_id = book_id
        self._score = score
        self._review = review
        
    def to_dict(self):
        return {
            'user_id': self._user_id,
            'book_id': self._book_id,
            'score': self._score,
            'review': self._review
        }