def act_sel(actions):
    actions = sorted(actions)
    count = len(actions)
    result = []
    result.append(actions[0])

    for i in range(1, count):
        if result[-1][1] <= actions[i][0]:
            result.append(actions[i])
    return result


actions = [(1,2), (1,4), (2,3), (5,8), (4,5)]
res = act_sel(actions)
print(res)
