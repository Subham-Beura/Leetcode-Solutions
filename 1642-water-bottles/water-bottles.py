class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # total=0
        # full=numBottles
        # empty=0
        # while full+empty>=numExchange:
        #     # Drink all full Bottles
        #     total+=full
        #     # Add to empty bottle
        #     empty+=full
        #     # Exchange
        #     full=empty//numExchange
        #     empty=empty%numExchange

        # total+=full
        # return total
        return numBottles+(numBottles-1)//(numExchange-1)