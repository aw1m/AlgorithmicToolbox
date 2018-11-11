# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort()
    point = []
    prev = [0,0]

    #print(segments)
    for s in segments:
        seg = [s.start, s.end]
        if prev==[0,0]:
            prev = seg
        elif  seg[0] >prev[0] and seg[1]<prev[1]:
            prev=seg
        elif  seg[0] > prev[0] and seg[0]<prev[1] and seg[1]>prev[1]:
            prev[0]=seg[0]
        elif seg[0]>prev[1]:
            point.append(prev[1])
            prev = seg
        else:
            continue
    point.append(prev[1])
    return point

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
