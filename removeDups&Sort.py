# list of numbers
testList = [10, 2, 5, 1, 9, 9, 2, 71, 3, 15, 16, 11, 11]
print("----------testList with duplications---------")
print(testList)

# creating a dictionary removes dupilcates since every number must be unique. We then convert back to a list
testList = list(dict.fromkeys(testList))

# testList without duplicates
print("-----testList w/o duplications-----")
print(testList)

# functions
# selectionSort
def selectionSort(testList):
    for i in range(len(testList)):
        minIndex = i
        for j in range(i+1,len(testList)):
            if testList[minIndex] > testList[j]:
                minIndex = j
        temp = testList[i]
        testList[i] = testList[minIndex]
        testList[minIndex] = temp
    return testList


# sorted list using selectionSort ascending order
print("-----------selectionSort-----------")
print(selectionSort(testList))