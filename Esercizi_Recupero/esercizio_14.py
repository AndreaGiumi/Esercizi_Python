def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    n = len(intervals)

    for i in intervals:
        if not (i[0] <= i[1]):
            raise ValueError("Errore! Il primo numero dell'intervallo deve essere minore del secondo!")
        else:
            return intervals

    if n < 1:
        return []
    if n == 1:
        return intervals
    


c = []
d = [[22, 8], [4, 21]]

print(merge_intervals(d))