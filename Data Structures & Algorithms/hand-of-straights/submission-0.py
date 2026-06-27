class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for _ in range(len(hand) // groupSize):
            mini = min(hand)
            for _ in range(groupSize):
                if mini not in count:
                    return False
                
                if count[mini] == 0:
                    return False
                
                count[mini] -= 1
                hand.remove(mini)
                mini +=1
        
        return True