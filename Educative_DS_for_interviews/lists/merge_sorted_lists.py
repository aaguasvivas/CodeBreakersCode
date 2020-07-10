def merge_lists_addy(lst1, lst2):
    combined = lst1 + lst2
    return sorted(combined)


def merge_lists(lst1, lst2):
    ind1 = 0  # Creating 2 new variables to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if lst1[ind1] > lst2[ind2]:
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indeces
            ind2 += 1
        else:
            ind1 += 1
    if ind2 < len(lst2):
        lst1.extend(lst2[ind2:])  # Append whatever is left of list2 to list1
    return lst1


# Time Complexity: O(mn)
