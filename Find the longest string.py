Given an array of strings arr[]. You have to find the longest string which is lexicographically smallest
and also all of its prefix strings are already present in the array.


Input: ab a abc abd
Output: abc
Explanation: We can see that length of the longest 
string is 3. And there are two string "abc" and "abd"
of length 3. But for string "abc" , all of its prefix
"a" "ab" "abc" are present in the array. So the
output is "abc"



class Solution():
    def longestString(self, arr, n):
        #your code goes here
        check = set(arr)
        ans = ""
        for i in arr:
            flag = 1
            for j in range(len(i)):
                st = i[:j+1]
                if st not in check:
                    flag = 0
                    break
            if flag:
                if len(ans) < len(i):
                    ans = i[:]
                elif len(ans) == len(i):
                    if ans > i:
                        ans = i[:]
        return ans
