def split_and_join(line):
    # write your code here
    n = len(line)
    strW = ''
    for i in range(n):
        if line[i] == " ":
            strW += '-'
        else:
            strW += line[i]
    return strW

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
