# this module contains  all the searching algorithm for our LMS 


class Algorithms:
    def __ini__(self):
        self.purpose = 'algorithm'


# Merge Sort for sorting library items
    def merge_sort(self, list_of_items, category):
        if len(list_of_items) <= 1:
            return list_of_items

        mid = len(list_of_items) // 2
        left_half = self.merge_sort(list_of_items[:mid], category)
        right_half = self.merge_sort(list_of_items[mid:], category)
        return self.merge_list_of_items(left_half, right_half, category)

# sort the list of items
    def merge_list_of_items(self, left_half, right_half, category):
        sorted_list_of_items = []
        left_half_index = right_half_index = 0

        while left_half_index < len(left_half) and right_half_index < len(right_half):
            if "book" in left_half[left_half_index] and "book" in right_half[right_half_index]:
                left_half_value = getattr(left_half[left_half_index]["book"], category, "")
                right_half_value = getattr(right_half[right_half_index]["book"], category, "")

                if left_half_value <= right_half_value:
                    sorted_list_of_items.append(left_half[left_half_index])
                    left_half_index += 1
                else:
                    sorted_list_of_items.append(right_half[right_half_index])
                    right_half_index += 1
            else:
                if "book" not in left_half[left_half_index]:
                    left_half_index += 1
                if "book" not in right_half[right_half_index]:
                    right_half_index += 1

        sorted_list_of_items.extend(left_half[left_half_index:])
        sorted_list_of_items.extend(right_half[right_half_index:])
        return sorted_list_of_items

    # Binary Search for searching library items
    def binary_search(self, sorted_books, search_key, search_value):
        low, high = 0, len(sorted_books) - 1
        while low <= high:
            mid = (low + high) // 2
            current_book = sorted_books[mid]
            current_value = getattr(current_book["book"], search_key, "Problem")
            if current_value == search_value:
                return current_book
            elif current_value < search_value:
                low = mid + 1
            else:
                high = mid - 1
        return None
