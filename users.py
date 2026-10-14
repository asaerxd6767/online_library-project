from basemodel import BaseModel

class User(BaseModel):
    def __init__(self, id, name, email):
        self._id = id
        self._name = name
        self._email = email
    
    def to_dict(self):
        return {
            'user_id': self._id,
            'name': self._name,
            'email': self._email
        }