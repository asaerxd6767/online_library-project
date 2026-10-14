from basemodel import BaseModel

class Category(BaseModel):
    def __init__(self, id, name):
        self._id = id
        self._name = name
        
    def to_dict(self):
        return {
            'category_id': self._id,
            'name': self._name
        }