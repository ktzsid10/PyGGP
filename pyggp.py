# -*- coding: utf-8 -*-

"""
Copyright 2017 Walter José

This file is part of the PyGGP Algorithm.

The PyGGP is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

PyGGP is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. See http://www.gnu.org/licenses/.

"""

from grammar import *
from bnf_tree import *
from ggpconfig import *
from ggp import *
from selection import *		

class PYGGP:

	def __init__(self,ff,sf=survival,sf_args=None,population=100,generations=100,mut_rate=90,cross_rate=90,
		grammar='grammar.bnf'):
		self.config = GGPconfig(pop=population,gen=generations,mr=mut_rate,cr=cross_rate)
		self.grammar = grammar
		self.rules,self.start = read_grammar(grammar)
		self.data = GGP(self.rules,self.start,self.config)
		self.fitness_function = ff
		self.selection_function = sf
		self.selection_function_args = sf_args
		
	def _showRules(self):
		print self.rules

	def _calculateProba(self):
		probabilities(self.rules,self.start)

	def _run(self):
		self.data._generatePopulation()
		self.data._printPopulation()
		
		#Calculate fitness for each individual, if fitness already calculated use older value
		self.data._calculatePopFitness(self.fitness_function)
		self.data._applySelection(self.selection_function,self.selection_function_args)	
		print "Before Crossover"
		self.data._printPopulation()
		self.data._applyCrossover()
		print "After Crossover"
		self.data._printPopulation()

def fitness(individual):
	expr = individual.split()
	if(expr[1]=='+'):
		return int(expr[0])+int(expr[2])
	elif (expr[1]=='*'):
		return int(expr[0])*int(expr[2])
	elif (expr[1]=='/'):
		return int(expr[0])/int(expr[2])
	elif (expr[1]=='-'):
		return int(expr[0])-int(expr[2])
	

def main():

	pyGGP = PYGGP(fitness,population=10,grammar='grammarSum.txt')
	#pyGGP._showRules()
	#pyGGP._calculateProba()
	pyGGP._run()

if __name__ == "__main__":

	main()


