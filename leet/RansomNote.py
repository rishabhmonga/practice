from collections import Counter

class RansomNote:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None:
            return False
        if ransomNote is '' and magazine is not None:
            return True
        magazineCounter = Counter()
        for str1 in magazine:
            # if str1 not in magazineCounter:
            #     magazineCounter[str1] = 1
            # else:
            #     magazineCounter[str1] +=  1
            magazineCounter[str1] += 1

        for str1 in ransomNote:
            if str1 not in magazineCounter or magazineCounter[str1] == 0:
                return False
            else:
                magazineCounter[str1] -= 1
        return True

note = RansomNote()
print(note.canConstruct("a", "ab"))
print('\n')
print(note.canConstruct("aa", "ab"))
print("\n")
print(note.canConstruct("aa", "aab"))
