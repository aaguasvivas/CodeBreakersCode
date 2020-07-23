def stringSort(s):
    # O(nlogn) time O(n) space
    sortedStr = sorted(s.replace(" ", ""))
    return "".join(sortedStr)


def stringSortCountArray(s):
    # a - alphabet
    # O(n + a) time and O(n) space
    # as array: O(1) space
    alphabet_size = 26
    count = [0] * alphabet_size

    for c in s.replace(" ", ""):
        count[ord(c) - ord('a')] += 1

    newStr = []
    for i, numLetter in enumerate(count):
        newStr.append(chr(i + ord('a')) * numLetter)

    return "".join(newStr)


def stringSortMultiPass(s):
    # a - size of alphabet
    # O(n*a) time and O(n) space
    # as array: O(1) space
    alphabet_size = 26
    s = list(s.replace(" ", ""))
    swap_index = 0
    for i in range(alphabet_size):
        currentLetter = chr(i + ord('a'))
        for j, c in enumerate(s):
            if c == currentLetter:
                s[swap_index], s[j] = s[j], s[swap_index]
                swap_index += 1
    return "".join(s)


if __name__ == '__main__':
    # alphabet of size 26 - aka constant
    s = 'the quick brown fox jumps over the lazy dog'
    print(stringSort(s))

    s = 'the quick brown fox jumps over the lazy dog'
    print(stringSortCountArray(s))

    s = 'the quick brown fox jumps over the lazy dog'
    print(stringSortMultiPass(s))
