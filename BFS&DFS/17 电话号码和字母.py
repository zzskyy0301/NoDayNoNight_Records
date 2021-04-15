#当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dicts={"2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}
        ans=[]
        def dfs(temp,index):
            if index==len(digits):
                ans.append(temp)
                return
            num=digits[index]
            letters=dicts[num]
            for let in letters:
               #temp.append(let) 
               dfs(temp+let,index+1)
        dfs("",0)
        return ans
