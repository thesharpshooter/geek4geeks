#Uses python2
start = map(int,raw_input().split(" "))
end = map(int,raw_input().split(" "))

temp = [[start[i],end[i]] for i in range(len(start))]

def activitySelection(temp):
    res = []
    temp = sorted(temp,key = lambda x : x[1])
    res.append(temp[0])
    prev = temp[0]
    for i in range(1,len(temp)):
        if temp[i][0] >= prev[1]:
            res.append(temp[i])
            prev = temp[i]
    return res

print activitySelection(temp)
