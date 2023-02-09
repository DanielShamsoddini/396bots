# 396bots
Hatebot

This is a program for Assignment 5 for Northwestern University's CS396: Artificial Life

It is heavily based on the ludobots MOOC on https://www.reddit.com/r/ludobots/ created by Professor Josh Bongard


My version however is a simple pet animalesque robot that moves towards a certain block it is programmed to hate and aims to collide with it

Its fitness function is given by
	
	fitness = -numpy.sqrt(numpy.sum(( numpy.array(self.bigblock) - numpy.array(positionOfLinkZero[:2]))**2)) + self.ifHit
  
  or in simpler terms
  
  	the fitness equals the distance between the value in the bigblock variable and the robots final position plus a sizeable positive modifier if the bot collides with the block while the bot is "alive"
		
