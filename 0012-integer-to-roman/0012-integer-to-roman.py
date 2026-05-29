class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        sym = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        op = ""
        for i in range(len(sym)-1,-1,-1):
            res = num // val[i]
            if res != 0:
                op = op + sym[i]*res
            num -= val[i] * res
        return op