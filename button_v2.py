from ethereum import tester
from ethereum import utils

s = tester.state()

#address 0 is the pool, 1 for player 1 and 2 for player 2
public_k0 = utils.privtoaddr(tester.k0)
public_k1 = utils.privtoaddr(tester.k1)
public_k2 = utils.privtoaddr(tester.k2)

print '******************************************************'
print 'Welcome to the Reddit button using serpent version 2'
print "balance of pool", (s.block.get_balance(public_k0)) 
print "balance of player 1", (s.block.get_balance(public_k1)) 
print "balance of player 2", (s.block.get_balance(public_k2)) 
print 'Press 1 for player 1 click the button'
print 'Press 2 for player 2 click the button'
print '******************************************************'

lastBlock = 0
lastPlayer = 0

while (s.block.number -  lastBlock < 3):
  action = raw_input('The action : ')
  if action == "1" and s.block.get_balance(public_k1) > 100000000000000000000000:
    s.send(tester.k1, public_k0, 100000000000000000000000)
    lastPlayer = "1"
    lastBlock = s.block.number
    print "player 1 pressed"
  if action == "2" and s.block.get_balance(public_k2) > 100000000000000000000000:
    s.send(tester.k2, public_k0, 100000000000000000000000)
    lastPlayer = "2"
    lastBlock = s.block.number
    print "player 2 pressed"
  if action == "mine":
    s.mine(number_of_blocks=1)  

  print "State of blockchain", s.block.number
  print "last block", lastBlock
  print "balance of the pool", (s.block.get_balance(public_k0)) 
  print "balance of player 1", (s.block.get_balance(public_k1)) 
  print "balance of player 2", (s.block.get_balance(public_k2)) 
  print '******************************************************'

print "winner is", lastPlayer
