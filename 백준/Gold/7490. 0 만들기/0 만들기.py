# 수식의 결과가 0이 되는 모든 수식 출력하는 프로그램
# ' ', '+', '-'
import copy 

def recursive(arr, n):
    if len(arr) == n:
        operators.append(copy.deepcopy(arr))
        return
        
    arr.append(' ')
    recursive(arr, n)
    arr.pop()
    
    arr.append('+')
    recursive(arr, n)
    arr.pop()
    
    arr.append('-')
    recursive(arr, n)
    arr.pop()
        

t = int(input())

for i in range(t):
    operators = []
    n = int(input())
    recursive([], n-1)
    
    for operator in operators:
        statement = ''
        for j in range(n-1):
            statement += str(j+1) + operator[j]
        statement += str(n)
        if (eval(statement.replace(' ', ''))) == 0:
            print(statement)
    print()
    
    