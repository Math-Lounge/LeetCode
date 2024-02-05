class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ones = 0;
        while (n > 0) {
            n &= (n-1);
            ones++;
        }
        return ones;
    }
};
