if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            element = int(command[2])
            position = int(command[1])
            my_list.insert(position, element)
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            element = int(command[1])
            my_list.remove(element)
        elif command[0] == "append":
            element = int(command[1])
            my_list.append(element)
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()
