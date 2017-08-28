def main():
    string = input()
    print(string)

    num = int(input())
    print(num)

    string = input().split()
    for i in string:
        print(i)
    
    num = map(int, input().split())
    print(' '.join(map(str, num)))

main()