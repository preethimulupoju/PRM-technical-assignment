def sort_list(n, arr):
    arr.sort(key=lambda x: x[-2])
    return arr

if __name__ == '__main__':
    n = int(input().strip())
    arr = [input().strip() for _ in range(n)]
    result = sort_list(n, arr)
    print(*result, sep='\n')
"sample input 4 great"
#hello
#hiyo
#abc
"output is abc"
"great"
"hello"
"hiyo"
