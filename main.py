import datetime
import hashlib
import json


class BlockCode:

    def __init__(self, previous_hash, content):
        self.previous_hash = previous_hash
        self.content = content
        self.index = "N/A"
        self.datetime = str(datetime.datetime.now())
        self.hash = self.hash()

    def __str__(self):
        return f"index: {self.index}\n" \
               f"datetime: {self.datetime}\n" \
               f"previous_hash: {self.previous_hash}\n" \
               f"hash: {self.hash}\n" \
               f"content: {self.content}"

    def hash(self):
        block_data = {
            "index": self.index,
            "datetime": self.datetime,
            "previous_hash": self.previous_hash,
            "content": self.content
        }
        encoded_block = json.dumps(block_data, sort_keys=True).encode()

        return hashlib.sha256(encoded_block).hexdigest()

    @previous_hash.setter
    def previous_hash(self, previous_hash):
        self.previous_hash = previous_hash
        self.hash = self.hash()

    @content.setter
    def content(self, content):
        self.content = content
        self.hash = self.hash()

    @index.setter
    def index(self, index):
        self.index = index
        self.hash = self.hash()

    @datetime.setter
    def datetime(self, datetime):
        self.datetime = datetime
        self.hash = self.hash()

    @hash.setter
    def hash(self, hash):
        self.hash = self.hash()


class TextBlock(BlockCode):

    def __init__(self, previous_block_hash, text, **kwargs):
        super().__init__(self, previous_block_hash, text, **kwargs)


class BlockChain:

    def __init__(self, genesis_message="Genesis Block"):
        self.chain = []
        self.chain.append(TextBlock("0", genesis_message, 1))

    def add_block(self, block: BlockCode):
        block.index = len(self.chain) + 1
        self.chain.append(block)

    def display(self):
        for block in self.chain:
            print(block)
