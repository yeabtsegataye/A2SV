class Solution:
    def interpret(self, command: str) -> str:
        goalDic = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }
        myStr = ''
        i = 0
        while i < len(command):
            if i+3 < len(command) and command[i:i+4] == '(al)':
                myStr+=goalDic[command[i:i+4]]
                i+=4
            elif i+1 < len(command) and command[i:i+2] == '()':
                myStr+=goalDic[command[i:i+2]]
                i+=2
            else:
                myStr+=goalDic[command[i]]
                i+=1 
        return myStr
