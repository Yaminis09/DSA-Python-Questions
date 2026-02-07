"""
https://www.naukri.com/code360/problems/negative-to-the-end_7088763?kunjiRedirection=true
"""
def negativeToTheEnd(v: [int]) -> [int]:
    positive_number = []
    negative_number = []
    
    for num in v:
        if num > 0:
            positive_number.append(num)
        elif num <0:
            negative_number.append(num)
    
    number = positive_number+negative_number
    
    return number
