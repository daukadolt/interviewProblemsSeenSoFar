from typing import List

def oneEditApart(str1: str, str2: str) -> bool:
        if len(str1) == len(str2):
                diffCount = 0
                for i in range(len(str1)):
                        if diffCount >= 2:
                                return False
                        if str1[i] != str2[i]:
                                diffCount += 1
                if diffCount >= 2:
                        return False
                return True
        else:
                longer, shorter = (str1, str2) if len(str1) > len(str2) else (str2, str1)
                iLong, iShort = 0, 0
                diffCount = 0
                while iShort < len(shorter):
                        if diffCount >= 2:
                                return False
                        if longer[iLong] != shorter[iShort]:
                                iLong += 1
                                diffCount += 1
                        else:
                                iLong += 1
                                iShort += 1
                if diffCount >= 2:
                        return False
                if iShort == len(shorter) and iLong == len(longer): # first condition is extra, but for the sake of remembering what this condition checks I'll leave it here for now.
                        return True
                if diffCount <= 1 and iLong == len(longer)-1:
                        return True
                return False

def coinExchange(coins: List[int], amount: int) -> List[int]:
        partialSums = {}
        prevSum = 0
        for i in range(len(coins)):
                prevSum += coins[i]
                partialSums[prevSum] = i
        theKeys = list(partialSums.keys())
        for i in range(len(theKeys)):
                searchFor = amount - coins[i] + theKeys[i]
                if searchFor in partialSums:
                        return [i, partialSums[searchFor]]
        return None

                