"""
Optimised solution 
https://www.naukri.com/code360/problems/negative-to-the-end_7088763?kunjiRedirection=true&leftPanelTabValue=PROBLEM

"""
def negativeToTheEnd(v):
    insert_pos = 0

    for i in range(len(v)):
        if v[i] > 0:
            temp = v[i]
            j = i
            while j > insert_pos:
                v[j] = v[j - 1]
                j -= 1
            v[insert_pos] = temp
            insert_pos += 1

    return v
