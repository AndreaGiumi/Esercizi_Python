def moltipilicatore(n:int):

    return lambda x:x*n



per_due = moltipilicatore(10)
print(per_due(10))