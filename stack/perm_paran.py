def generateParenthesis(n):

  final_ans = []

  def _dfs(open , close , s):

    #base case
    if open == close and (open + close) == 2 * n:
      final_ans.append(s)
      return
    
    if open <= n:
      _dfs(open + 1 , close , s + "(")

    if close < open:
      _dfs(open , close + 1 , s + ")")

  _dfs(0 , 0 , "")
  return final_ans


print(generateParenthesis(3))




  