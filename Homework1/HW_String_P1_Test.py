import Homework1.HW_String_P1_ToFill as toFill

score = 0

if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    if toFill.exampleOne() == "I am alive! Alive!":
        score+=1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    if toFill.exampleTwo("second one") == "And this alive too: second one" :
        score+=1
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if toFill.exampleThree("one","TWO",3) == "one...TWO...3":
        score+=1
else:
    print("ATTN:!!!Please create method exampleThree!!!")

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    if toFill.exampleFour("$$$$I MAKE IT RAIN$$$$","$") == "I MAKE IT RAIN":
        score+=1
else:
    print("ATTN:!!!Please create method exampleFour!!!")

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):
    if toFill.exampleFive("?DOES THIS STUFF WITH ? WORK AT ALL????") == "DOES THIS STUFF WITH  WORK AT ALL":
        score+=3
else:
    print("ATTN:!!!Please create method exampleFive!!!")

if (hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
    if toFill.exampleSix("Lett'ss ssee if itt workss") == "Let's see if it works":
        score+=3
else:
    print("ATTN:!!!Please create method exampleSix!!!")

print("YOUR SCORE IS : {}".format(score) )