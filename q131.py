class Solution:
  def partition(self, s: str) -> List[List[str]]:
    res = []
    self.backtrack(s, 0, res, [])
    return res
  
  def backtrack(self, s, start, res, comb):
    if start == len(s):
      res.append(list(comb))
      return

    for i in range(start, len(s)):
      substr = s[start:i + 1]
      if self.validPalindrome(substr):
        comb.append(substr)
        self.backtrack(s, i + 1, res, comb)
        comb.pop()

  def validPalindrome(self, substr):
    return substr == substr[::-1] 
