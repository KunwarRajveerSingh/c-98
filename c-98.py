def countWordsForFile():
    FileName = input('enter the file name:-')
    file = open(FileName, 'r')
    numberOfWords = 0
    numberOfLines = 0
    for line in file:
        words = line.split()
        numberOfWords  = numberOfWords + len(words)
        numberOfLines = numberOfLines + 1
    print(numberOfWords, 'numberOfWords')
    print(numberOfLines, 'numberOfLines')

def greet(name):
    print('hello ' + name + ',  how are you')


count = 3
while count>1:
    
    if count %2 == 0:
        countWordsForFile()
    else:
        name = input('enter your name :-')
        greet(name)
    count = count -1
     


