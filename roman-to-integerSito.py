#Convert a Roman number to an integer number

#1 <= s.length <= 15
#s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
#It is guaranteed that s is a valid roman numeral in the range [1, 3999]

#it's a recursive solution, valore() is a side function

class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) > 1:
            a = Solution.valore(s[0])
            b = Solution.valore(s[1])
            if a < b:
                return b-a + Solution.romanToInt(self, s[2:])
            return Solution.valore(s[0]) + Solution.romanToInt(self, s[1:])
        if len(s) == 1:
            return Solution.valore(s[0])
        return 0


    def valore(c) -> int:
        match c:
            case "I":
                value=1
            case "V":
                value=5
            case "X":
                value=10
            case "L":
                value=50
            case "C":
                value=100
            case "D":
                value=500
            case "M":
                value=1000
            case _:
                value=999999999
        return(value)
