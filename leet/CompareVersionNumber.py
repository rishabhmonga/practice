def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    ver1_split = version1.split('.')
    ver2_split = version2.split('.')
    ver1 = version1.split('.')[0]
    ver2 = version2.split('.')[0]
    rev1 = '0'
    rev2 = '0'
    if len(ver1_split) > 1:
        rev1 = version1.split('.')[1]
    if len(ver2_split) > 1:
        rev2 = version2.split('.')[1]
    if int(ver1) > int(ver2):
        return 1
    elif int(ver1) == int(ver2):
        if int(rev1) > int(rev2):
            return 1
        elif int(rev1) == int(rev2):
            return 0
        else:
            return -1
    else:
        return -1

if __name__ == '__main__':
    print(compareVersion('1.0.1', '1'))
