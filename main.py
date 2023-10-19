from chain import BlockChain
# from src import Block

bc = BlockChain()

bc.add_block("This block is my first one")

bc.add_block("Second block")

bc.display()

# print(bc.is_valid())

# bc.save(force=True)

# BlockChain.load("blockchain").display()

# chain_json = bc[1].serialize()
# print(Block.deserialize(chain_json))

# chain_json = bc.serialize()
# BlockChain.deserialize(chain_json).display()
