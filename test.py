from main import BlockChain, BlockCode

bc = BlockChain()

bc.add_block("This block is my first one")

bc.add_block("Second block")

# bc.display()

# print(bc.is_valid())

block_json = bc[0].serialize()

print(BlockCode.deserialize(block_json))

# import json

# json_data = json.dumps(bc, default=lambda o: o.__dict__, indent=4)
# print(json_data)

# print(**json.loads(json_data))
