
class Solution:

    _SingleMap_ = \
    {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    _DoubleMap_ = \
    {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    def romanToInt (self, s: str) -> int:

        N = i = 0
        end = len (s)
        while (i < end):
            if s [i:i+2] in self._DoubleMap_:
                N += self._DoubleMap_ [s [i:i+2]]
                i += 2
            else:
                N += self._SingleMap_ [s [i]]
                i += 1
            if i == end: break
        return N
