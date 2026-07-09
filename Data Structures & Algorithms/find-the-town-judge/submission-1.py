class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        first = [i[0] for i in trust]
        second = [i[1] for i in trust]
        count = Counter(second)

        for person, freq in count.items():
            if freq == n - 1 and person not in first:
                return person
        
        return -1