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

from collections import deque

def read_grammar(filename):

	"""
    Read grammar based in a bnf file
    """

	rules = {}
	first = ""

	with open(filename,'r') as f_in:

		lines = filter(None, (line.rstrip() for line in f_in))
		first = lines[0].split('->')[0].strip()
		for line in lines:
			parent,childs = line.strip().split('->')
			parent = parent.strip()
			groups = childs.split('|')

			rules[parent]=[]
			for group in groups:
				rules[parent].append(group.split())

	return rules,first

def analise_probabilities(rules, start):

	to_calc = deque()
	to_calc.append(start)
	probabilites = {}

	probabilites[start]=100

	while to_calc:
		parent = to_calc.popleft()
		if(parent in rules):
			childs = rules[parent]
		else:
			continue

		if(len(childs)>1):
			proba = probabilites[parent]/len(childs)
		else:
			proba = probabilites[parent]

		for child in childs:
			for grandson in child:
				if(grandson.startswith('[')):
					grandson = grandson.replace('[','').replace(']','')
					probabilites[grandson]=proba/2
				else:
					probabilites[grandson]=proba
				to_calc.append(grandson)

	print probabilites