# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
ana = ["eat","tea","tan","ate","nat","bat"]

visit = [False]*len(ana)
result = []
for i in range(len(ana)):
    if visit[i]:
        continue
    group = []
    group.append(ana[i])
    visit[i]= True
    # print(group)
    
    for j in range(i+1, len(ana)):
        # print(ana[j])
        if not visit[j]:
            if sorted(ana[i]) == sorted(ana[j]):
                group.append(ana[j])
                visit[j] = True
    result.append(group)
print(result)
    
