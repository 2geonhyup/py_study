import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


class Solution:
    def function(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # 숫자와 문자만 남깁니다
                strs.append(char.lower())
        # print(strs)
        strB = []
        strB = list(reversed(strs))  # 거꾸로 뒤집힌 리스트를 반환합니다
        # print(strB)
        return strs == strB


sol = Solution()
print(sol.function("A man, a plan, a canal: Panama"))
# practice
