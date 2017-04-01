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

class GGPconfig:

	def __init__(self,pop=100,gen=100,mr=90,cr=90):
		self.population_size = pop
		self.generations = gen
		self.mutation_rate = mr
		self.crossover_rate = cr