class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        for i in count:
            count[i] = [count[i], 0]   

        time = 0

        while True:
            status = True
            curr = None

            for i in count:
                if count[i][0] > 0:
                    status = False

                    if count[i][1] == 0:
                        if curr is None or count[i][0] > count[curr][0]:
                            curr = i

            if status:
                break

            if curr is not None:
                count[curr][0] -= 1
                count[curr][1] = n + 1

            for i in count:
                if count[i][1] > 0:
                    count[i][1] -= 1

            time += 1

        return time