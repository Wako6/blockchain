from main import BlockChain

bc = BlockChain()

bc.add_block("This block is my first one")

bc.add_block("Second block")

bc.display()

print(bc.is_valid())
