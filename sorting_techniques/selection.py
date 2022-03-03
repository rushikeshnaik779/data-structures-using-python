# selection sort 
# we use index for the number and compare the number 
# with other numbers and then swap using index for that number 


def select_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i 
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
                 
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp 

    return my_list 

print(select_sort([4,2,1,5,20,2,1]))
    

