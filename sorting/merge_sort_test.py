from unittest import TestCase, main
from sorting import sorting_num as sn
import tkinter

class MergeSortTest(TestCase):
    def test_notsorted(self):
        call = sn.merge_sort([5, 567, 1, 0, -15])
        result = [-15, 0, 1, 5, 567]
        self.assertEqual(call, result)

    def test_sorted(self):
        call = sn.merge_sort([-6, 33, 67, 89, 4567])
        result = [-6, 33, 67, 89, 4567]
        self.assertEqual(call, result)

    def test_empty(self):
        call = sn.merge_sort([])
        result = None
        self.assertEqual(call, result, 'Ошибка, функция merge_sort не может отсортировать пустой список')

if __name__ == '__main__':
    window = tkinter.Tk()
    window.mainloop()