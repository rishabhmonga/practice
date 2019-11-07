from collections import Counter


def subdomainVisits(cpdomains):
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    c = Counter()
    for cd in cpdomains:
        n, d = cd.split()
        c[d] += int(n)
        for i in range(len(d)):
            if d[i] == '.': c[d[i + 1:]] += int(n)
    return ["%d %s" % (c[k], k) for k in c]



if __name__ == '__main__':
    #    Output:    ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    cpdomains = ["9001 discuss.leetcode.com"]
    # print(subdomainVisits(cpdomains))
    print(subdomainVisits(cpdomains))
