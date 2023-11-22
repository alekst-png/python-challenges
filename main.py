# test function
def print_hi(name):
    print(f'Hi, {name}')


# merge two arrays and sort
def merge(num1, m, num2, n):
    for i in range(n):
        num1[m + i] = num2[i]
    num1.sort()
    return num1

# remove if more than 2 duplicates, then sort
def twoDuplicates(nums):
    i=0
    # for each value in the list
    for n in nums:
        if i<2 or n>nums[i-2]:
            nums[i]=n
            i+=1

            # 1>-2 [1]
            # 1>-1 [1,1]
            # 1>1 [1,1]
            # 2>1 [1,1,2]
    return nums


# number of values above 3 in list
def three(arr):
    num = 0
    for i in range(len(arr)):
        if arr[i] > 2:
            num += 1

    return num


# reverse words
def reverseWords(stringSentence):
    words = stringSentence.split(" ")
    output = ""

    for i in range(len(words) -1, -1, -1):      # range (start, stop, step - -1 is reverse)
        if words[i].strip() == "":
            continue
        output = output + (words[i]) + " "

    return output


# if anagram
def anagram(s, t):
    # sort alphabetically
    sortedS = sorted(s)
    sortedT = sorted(t)
    if sortedS == sortedT:
        return 'true'
    else:
        return 'false'


class Main(object):
    # merge two arrays and sort
    # array = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    # for i in range(6):
    #     print(array[i])

    # value = twoDuplicates([1,1,1,2])
    # for i in range(len(value)):
    #     print(value[i])
    # print("number of values is " + str(len(value)))
    #
    # # prints each value in list
    # for n in [1,1,1,2]:
    #     print(n)

    # print(three([3,0,6,1,5]))
    # print(reverseWords("the big red house"))
    print(anagram("anagram", "gramana"))
