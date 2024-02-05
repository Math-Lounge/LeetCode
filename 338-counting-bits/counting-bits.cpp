class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> bits { 0, };
        bits.reserve(n+1);
        for (int i = 1; i <= n; ++i) {
            bits.push_back(bits[i >> 1] + (i & 1));
        }
        return bits;
    }
};
