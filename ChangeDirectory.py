newPath = input("Enter new path: ")
def cd(newPath):
    currentPath= "/a/b/c/d"
    if newPath[0] == '/':
        currentPath = newPath

    elif newPath[0:2] == '..':
        if newPath[2] == '/':
            currentPath = currentPath[0: currentPath.rindex("/")]
            newPath = newPath[2:]
            currentPath += newPath

        elif newPath[2] == '/0':
            currentPath = currentPath[0: currentPath.rindex("/")]

    elif newPath[0] == '.' and newPath[1] == '/':
        currentPath += newPath[1:]

    else:
        currentPath = currentPath + "/" + newPath
    print(currentPath)
cd(newPath)
