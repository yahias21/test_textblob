def accuracy(tested,analytics):
        count=0
        for i in range(len(tested)):
            if (tested[i] > 0 and analytics[i] > 0) or (tested[i] < 0 and analytics[i] < 0) or (
                    tested[i] == 0 and analytics[i] == 0):
                count += 1
        return [count * 100 / len(tested),len(tested)]
