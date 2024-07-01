from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    max_speed = max(piles)
    min_speed = 1
    while min_speed + 1 < max_speed:
        mid_speed = min_speed + (max_speed-min_speed)//2
        current_h = get_total_hours(piles,mid_speed)
        if current_h <= h:
            # is valid:
            max_speed = mid_speed 
        else:
            min_speed = mid_speed
    if h >= get_total_hours(piles,min_speed):
         return min_speed
    else:
         return max_speed
    
def get_total_hours (piles, spped):
    current_h = 0
    for pile in piles:
            current_h += (pile+ spped -1)//spped
    return current_h

print(minEatingSpeed([3,6,7,11],8))