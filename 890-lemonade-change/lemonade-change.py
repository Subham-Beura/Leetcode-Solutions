class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total=0
        fives=0
        tens=0
        twenty=0
        possible=True
        for bill in bills:
            if bill==5:
                fives+=1
            elif bill==10:
                if fives<1:
                    possible=False
                fives-=1
                tens+=1
            else:
                if tens>=1 and fives>=1:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    possible=False
                twenty+=1
            # print(possible)
            if not possible:
                return False
        return True

         