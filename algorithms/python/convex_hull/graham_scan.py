#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Compute convex hull using Graham's scan approach.
'''


def graham_scan(points):
    '''
    Graham's scan approach to compute the convex hull points.

    Return a array of points. Each point is a tuple.
    '''

    if not points:
        raise Exception('No points to operate.')

    l = len(points)

    if l < 3:
        return points

    # find the lowest point
    l_p = min(points, key=lambda e: e[1])
    l_i = points.index(l_p)

    # swap the lowest point to the last position
    if l_i != (l-1):
        points[l_i], points[l - 1] = points[l -1], points[l_i]

    from math import atan2

    def polar_cmp(x, y):
        angle1 = atan2(x[1] - l_p[1], x[0] - l_p[0])
        angle2 = atan2(y[1] - l_p[1], y[0] - l_p[0])

        if angle1 > angle2:
            return -1
        elif angle1 < angle2:
            return 1

        if x[1] > y[1]:
            return -1
        elif x[1] < y[1]:
            return 1

        return 0

    # sort points[0, l-1] by descending polar angle with respect to
    # points[lowest_i]
    s_points = sorted(points[:-1], cmp=polar_cmp)

    first_angle = atan2(s_points[0][1] - l_p[1], s_points[0][0] - l_p[0])
    last_angle = atan2(s_points[-1][1] - l_p[1], s_points[-1][0] - l_p[0])

    # if all points are colinear
    if first_angle == last_angle:
        return [l_p, s_points[0]]

    hull = []
    hull.append(s_points[-1]) # lowest polar angle point
    hull.append(l_p) # lowest point

    def is_left_turn(p1, p2, p3):
        return (((p2[0] - p1[0]) * (p3[1] - p1[1]))
            - ((p2[1] - p1[1]) * (p3[0] - p1[0])) > 0)

    for p in s_points:
        while(is_left_turn(hull[-2], hull[-1], p)):
            hull.pop()
        hull.append(p)

    return hull[:-1]


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Compute convex hull using Graham\'s scan approach.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--random', type=int, help='max random point count')
    group.add_argument('--file', type=str, help='file from which points read ')
    parser.add_argument('--plot', action='store_true', help='plot convex hull using matplotlib')

    args = parser.parse_args()

    if args.random:
        # to avoid 'ValueError("sample larger than population")' when call
        # random.sample().
        r_end = 100
        if args.random >= r_end:
            r_end = args.random + 10

        x_axes = random.sample(xrange(1, r_end), args.random)
        y_axes = random.sample(xrange(1, r_end), args.random)
        points = zip(x_axes, y_axes)
    else:
        from helper import read_points
        points = read_points(args.file)

    convex_hull = graham_scan(points)

    print 'origin points:\t', points
    print 'convex hull:\t', convex_hull

    if args.plot:
        import matplotlib.pyplot as plt

        for p in points:
            color = 'r' if p in convex_hull else 'b'
            plt.plot(p[0], p[1], color + 'o')

        h_x_axes = [ e[0] for e in convex_hull ]
        h_y_axes = [ e[1] for e in convex_hull ]

        h_x_axes.append(h_x_axes[0])
        h_y_axes.append(h_y_axes[0])

        plt.plot(h_x_axes, h_y_axes)
        plt.axis([-10, r_end + 10, -10, r_end + 10])
        plt.show()
