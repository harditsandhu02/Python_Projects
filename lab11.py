# CS 177 – lab10.py
# Hardit Sandhu
# This program will first take two dictionaries dict1 and dict2 and an integer x as parameters. 
# Then the program will find out a set of common restaurants within the distance they specify (x).


def findRestaurant(dict1, dict2, x):
    # initializing the three lists
    list1 = []
    list2 = []
    list3 = []

    # first for loop will go through 'dict1'
    for i in dict1:
        # if the key is less than the distance 'x'
        if i < x:
            # adding the resturants to the first list
            list1.append(dict1[i])
    

    # second for loop will go through 'dict2'
    for i in dict2:
        # if the key is less than the distance 'x'
        if i < x:
            # adding the resturants to the first list
            list1.append(dict2[i])

    # removing the sublists in the list
    for sublist in list1:
        for i in sublist:
            # adding each individual sublist value to the new list, 'list2'
            list2.append(i)

    # if the values in the lists match, then the loop will add them to the new list, 'list3'
    for i in range(len(list2)):
        for x in range(i+1, len(list2)):
            # if the two dictionaries have a common resturant
            if list2[i] == list2[x]:
                # add the common resturant to the final list
                list3.append(list2[i])
    
    # finally, convert the list into a set, 'set1'
    set1 = set(list3)
    return(set1)

# main function to test the 'findRestaurant' function
def main():


    dic1Ex1 = {5: ['Panera'], 10: ['RedSeven', 'BK']}
    dic2Ex1 = {10: ['Heisei', 'Panera'], 20: ['BK']}
    xEx1 = 15
    print(findRestaurant(dic1Ex1, dic2Ex1,xEx1))


    dic1Ex2 = {5: ['Panera'], 10: ['RedSeven', 'BK', 'Heisei']}
    dic2Ex2 = {10: ['Heisei', 'Panera'], 20: ['BK']}
    xEx2 = 15
    print(findRestaurant(dic1Ex2, dic2Ex2,xEx2))


    dic1Ex3 = {5: ['Panera'], 10: ['RedSeven', 'BK']}
    dic2Ex3 = {}
    xEx3 = 15
    print(findRestaurant(dic1Ex3, dic2Ex3,xEx3))


# calling the main function
if __name__ == "__main__":
    main()