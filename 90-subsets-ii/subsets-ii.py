class Solution:

    def subsetsWithDup (self, nums: List[int]) -> List[List[int]]:
        solutions = {}
        nums.sort ()
        self._subsetsWithDup_ (nums, 0, [], solutions)
        return solutions.values ()

    def _subsetsWithDup_ (self, nums, i, curr, solutions):
        if i == len (nums):
            hash = '_'.join (map (str, curr))
            if hash not in solutions:
                solutions [hash] = list (curr)
            return
        curr.append (nums [i])
        self._subsetsWithDup_ (nums, i+1, curr, solutions)
        curr.pop ()
        self._subsetsWithDup_ (nums, i+1, curr, solutions)
