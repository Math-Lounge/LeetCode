#include <map>

class Solution {
public:
    int longestPalindrome(string s) {
        std::map<char, unsigned int> counter;
        for (char ch : s) {
            counter[ch]++;
        }
        unsigned int len = 0;
        bool odd_len = false;
        for (auto [ch, count] : counter) {
            len += 2 * (count / 2);
            if ((count % 2 == 1) && !odd_len) {
                odd_len = true;
                len += 1;
            }
        }
        return len;
    }
};
