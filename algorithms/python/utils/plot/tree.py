#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygraphviz as pgv

from searching.binary_search_tree import BinarySearchTree
from searching.avl_tree import AVLTree


g_attr = {
    'size': '8',
    'ratio': 0.618,
}

n_attr = {
    'color': 'red',
    'fillcolor': 'red',
    'shape': 'circle',
    'style': 'filled',
    'height': 0.3,
    'fontsize': 10,
    'fixedsize': True,
}

e_attr = {
    'color': 'black',
    'arrowsize': 0.6,
}


def _node_edges(root, edges):
    '''Recursively fill edges in to `edges` from root `node`.'''

    if not root:
        return

    if root.left:
        edges.append((root.value, root.left.value))
        _node_edges(root.left, edges)

    if root.right:
        edges.append((root.value, root.right.value))
        _node_edges(root.right, edges)


def get_edges(tree):
    '''Export a list of edges from tree.

    Parameters
    ----------
    tree : input tree data structure
        A BST or AVL tree.

    '''

    if not tree:
        raise ValueError('tree is None or tree is empty')

    if not tree.__class__ in (BinarySearchTree, AVLTree):
        raise ValueError('tree must be an instance of BinarySearchTree or AVLTree')

    edges = []
    _node_edges(tree.root, edges)

    return edges


def plot(tree, graph_attr=g_attr, node_attr=n_attr, edge_attr=e_attr,
        graph_file='tree_graph.png'):
    '''Plot a Binary Search Tree or AVL Tree use pygraphviz. Output a png file
    named `graph_file`.

    Parameters
    ----------
    tree : input tree data structure
        a BST or AVL tree.

    graph_attr : dict, optional (default=`g_attr`)

    node_attr : dict, optional (default=`n_attr`)

    edge_attr : dict, optional (default=`e_attr`)

    graph_file : string, optional (default='tree_graph.png')

    '''

    # export edge list from tree
    edgelist = get_edges(tree)
    # a directed agraph instance
    G = pgv.AGraph(directed=True)
    G.graph_attr.update(graph_attr)
    G.node_attr.update(node_attr)
    G.edge_attr.update(edge_attr)
    G.add_edges_from(edgelist)
    G.layout('dot')
    G.draw(graph_file)
