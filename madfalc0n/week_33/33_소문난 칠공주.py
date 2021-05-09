"""
소문난 칠공주
https://www.acmicpc.net/problem/1941
"""

def backtrack(cur, visit, cost):
    global princess_dict, visit_list
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if cost == 7:
        if princess_dict['S'] >= 4:
            if sorted(visit) not in visit_list:
                visit_list.append(sorted(visit))
                # print(princess_dict)
                # print(visit_list)
    else:
        x,y = cur
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if [nx,ny] not in visit:
                    people = mat[nx][ny]
                    princess_dict[people] += 1
                    if princess_dict['Y'] > 3:
                        princess_dict[people] -= 1
                        continue
                    visit.append([nx,ny])
                    tmp_cost = cost + 1
                    for i in range(tmp_cost):
                        backtrack(visit[i], visit, cost + 1)
                    visit.pop(-1)
                    princess_dict[people] -= 1


mat = []
check_point = []
for i in range(5):
    mat.append(list(input()))
    for j in range(5):
        if mat[i][j] == 'S':
            check_point.append([i,j])

# print(check_point)


# print(mat)
cost  =  0
visit = []
visit_list = []
princess_dict = dict.fromkeys(['Y','S'],0)
# print(princess_dict)
for cur in check_point:
    x,y = cur
    # print(cur)
    visit.append(cur)
    people = mat[x][y]
    princess_dict[people] += 1
    backtrack(cur, visit, cost + 1)
    princess_dict[people] -= 1
    visit.pop(-1)

print(len(visit_list))        
