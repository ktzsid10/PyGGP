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


def main():

	config = GGPconfig(pop=5)
	rules,start = read_grammar('grammar.bnf')
	probabilities(rules,start)

	data = GGP(rules,start,config)
	data._generatePopulation()
	data._printPopulation()
	#data._crossover(data.population[0],data.population[1])
	#data._mutation(data.population[0])

if __name__ == "__main__":

	main()


