class Solution:
    def hammingWeight(self, n):
        count = 0
        
        while n:
            count += (n & 1)   # nếu bit cuối là 1 thì cộng
            n >>= 1            # dịch phải
        
        return count