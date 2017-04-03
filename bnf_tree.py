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
from random import randint

class Node:
    """
    Class Node
    """
    def __init__(self,value):
        self.data=value
        self.childs = []
        self.parent = None

    def _addChild(self,child):
        child.parent=self
        self.childs.append(child)

    def _replaceChild(self,child,child2):
        ind = self.childs.index(child)
        self.childs[ind]=child2
        child2.parent=self

    def _getChildsValue(self):
        childsV = []
        for child in self.childs:
            childsV.append(child.data)
        return childsV

class BNFTree:
    """
    Class Tree
    """
    def __init__(self,root='<start>'):
        self.nodes={}
        self.nodes[root]=Node(root)
        self.root = root

    def _insertNode(self,parent,data):

        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        if(parent in self.nodes):

            temp = self.nodes[parent]
            child = Node(data)

            temp._addChild(child)
            self.nodes[data]=child
        else:
            raise ValueError('BNF is not well defined, child '+data+' appears before '+parent+' definition') 

    def _searchNode(self,node):

        """
        Function that returns the reference to the node
        """

        if(node in self.nodes):
            return self.nodes[node]
        else:
            return None
    
    def _printNodes(self):

        for key,values in self.nodes.items():
            print key+" "+str(values)
            print values.childs

    def _updateNodes(self):

        root = self.nodes[self.root]
        self.nodes.clear()
        self._updateNode(root)

    def _updateNode(self,node):

        self.nodes[node.data]=node
        for child in node.childs:
            self._updateNode(child)

    def _walk_tree(self,node,result):

        if(len(node.childs)==0 or node.childs==None):
            result.append(node.data)
        else:
            for child in node.childs:
                self._walk_tree(child,result)

    def _getExpression(self):
        
        result = []
        root_node = self.nodes[self.root]
        self._walk_tree(root_node,result)
        return ' '.join(result)

def roulette(childs):

    size = 100/len(childs)
    index = 0
    roulette = []

    for child in childs:
        temp = [index]*size
        index+=1
        roulette+=temp

    return roulette[randint(0,len(roulette)-1)]

def create_Tree(rules,start):

    tree = BNFTree(root=start)

    to_add = deque()
    to_add.append(start)

    while to_add:
        parent = to_add.popleft()

        if(parent in rules):
            childs = rules[parent]
        else:
            continue

        if(len(childs)>1):
            index = roulette(childs)
            childs = childs[index]
        else:
            childs=childs[0]

        for child in childs:

            if(child.startswith('[')):
                index = randint(0,100)
                if(index<50):
                    continue
                child = child.replace('[','').replace(']','')

            tree._insertNode(parent,child)
            to_add.append(child)
    
    return tree

def mutateTree(rules,node,tree):

    tree.nodes[node.data].childs = []

    to_add = deque()
    to_add.append(node.data)

    while to_add:

        parent = to_add.popleft()
        if(parent in rules):
            childs = rules[parent]
        else:
            continue

        if(len(childs)>1):
            index = roulette(childs)
            childs = childs[index]
        else:
            childs=childs[0]

        for child in childs:

            if(child.startswith('[')):
                index = randint(0,100)
                if(index<50):
                    continue
                child = child.replace('[','').replace(']','')

            tree._insertNode(parent,child)
            to_add.append(child)

    tree._updateNodes()
    return tree
