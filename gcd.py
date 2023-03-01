strToNums = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
numsToStr = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def numToString(result: int):
    '''
    The resultant value is converted back to words in this function and output is returned.
    '''
    result = str(result)
    finalOutput = ""
    i: int = 0
    while i < len(result):
        if result[i] in numsToStr.keys():
            finalOutput += numsToStr.get(result[i])
        i += 1
    return finalOutput


def calculateGcd(val1: int, val2: int) -> int:
    '''
    After words are coverted into digits, flow is transfered to this function.
    This function calculates GCD of the given input.
    '''
    if val2 == 0:
        return val1
    else:
        return(calculateGcd(val2, val1 % val2))


def stringToNumber(gcdNum: str, miss: int = 0, x: int = 0, y: int = 3, result: str = "") -> int:
    '''
    This function converts the given input from words to string.
    It also checks for invalid inputs.
    '''
    if miss <= 2 and y <= len(gcdNum):
        temp = slice(x, y)
        temp2 = gcdNum[temp]
        if temp2 in strToNums.keys():
            result += strToNums.get(temp2)
            return stringToNumber(gcdNum, 0, y, y + 3, result)

        else:
            return stringToNumber(gcdNum, miss + 1, x, y + 1, result)
    else :
        if miss == 0 and gcdNum[x:y]== "":
            return result
        else:
            raise ValueError('Invalid input')


def main():
    '''
    Flow of code begins from this function.
    This function validates the input and calls the preceding function.
    Final result is displayed in this function.
    '''
    gcdNum1: str = input("input 1: ")
    gcdNum2: str = input("input 2: ")
    if len(gcdNum1) < 3 or len(gcdNum2) < 3:
        raise ValueError('Invalid input')
    else:
        val: int = int(stringToNumber(gcdNum1))
        val2: int = int(stringToNumber(gcdNum2))
        result: int = calculateGcd(val, val2)
        print(numToString(result))


if __name__ == '__main__':
    main()
