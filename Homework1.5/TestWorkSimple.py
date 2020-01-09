import Homework1_5 as work


simpleCount = 0

if(work.combineStringNumsSmart() == "В чате Data Science Academy на данный момент 185 студентов"):
    print("\nArray test is correct")
    simpleCount += 1

if(work.simpleArrayString() == "The population of the Roman Empire was 56.8 million at 25BC"):
    print("\nArray test is correct")
    simpleCount += 1

if(work.addingArrayString() == "The population of the Roman Empire was 56.8 million at 25BC" ):
    print("\nArray addition test is correct")
    simpleCount += 1

if(work.measuringLengthofArray() == "Квинтилий Вар потерял 3 легиона в Германии: Legio XIX, Legio XVII, и Legio XVIII"):
    print("\nArray length test is correct")
    simpleCount += 1

if( work.doIterations() == "\n BSC обанкротился\n LEH обанкротился\n WB обанкротился"):
    print("\nIteration test is correct")
    simpleCount += 1


if( len(work.doRangeIteration())== 999 and work.doRangeIteration()[565]==566):
    print("\nIterations test is correct")
    simpleCount += 1

if( work.doDictionary() == "Траян умер в 117 г н.э." ):
    print("\nDictionary test is correct")
    simpleCount += 1

if( work.doFunctionCalling() == "\n Нерва умер в 98 г н.э.\n Траян умер в 117 г н.э.\n Адриан умер в 138 г н.э." ):
    print("\nFunction test is correct")
    simpleCount += 1

print("\nTotal of {} out of 7 tests is completed".format(simpleCount))