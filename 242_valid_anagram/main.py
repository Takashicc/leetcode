# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    # First solution
    def isAnagram(self, s: str, t: str) -> bool:
        s_lookup = {}
        for char in s:
            if s_lookup.get(char) is None:
                s_lookup[char] = 1
            else:
                s_lookup[char] += 1

        t_lookup = {}
        for char in t:
            if t_lookup.get(char) is None:
                t_lookup[char] = 1
            else:
                t_lookup[char] += 1

        for key, value in s_lookup.items():
            if t_lookup.get(key) is None:
                return False

            if t_lookup.get(key) != value:
                return False

        return len(s_lookup) == len(t_lookup)


def main():
    assert Solution().isAnagram("anagram", "nagaram") is True
    assert Solution().isAnagram("rat", "car") is False


if __name__ == '__main__':
    main()
