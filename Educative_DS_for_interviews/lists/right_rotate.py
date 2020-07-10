def rightRotate(lst, n):
    # Get rotation index
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
