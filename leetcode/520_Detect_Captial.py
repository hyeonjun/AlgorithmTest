class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            if len(word) > 1:
                if word[1].isupper():
                    for w in word[2:]:
                        if w.islower():
                            return False
                else:
                    for w in word[2:]:
                        if w.isupper():
                            return False
        else:
            for w in word[1:]:
                if w.isupper():
                    return False
        return True
