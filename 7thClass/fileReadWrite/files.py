# files and exceptions 1
print('\nFILE READER')
with open('demo.txt') as fileObj:
    content = fileObj.read()
    print(content)
    content.rstrip()

# files and exceptions 1
print('\nLOOP FILE CONTENT')
with open('demo.txt') as loopFile:
    for line in loopFile:
        print(line)


print('\nFILE PATHS')
with open('textFiles\RDir_textFile.txt') as relativeDirFile:
    print(relativeDirFile.read())
