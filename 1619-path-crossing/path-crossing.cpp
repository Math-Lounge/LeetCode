#include <utility>
#include <map>
#include <unordered_map>

typedef std::pair <int, int> Coord;

bool operator < (const Coord & lhs, const Coord & rhs)
{
    return false
        || (   std::get <0> (lhs) <  std::get <0> (rhs))
        || (true
            && std::get <0> (lhs) == std::get <0> (rhs)
            && std::get <1> (lhs) <  std::get <1> (rhs)
            )
    ;
}

class Solution {
public:
    bool isPathCrossing (string path)
    {
        Coord curr (0,0);
        _path.insert (curr);
        auto & [x,y] = curr;
        for (auto p : path)
        {
            const auto & [dx,dy] = _map [p];
            x += dx; y += dy;
            auto && [_, inserted] = _path.insert (curr);
            if (!inserted) return true;
        }
        return false;
    }

private:
    std::set <Coord> _path;
    static std::map <char, Coord> _map;
};

/*static*/ std::map <char, Coord> Solution::_map =
{
    { 'N', Coord ( 0, 1) },
    { 'S', Coord ( 0,-1) },
    { 'W', Coord (-1, 0) },
    { 'E', Coord ( 1, 0) },
};
