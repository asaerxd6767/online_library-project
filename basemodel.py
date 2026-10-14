from abc import ABC, abstractmethod

class BaseModel(ABC):
    
    @abstractmethod
    def to_dict(self) -> dict:
        # I will need for every class to use this method
        pass