class Solution {
public:
    void setZeroes (vector <vector <int>> & matrix)
    {
        bool first_col = inPlaceSetZeroes (/*ref*/ matrix);
        checkSetZeroes (/*ref*/ matrix);
        if (matrix [0] [0] == 0)
            setFirstZeroes (/*ref*/ matrix, false);
        if (first_col)
            setFirstZeroes (/*ref*/ matrix, true);
    }

    void setFirstZeroes (/*ref*/ vector <vector <int>> & matrix, bool col)
    {
        size_t max = col ? matrix.size () : matrix [0].size ();
        for (size_t i = 0; i < max; ++i)
        {
            auto & entry = col ? matrix [i] [0] : matrix [0] [i];
            entry = 0;
        }
    }

    void checkSetZeroes (/*ref*/ vector <vector <int>> & matrix)
    {
        for (size_t r = 1; r < matrix.size (); ++r)
        {
            for (size_t c = 1; c < matrix [0].size (); ++c)
            {
                if ((matrix [r] [0] == 0) || (matrix [0] [c]) == 0)
                {
                    matrix [r] [c] = 0;
                }
            }
        }
    }

    bool inPlaceSetZeroes (/*ref*/ vector <vector <int>> & matrix)
    {
        bool first_col = false;
        for (size_t r = 0; r < matrix.size (); ++r)
        {
            first_col |= (matrix [r] [0] == 0);
            for (size_t c = 1; c < matrix [0].size (); ++c)
            {
                if (matrix [r] [c] == 0)
                {
                    matrix [r] [0] = 0;
                    matrix [0] [c] = 0;
                }
            }
        }
        return first_col;
    }
};
