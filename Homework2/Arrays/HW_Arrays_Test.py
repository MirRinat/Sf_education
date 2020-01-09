import HW_Arrays_ToFill as toFill

score = 0

if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    testArray=[1,2,3,4,5,6,'q']
    if toFill.exampleOne(testArray) == 14:
        score+=1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    testArray = [1, 2, 3, 4, 5, 'six', 'q']
    if toFill.exampleTwo(testArray) == 'six' :
        score+=1
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if toFill.exampleThree("one","TWO",3) == ["one","TWO",3]:
        score+=1
else:
    print("ATTN:!!!Please create method exampleThree!!!")

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    if toFill.exampleFour(testArray) == [1,4,6]:
        score+=2
else:
    print("ATTN:!!!Please create method exampleFour!!!")

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    if toFill.exampleFive(testArray,'e') == [1, 2, 3, 4, 5, 6, 'q','e']:
        score+=1
else:
    print("ATTN:!!!Please create method exampleFive!!!")

if (hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    if toFill.exampleSix(testArray,3,"w") == [1,'w',3,5,6,'q']:
        score+=2
else:
    print("ATTN:!!!Please create method exampleSix!!!")

if (hasattr(toFill, 'exampleSeven') and callable(getattr(toFill, 'exampleSeven'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    if toFill.exampleSeven(testArray, "e") == [ 3, 4, 5, 6, 'q','e']:
        score += 2
else:
    print("ATTN:!!!Please create method exampleSeven!!!")

print("YOUR SCORE IS : {}".format(score) )