class Solution {
public:
    bool recurse
    (
        const vector <vector <char>> & board,
        int row, int col,
        const string & word, int idx,
        /*ref*/ std::set <int> & visited
    )
    {
        if (idx == word.size ()) return true;
        auto in_bounds = [] (int val, int bound) -> bool { return (0 <= val) && (val < bound); };
        if (!in_bounds (row, n_rows) || !in_bounds (col, n_cols)) return false;
        if (board [row] [col] != word [idx]) return false;

        int m_idx = row * this->n_cols + col;
        if (visited.count (m_idx) > 0) return false;
        if (!visited.insert (m_idx).second) return false;

        const std::vector <std::tuple <int, int>> neighbors
        {
            {row  , col+1}, {row+1, col  },
            {row  , col-1}, {row-1, col  },
        };
        for (auto [r,c] : neighbors)
        {
            bool found = recurse (board, r, c, word, idx+1, visited);
            if (found) return true;
        }

        visited.erase (m_idx);
        return false;
    }

    bool exist (vector <vector <char>> & board, string word)
    {
        n_rows = board.size ();
        n_cols = board [0].size ();
        if (!verifyCounts (board, word)) return false;
        for (int row = 0; const auto & line : board)
        {
            for (int col = 0; const auto & letter : line)
            {
                std::set <int> visited; // single int index
                bool found = recurse (board, row, col, word, 0, visited);
                if (found) return true;
                ++col;
            }
            ++ row;
        }
        return false;
    }

    bool verifyCounts (const vector <vector <char>> & board, string word)
    {
        std::map <char, int> count;
        for (const auto & line : board)
            for (auto letter : line)
                count [letter]++;
        for (auto letter : word)
            count [letter]--;
        for (const auto [l,c] : count)
            if (c < 0)
                return false;
        return true;
    }

private:
    int n_rows, n_cols;
};
