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
from bnf_tree import *

class GGPdata:

	def __init__(self,rules,start,config):
		self.rules=rules
		self.start=start
		self.config=config
		self.population=[]

	def _printPopulation(self):
		count = 0
		for ind in self.population:
			print "Ind "+str(count)+": "+ind._getExpression()
			count+=1

	def _generatePopulation(self):

		if(len(self.population)>0):
			self.population.clear()

		for i in range(0,self.config.population_size):
			tree=create_Tree(self.rules,self.start)
			self.population.append(tree)
