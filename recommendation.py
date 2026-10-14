class Recommendation:
    def __init__(self, user_id, book_id, reason, score):
        self._user_id = user_id
        self._book_id = book_id
        self._reason = reason
        self._score = score