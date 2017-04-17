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
from progress import *

class PYGGP:

	def __init__(self,ff,sf=survival,sf_args=None,population=100,generations=100,mut_rate=90,cross_rate=90,
		es=2,grammar='grammar.bnf'):
		self.config = GGPconfig(pop=population,gen=generations,mr=mut_rate,cr=cross_rate)
		self.grammar = grammar
		self.rules,self.start = read_grammar(grammar)
		self.data = GGP(self.rules,self.start,self.config)
		self.fitness_function = ff
		self.selection_function = sf
		self.selection_function_args = sf_args
		if(es%2!=0):
			es+=1
		self.elitism_size = es
		
	def _showRules(self):
		print self.rules

	def _calculateProba(self):
		probabilities(self.rules,self.start)

	def _run(self):
		self.data._generatePopulation()
		print "Initial Population"
		self.data._printPopulation()
		print "\n"
		
		#Calculate fitness for each individual, if fitness already calculated use older value
		for i in range(0,self.data.config.generations):
			printProgress (i+1,self.data.config.generations, prefix = 'Processing '+str(i+1)+' of '+str(self.data.config.generations))
			self.data._calculatePopFitness(self.fitness_function)
			if(self.elitism_size>0):
				self.data._separateKbest(self.elitism_size)
			self.data._applySelection(self.selection_function,self.selection_function_args)	
			self.data._applyCrossover()
			self.data._applyMutation()

			if(self.elitism_size>0):
				self.data._concatKbest()

		print "\nBest 5 Individuals:"
		count = 0

		for key,value in self.data._getBestFitness().items():
			print key+" Fitness: "+str(value)
			if count>4:
				break
			count+=1
