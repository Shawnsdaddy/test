from typing import List


def max_dist_to_closest(seats: List[int]) -> int:
    maxthLength = 0
    startindex = -1
    max_startIndex = -1
    for index, char in enumerate(seats):
        if char == 0 :
            if startindex==-1:
                startindex = index
        else:
            if startindex!= -1 :
                length = index -startindex
                if length>maxthLength:
                    max_startIndex = startindex
                    maxthLength = length
                startindex = -1
    if startindex!=-1:
        length = index-startindex+1
        if length > maxthLength:
            return length
    return (1+maxthLength)//2












