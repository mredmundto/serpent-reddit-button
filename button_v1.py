from ethereum import tester
from ethereum import utils

s = tester.state()
c = s.abi_contract('button.se')

#address 0 is the pool, 1 for player 1 and 2 for player 2
public_k0 = utils.privtoaddr(tester.k0)
public_k1 = utils.privtoaddr(tester.k1)
public_k2 = utils.privtoaddr(tester.k2)

c.register(public_k0, 0)
c.register(public_k1, 10)
c.register(public_k2, 10)

print '******************************************************'
print '*Welcome to the Reddit button using serpent version 1*'
print '*Press 1 for player 1 pressing the button            *' 
print '*Press 2 for player 2 pressing the button            *'
print '*Press mine for mining a new block                   *'
print '******************************************************'

while (c.winner() == 0):
	action = raw_input('The action : ')
	if action == "1": 
		c.pressButton(utils.privtoaddr(tester.k1),public_k0,1, s.block.number)
	if action == "2": 
		c.pressButton(utils.privtoaddr(tester.k2),public_k0,1, s.block.number)
	if action == "mine": 
		s.mine(number_of_blocks=1)
	
	c.checkWinner(utils.privtoaddr(tester.k0), s.block.number)
	print 'current block ', s.block.number
	print 'last block', c.lastBlock()
	print 'Balance for the pool:', c.ask(public_k0)
	print 'Balance for the player 1:', c.ask(public_k1)
	print 'Balance for the player 2:', c.ask(public_k2)
	print '****************************************************'
	

print 'The game is ended'
print 'Balance for the pool:', c.ask(public_k0)
print 'Balance for the player 1:', c.ask(public_k1)
print 'Balance for the player 2:', c.ask(public_k2)
