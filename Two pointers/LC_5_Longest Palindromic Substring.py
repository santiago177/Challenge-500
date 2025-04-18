def getUpdatedPointers(s, start, left, right, sameChar):
    def reset():
        nonlocal start, left, right, sameChar
        start += 1
        left = start
        right = start
        sameChar = False
    if left > 0 and right < len(s) - 1:
        if s[left - 1] == s[right + 1]:
            if sameChar:
                if s[left] != s[left - 1]:
                    sameChar = False
            left -= 1
            right += 1
        elif sameChar:
            if s[left - 1] == s[left]:
                left -= 1
            elif s[right + 1] == s[right]:
                right += 1
            else:
                reset()
        else:
            reset()
    elif left == 0 and right < len(s) - 1:
        if sameChar:
            if s[right] == s[right + 1]:
                right += 1
            else:
                reset()
        else:
            reset()
    elif left > 0 and right == len(s) - 1:
        if sameChar:
            if s[left] == s[left - 1]:
                left -= 1
            else:
                reset()
        else:
            reset()
    else:
        return {"start" : 0, "left" : 0, "right" : 0, "sameChar" : False, "solved" : True}
    return {"start" : start, "left" : left, "right" : right, "sameChar" :sameChar, "solved" : False}

def longestPalindrome(s: str) -> str:
    longest = ""
    start = 0
    left = 0
    right = 0
    sameChar = False
    while start < len(s):
        if right == left:
            sameChar = True
        pointers = getUpdatedPointers(s, start, left, right, sameChar)
        start = pointers["start"]
        left = pointers["left"]
        right = pointers["right"]
        sameChar = pointers["sameChar"]
        if right - left + 1 > len(longest):
            longest = s[left:right + 1]
        if pointers["solved"]:
            return longest

    return longest


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("babccm"))
print(longestPalindrome("cbabbab"))
print(longestPalindrome("babbabcc"))
print(longestPalindrome("caccccccb"))
