# algorithm-study
Record my algorithm learning process and implement them use different programming languages.

To see the implementation of specific programming language, please checkout to the corresponding branch. E.g. to see the python implementation, use the following command:
```
git checkout python
```

## Requirements
[matplotlib][matplotlib]
> Some algorithm need the module matplotlib to plot the result. E.g. [context_hull/graham_scan.py][graham scan]

[nose][nose]
> Used for unit test. E.g. `nosetests -v test/`

[subprocess32][subprocess32]

[graphviz][graphviz]
> For Ubuntu use the following command to install:
>
> `sudo apt-get install graphviz libgraphviz-dev`
>
> Note: **libgraphviz-dev** is necessary for install `pygraphviz`

[pygraphviz][pygraphviz]
> Because the issue that `pygraphviz` can not infer `include/` and `lib/` directories correctly
> on Ubuntu, please use the following command when install `pygraphviz`:
> 
> pip install pygraphviz --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/"

[python-tk][python-tk]
> `sudo apt-get install python-tk`

## Screenshots
#### Convex Hull
![Convex Hull Picture 1][convex hull picture 1]

#### AVL Tree
![AVL Tree Picture 1][avl tree picture 1]

## References
[George T. Heineman, Gary Pollice and Stanley Selkow's Algorithms in a Nutshell, 2nd Edition][algorithm in a nutshell]


[graham scan]: /convex_hull/graham_scan.py

[avl tree picture 1]: /res/screenshots/avl_tree_graph.png
[convex hull picture 1]: /res/screenshots/convex_hull_1.png

[algorithm in a nutshell]: http://shop.oreilly.com/product/0636920032885.do
[matplotlib]: http://matplotlib.org/
[nose]: http://nose.readthedocs.io/en/latest/
[subprocess32]: https://github.com/google/python-subprocess32/
[graphviz]: http://www.graphviz.org/
[pygraphviz]: https://pygraphviz.github.io/
[python-tk]: https://docs.python.org/2/library/tkinter.html
