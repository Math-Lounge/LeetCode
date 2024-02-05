class Solution {
public:
    string reverseVowels(string s) {
        const std::set<char> vowels { 'a', 'e', 'i', 'o', 'u', };
        char* beg = s.data();
        char* end = beg + s.length() - 1;
        auto incr = [&](char*& c, int chng) {
            while ((beg < end) && (vowels.contains(tolower(*c)) == 0))
                c += chng;
        };
        while (beg < end) {
            incr(beg,  1);
            incr(end, -1);
            if (beg < end)
                swap(*beg, *end);
                beg++;
                end--;
        }
        return s;
    }
};
