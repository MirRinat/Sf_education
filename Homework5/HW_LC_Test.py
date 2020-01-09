import HW_LC_ToFill as toFill
score = 0

if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    valueOne = "GS"
    valueTwo = "JPM"
    if toFill.exampleOne(valueOne,valueTwo) == True:
        score+=1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    valueOne = "GS"
    valueTwo = "GS"
    valueThree = "GS"
    if toFill.exampleTwo(valueOne,valueTwo,valueThree) :
        score+= 1
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    valueOne = "GS"
    valueTwo = "JPM"
    valueThree = "GS"
    valueFour = "JPM"
    if toFill.exampleThree(valueOne,valueTwo,valueThree) and \
            toFill.exampleThree(valueOne,valueTwo,valueFour):
        score += 1
else:
    print("ATTN:!!!Please create method exampleThree!!!")

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    testString = "PythonRules"
    wordOne = 'Rules'
    wordTwo = "Java"
    if toFill.exampleFour(testString,wordOne)== 's' and \
                    toFill.exampleFour(testString,wordTwo) == 'P':
        score+=2
else:
    print("ATTN:!!!Please create method exampleFour!!!")

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):

    testArray = [ "Python","Rules","Data","Science" ]

    if toFill.exampleFive(testArray,"Rules","Data") == "One" and \
            toFill.exampleFive(testArray, "Java", "Data") == "Two" and \
                toFill.exampleFive(testArray,"C++","Games") == "None":
        score+=2
else:
    print("ATTN:!!!Please create method exampleFive!!!")

if (hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
        testArray = ["Python", "Rules", "Data", "Science"]

        first = toFill.exampleSix(testArray, "Java",   4) == "Success"
        second = toFill.exampleSix(testArray,"Java",   3) == "Not In Success"
        third = toFill.exampleSix(testArray, "Python", 4) == "Length Success"
        fourth = toFill.exampleSix(testArray,"Python",   3) == "Failure"
        if first and second and third and fourth:
             score += 3
else:
        print("ATTN:!!!Please create method exampleSeven!!!")

print("YOUR SCORE IS : {}".format(score))