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

## Screenshots
#### Convex Hull
![Convex Hull Picture 1][convex hull picture 1]

## References
[George T. Heineman, Gary Pollice and Stanley Selkow's Algorithms in a Nutshell, 2nd Edition][algorithm in a nutshell]


[graham scan]: /convex_hull/graham_scan.py
[convex hull picture 1]: /res/screenshots/convex_hull_1.png

[algorithm in a nutshell]: http://shop.oreilly.com/product/0636920032885.do
[matplotlib]: http://matplotlib.org/
[nose]: http://nose.readthedocs.io/en/latest/
[subprocess32]: https://github.com/google/python-subprocess32/
