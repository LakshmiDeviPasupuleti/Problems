class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box={}
       # sum=0
        for i in range(lowLimit,highLimit+1):
            num=i
            sum=0
            while num >0:
                digit=num%10
                sum=sum+digit
                num=num//10
            if sum not in box:
                box[sum]=0
            box[sum]=box[sum]+1
            #count=count+1
        return max(box.values())
