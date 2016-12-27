def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs is None or len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    lcp = strs[0]
    for s in strs:
        while lcp is not '' and not s.startswith(lcp):
            lcp = lcp[:-1]
    return lcp

if __name__ == '__main__':
    print(longestCommonPrefix(["aab", "ab"]))
    print(longestCommonPrefix([]))
