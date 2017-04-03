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

class GGP:

	def __init__(self,rules,start,config):
		self.rules=rules
		self.start=start
		self.config=config
		self.population=[]
		self.fitness={}

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

	def _crossover(self,ind1,ind2):

		#Calculate the nodes intersection between the individuals
		apply_cross = randint(0,100)
		if(apply_cross<self.config.crossover_rate):
			intersection = list(ind1.nodes.viewkeys() & ind2.nodes.viewkeys())
			node_apply = intersection[randint(0,len(intersection)-1)]		

			if node_apply == self.start:
				ind1.nodes[node_apply],ind2.nodes[node_apply] = ind2.nodes[node_apply],ind1.nodes[node_apply]
			else:
				parent1 = ind1.nodes[node_apply].parent
				parent2 = ind2.nodes[node_apply].parent

				child1 = ind1.nodes[node_apply]
				child2 = ind2.nodes[node_apply]

				parent1._replaceChild(child1,child2)
				parent2._replaceChild(child2,child1)

				#ind1.nodes[node_apply],ind2.nodes[node_apply] = ind2.nodes[node_apply],ind1.nodes[node_apply]
				ind1._updateNodes()
				ind2._updateNodes()


	def _printFitness(self):

		for key,value in self.fitness.items():

			print key+" "+str(value)

	def _calculatePopFitness(self,fitness_function):
		for ind in self.population:
			if(ind._getExpression() not in self.fitness):
				fit = fitness_function(ind._getExpression())
				self.fitness[ind._getExpression()]=fit		

	def _getFitness(self,ind):
		return self.fitness[ind._getExpression()]

	def _applySelection(self,selection_function,sf_args):
		self.population = selection_function(self,sf_args)

	def _applyCrossover(self):
		for i in xrange(0,len(self.population),2):
			self._crossover(self.population[i],self.population[i+1])

	def _getFitnessIndex(self,index):
		return self.fitness[self.population[index]._getExpression()]

	def _setFitness(self,ind,value):
		self.fitness[ind._getExpression()]=value

	def _mutation(self,ind):

		apply_mutation = randint(0,100)
		if(apply_mutation<self.config.mutation_rate):
			nodes = list(ind.nodes.viewkeys())
			node_apply = nodes[randint(0,len(nodes)-1)]
			
			mutateTree(self.rules,ind.nodes[node_apply],ind)
