"""
Assessment 3.7: Sorting Algorithms
Full Name : Franz Ezekiel Lapon Teves
Sorting   : Insertion Sort

Rules:
  - Two arrays: unsorted and sorted
  - Duplicate letters are discarded
  - Symbols (spaces, digits, punctuation) are excluded
"""

FULL_NAME = "Franz Ezekiel Lapon Teves"


def build_unsorted_array(full_name):
    """Build the unsorted array: letters only, no duplicates (case-insensitive)."""
    unsorted = []
    for char in full_name:
        if not char.isalpha():      # exclude spaces and symbols
            continue
        letter = char.upper()       # F and f count as the same letter
        if letter not in unsorted:  # discard duplicates
            unsorted.append(letter)
    return unsorted


def insertion_sort(arr):
    """Sort a list in ascending (A to Z) order using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]                # element to insert into the sorted part
        j = i - 1

        # shift larger elements one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key            # place the key in its correct position
    return arr


def main():
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = insertion_sort(unsorted_array.copy())  # keep the original intact

    print("Full Name      :", FULL_NAME)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)


if __name__ == "__main__":
    main()
