from unittest import TestCase, main
from sorting import sorting_num as sn
import tkinter

class HeapSortTest(TestCase):
    def test_notsorted(self):
        """Тестирование неотсортированного списка"""
        call = sn.heap_sort([5, 567, 1, 0])
        result = [0, 1, 5, 567]
        self.assertEqual(call, result)

    def test_sorted(self):
        """Тестирование отсортированного списка"""
        call = sn.heap_sort([33, 67, 89, 4567])
        result = [33, 67, 89, 4567]
        self.assertEqual(call, result)

    def test_empty(self):
        """Тестирование пустого списка"""
        call = sn.heap_sort([])
        result = []
        self.assertEqual(call, result, 'Ошибка, функция heap_sort не может отсортировать пустой список')

if __name__ == '__main__':
    window = tkinter.Tk()
    window.mainloop()