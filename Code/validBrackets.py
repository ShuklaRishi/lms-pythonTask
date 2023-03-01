def generateParenthesis(numberOfBrackets: int) -> list[str]:
    def dfs(s: str, left: int, right: int):
        '''
        generateParenthesis() function takes number of brackets as an input and returns output list.
        dfs() performs dfs and generate valid pair of parnthesis and returns the result to parent function.
        '''
        if len(s) == numberOfBrackets*2:
            result.append(s)
            return
        if left < numberOfBrackets:
            dfs(s +'(', left+1, right)
        if right < left:
            dfs(s + ')', left, right+1)
                
    result = []
    dfs('', 0, 0)
    return(result)


def main():
    result = []
    '''
    main() function takes input from user, validates it.
    Further it calls generateParenthesis() function to generate valid pairs of parenthesis.
    '''
    numberOfBrackets: int = int(input())
    if numberOfBrackets == 0:
        print(result)
    elif numberOfBrackets < 0:
        raise ValueError('Invalid input')
    else:
        print(generateParenthesis(numberOfBrackets))


if __name__ == '__main__':
    main()
