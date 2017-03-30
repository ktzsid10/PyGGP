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

class Node:
    """
    Class Node
    """
    def __init__(self,value,option=False):
        self.data=value
        self.childs = []
        self.optional = option

    def _addChild(self,child):
        self.childs.append(child)

    def _setOptional(self,optional):
        self.optional = optional

class BNFTree:
    """
    Class Tree
    """
    def __init__(self,root='<start>'):
        self.nodes={}
        self.nodes[root]=Node(root)

    def insertNode(self,parent,data):

        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        if(parent in self.nodes):

            optional = False
            if(data.startswith('[')):
                optional = True
                data = data.replace('[','').replace(']','')

            temp = self.nodes[parent]
            child = Node(data,option=optional)

            temp._addChild(child)
            self.nodes[data]=child
        else:
            raise ValueError('BNF is not well defined, child '+data+' appears before '+parent+' definition')

    def searchNode(self,node):

        """
        Function that returns the reference to the node
        """

        if(node in self.nodes):
            return self.nodes[node]
        else:
            return None
    
    def printNodes(self):

        for key,values in self.nodes.items():
            print key +" "+str(values.optional)
            print values.childs

def create_Tree(filename):

    tree = BNFTree()

    with open(filename,'r') as inp:
        for line in inp:
            parent,childs = line.strip().split('->')
            childs = childs.split()
            parent = parent.strip()
            for child in childs:
                tree.insertNode(parent,child)

    print(tree.printNodes())