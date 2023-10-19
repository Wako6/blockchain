import json
from pathlib import Path

from .block import Block


class BlockChain:
    save_extension = ".json"

    def __init__(self, genesis_message="[Genesis Block]"):
        self.chain = []
        genesis_block = Block("0", genesis_message, index=1)
        self.chain.append(genesis_block)

    def __getitem__(self, index):
        return self.chain[index]

    def add_block(self, content):
        block = Block(self.chain[-1].hash, content, index=len(self.chain) + 1)
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

            is_valid_previous_hash = (block.previous_hash
                                      != previous_block.hash)

            is_valid_hash = (block.hash != block.get_hash())

            if not is_valid_previous_hash or not is_valid_hash:
                return False

            previous_block = block

        return True

    def serialize(self):
        return json.dumps(
            {
                "chain":
                [block.serialize(to_json=False) for block in self.chain]
            },
            indent=4,
            sort_keys=True)

    @classmethod
    def deserialize(cls, chain_data: str | dict):
        if type(chain_data) is str:
            chain_data = json.loads(chain_data)

        blockchain = BlockChain()
        blockchain.chain = []

        for block_dict in chain_data.get('chain'):
            blockchain.chain.append(Block.deserialize(block_dict))

        return blockchain

    def save(self, filename="blockchain", path="", force=False):
        path = Path(path)

        if not filename.endswith(BlockChain.save_extension):
            filename += BlockChain.save_extension

        if force and not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        if not (path / filename).exists() or force:
            with open(path / filename, "w") as file:
                file.write(self.serialize())
        else:
            raise FileExistsError(
                f"{path / filename} is already exist. You can force the save "
                "for replace it")

    @classmethod
    def load(cls, filepath):

        class BadFormatExtension(Exception):

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

        if not filepath.endswith(BlockChain.save_extension):
            raise BadFormatExtension(
                f"Load function in {cls.__name__} waiting a JSON file")

        filepath = Path(filepath)

        block_data = None
        if filepath.exists():
            with open(filepath, "r") as file:
                block_data = file.read()

        return cls.deserialize(block_data)
