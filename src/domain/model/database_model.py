from abc import ABCMeta, abstractmethod, abstractproperty
import uuid
import json
from datetime import datetime

class IDatabaseModel:
    __metaclass__ = ABCMeta
    _id: str
    created_at: datetime
    updated_at: datetime

    @abstractmethod
    def __init__(self):
        self._id = str(uuid.uuid4())
        utcNow = datetime.utcnow()

        self.created_at = utcNow
        self.updated_at = utcNow

    @abstractmethod
    def to_dict(self): raise NotImplemented

    @abstractmethod
    def to_json(self): raise NotImplemented

    @classmethod
    def version(self): return '1.0'