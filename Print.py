if __name__ == '__main__':
    n = int(input())
    i = 1
    numArr = []
    while(i<n+1):
        numArr.append(i)
        i+=1
    print(''.join(map(str, numArr)))
        
