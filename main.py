# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def read_and_load(name):
    arr_list = []
    with open(name, 'r') as int_arr:
        for line in int_arr:
            arr_list.append(int(line))
        int_arr.close()

    return arr_list

def count_inversions(arr_list):
    size = len(arr_list)

    if size > 1:
        if size % 2 == 0:
            mid_point = int(size/2)
        else:
            mid_point = int((size+1)/2)

        list1 = arr_list[:mid_point]
        list2 = arr_list[mid_point:]

        return count_inversions(list1) + count_inversions(list2) + merge(list1, list2, arr_list)
    else:
        return 0

def merge(list1, list2, total_list):
    copy_list1, copy_list2 = list(list1), list(list2)
    total_size = len(total_list)
    l1_index, l2_index = 0, 0
    l1_size, l2_size = len(list1), len(list2)
    l1_done, l2_done = False, False
    inversions = 0
    for i in range(total_size):
        if not l2_done and not l1_done:
            if copy_list1[l1_index] > copy_list2[l2_index]:
                total_list[i] = copy_list2[l2_index]
                inversions += (l1_size - l1_index)

                if l2_index + 1 < l2_size:
                    l2_index += 1
                else:
                    l2_done = True
            else:
                total_list[i] = copy_list1[l1_index]
                if l1_index + 1 < l1_size:
                    l1_index += 1
                else:
                    l1_done = True

        elif l1_done and not l2_done:
            total_list[i] = copy_list2[l2_index]
            if l2_index + 1 < l2_size:
                l2_index += 1
            else:
                l2_done = True
        elif l2_done and not l1_done:
            total_list[i] = copy_list1[l1_index]
            if l1_index + 1 < l1_size:
                l1_index += 1
            else:
                l1_done = True

    return inversions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr_list = read_and_load('IntegerArray.txt')
    print(count_inversions(arr_list))
    print(arr_list)

