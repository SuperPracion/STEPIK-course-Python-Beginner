def merge(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))