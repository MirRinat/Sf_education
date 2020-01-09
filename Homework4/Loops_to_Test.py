import Loops_To_Fill  as toFill

score = 0

expectedOne = [64,81,16]
expectedTwo = [25, 9]
if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    if( expectedOne == toFill.exampleOne([8,9,4]) and
        expectedTwo == toFill.exampleOne([5,3]) ):
            score += 1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    expectedOne = [200,101]
    expectedTwo = [1100,- 50]
    if( expectedOne == toFill.exampleTwo([1,2,3,4,100,1]) and
         expectedTwo == toFill.exampleTwo([1000,-150])
        ):
         score += 2
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

expectedOne =  [-1,1,-2,2]
expectedTwo = [0,0,0,0,0,0,0]
if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if( expectedOne == toFill.exampleThree([1,-1,-1,1,2,-2,-2,2]) and
        expectedTwo == toFill.exampleThree([1,0,1,0,1,0,1,0,1,0,1,0,1,0])):
        score +=2
else:
    print("ATTN:!!!Please create method exampleThree!!!")

expectedOne =  ["3","9","6"]
expectedTwo = ["4","2","6","6"]

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    if( expectedOne == toFill.exampleFour([3,5,9,6,7,15,24],3) and
                expectedTwo == toFill.exampleFour([4,1,2,6,5,6,12],2)):
        score +=5
else:
    print("ATTN:!!!Please create method exampleFour!!!")

print(score)
