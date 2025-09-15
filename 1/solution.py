from typing import Optional


def sum_pair(nums: list, target: int) -> Optional[tuple[int, int]]:
    if len(nums) < 2:
        return None

    seen = dict()
    for i, n in enumerate(nums):
        addition = target - n
        if addition in seen:
            return seen[addition], i
        seen[n] = i
    return None