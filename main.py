import datetime
import hashlib
import json


class BlockCode:

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


class BlockChain:

    def __init__(self, genesis_message="[Genesis Block]"):
        self.chain = []
        genesis_block = BlockCode("0", genesis_message, index=1)
        self.chain.append(genesis_block)

    def add_block(self, content):
        block = BlockCode(self.chain[-1].hash,
                          content,
                          index=len(self.chain) + 1)
        self.chain.append(block)

    def display(self):
        for i, block in enumerate(self.chain):
            if i != 0:
                print()
            print(block)

    def is_valid(self):
        iterator = iter(self.chain)
        previous_block = next(iterator)

        while True:
            try:
                block = next(iterator)
            except StopIteration:
                break

            if block.previous_hash != previous_block.hash:
                return False

            previous_block = block

        return True

    def serialize(self):
        pass

    @staticmethod
    def deserialize():
        pass
