import datetime
import hashlib
import json


class Block:

    def __init__(self, previous_hash, content, index="N/A", *args, **kwargs):
        self._previous_hash = previous_hash
        self._content = content
        self._index = index
        self._datetime = str(datetime.datetime.now())
        self._hash = self.get_hash()

    def __str__(self):
        return f"index: {self._index}\n" \
               f"datetime: {self._datetime}\n" \
               f"previous_hash: {self._previous_hash}\n" \
               f"hash: {self._hash}\n" \
               f"content: {self._content}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        self_dict = self.serialize(to_json=False)
        other_dict = other.serialize(to_json=False)

        return all((other_dict.get(k) == v for k, v in self_dict.items()))

    def get_hash(self):
        data = {
            "index": self._index,
            "datetime": self._datetime,
            "previous_hash": self._previous_hash,
            "content": self._content
        }

        encoded_block = json.dumps(data, sort_keys=True).encode()

        return hashlib.sha256(encoded_block).hexdigest()

    @property
    def previous_hash(self):
        return self._previous_hash

    @previous_hash.setter
    def previous_hash(self, previous_hash):
        self._previous_hash = previous_hash
        self._hash = self.get_hash()

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content
        self._hash = self.get_hash()

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self._index = index
        self._hash = self.get_hash()

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        self._datetime = datetime
        self._hash = self.get_hash()

    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, hash):
        self._hash = self.get_hash()

    def serialize(self, to_json=True):
        block_data = {
            "previous_hash": self._previous_hash,
            "content": self._content,
            "index": self._index,
            "datetime": self._datetime,
            "hash": self._hash
        }

        if to_json:
            block_data = json.dumps(block_data, indent=4, sort_keys=True)

        return block_data

    @classmethod
    def deserialize(cls, block_data: str | dict):
        if type(block_data) is str:
            block_data = json.loads(block_data)

        block = cls("0", "[Genesis Block]")

        block._previous_hash = block_data.get("previous_hash")
        block._content = block_data.get("content")
        block._index = block_data.get("index")
        block._datetime = block_data.get("datetime")
        block._hash = block.get_hash()

        return block
