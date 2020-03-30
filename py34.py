# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        length = len(s)
        if length == 0:
            return -1
        item = {}
        for i in range(length):
            item[s[i]] = item.get(s[i], 0) + 1
        for j in range(length):
            if item[s[j]] == 1:
                return j
        return -1
