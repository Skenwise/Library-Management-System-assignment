# this module contains  all the searching algorithm for our LMS 

# Merge Sort for sorting library items
def merge_sort(list_of_items, category):
    if len(list_of_items) <= 1:
        return list_of_items

    mid = len(list_of_items) // 2
    left_half = merge_sort(list_of_items[:mid], category)
    right_half = merge_sort(list_of_items[mid:], category)
    return sort(left_half, right_half, category)

def sort(left_half, right_half, category):
    sorted_list_of_items = []
    left_half_index = right_half_index = 0

    while left_half_index < len(left_half) and right_half_index < len(right_half):
        if left_half[left_half_index][category] <= right_half[right_half_index][category]:
            sorted_list_of_items.append(left_half[left_half_index])
            left_half_index += 1
        else:
            sorted_list_of_items.append(right_half[right_half_index])
            right_half_index += 1

    sorted_list_of_items.extend(left_half[left_half_index:])
    sorted_list_of_items.extend(right_half[right_half_index:])
    return sorted_list_of_items

# Binary Search for searching library items
def binary_search(items, key, value):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid][key] == value:
            return items[mid]
        elif items[mid][key] < value:
            low = mid + 1
        else:
            high = mid - 1
# implementation of the merge sort algorithm

library_items = [
    {"title": "Python Programming", "author": "John Doe", "year": 2021},
    {"title": "Data Structures", "author": "Jane Smith", "year": 2019},
    {"title": "Algorithms Unlocked", "author": "Thomas H.", "year": 2015},
    {"title": "Artificial Intelligence", "author": "Anna Johnson", "year": 2020},
]
new_library = merge_sort(library_items, "author")
for book in new_library:
    print(book)

