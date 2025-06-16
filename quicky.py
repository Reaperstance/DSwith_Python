class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self, beg, end):
        if beg >= end:
            return

        p = self.arr[(beg + end) // 2]  
        left = []
        mid = []
        right = []

        for i in self.arr[beg:end+1]:
            if i < p:
                left.append(i)
            elif i == p:
                mid.append(i)
            else:
                right.append(i)

        self.arr[beg:end+1] = left + mid + right  

        mid_start = beg + len(left)
        mid_end = mid_start + len(mid) - 1

        self.sort(beg, mid_start - 1)
        self.sort(mid_end + 1, end)

    def get_sorted(self):
        return self.arr

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
qs = QuickSort(arr)
qs.sort(0, len(arr) - 1)
print("Sorted array:", qs.get_sorted())
