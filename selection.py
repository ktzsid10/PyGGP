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

from random import randint
import copy

def survival(data,*args):
	new_population = []
	for i in range(0,len(data.population)):
		opponent = randint(0,len(data.population)-1)
		while opponent == i:
			opponent = randint(0,len(data.population)-1)

		to_append = i

		if(data._getFitnessIndex(i)<data._getFitnessIndex(opponent)):
			to_append = opponent

		new_population.append(copy.deepcopy(data.population[to_append]))

	return new_population