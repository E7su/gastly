def cover_segments_with_points():

    count = int(input())

    points = []
    for i in range(0, count):
        left, right = list(int(x) for x in input().split())
        points.append((i, 'l', left))
        points.append((i, 'r', right))

    # if points is equal: left points first, right point second
    points = sorted(points, key=lambda x: (x[2], x[1]))

    stack = []
    res = []
    covered = [False] * count
    for point in points:
        if point[1] == 'l':
            stack.append(point[0])
        else:
            segment_num = point[0]
            if not covered[segment_num]:
                res.append(point[2])  # right point
                stack.remove(segment_num)
                covered[segment_num] = True
                for segment in reversed(stack):
                    covered[segment] = True
                    stack.remove(segment)
    print(len(res))
    print(' '.join(map(str, res)))


cover_segments_with_points()
