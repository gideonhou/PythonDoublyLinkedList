from PythonDoublyLinkedList import DoublyLinkedList
import unittest

class testDoublyLinkedList(unittest.TestCase):
    # set up
    def setUp(self):
        self.ll = DoublyLinkedList();
        
    # tear down
    def tearDown(self):
        return;

    # test for first sinert
    def test_firstinsert(self):
        self.assertEqual(self.ll.size, 0);
        self.assertEqual(self.ll.insert(1), True);
        self.assertEqual(self.ll.size, 1);
        return;

    # test for incorrect insert type
    def test_falseinsert(self):
        self.ll.insert(0);
        self.assertEqual(self.ll.insert("bad insert"), False);
        self.assertEqual(self.ll.size, 1);
        return;

    # tests LL's insert method by inserting sequential elements
    def test_sequentialinsert(self):
        insertArray = xrange(0, 9);
        for el in insertArray:
            self.assertEqual(self.ll.insert(el), True);
        self.assertEqual(self.ll.size, 9);

        elements_ll = self.ll.get_list();
        for a, b in zip(insertArray, elements_ll):
            self.assertEqual(a, b);

        self.assertEqual(self.ll.head.data, 0);
        self.assertEqual(self.ll.tail.data, 8);
        self.ll.clear();
        self.assertEqual(self.ll.head, None);
        self.assertEqual(self.ll.tail, None);
        self.assertEqual(self.ll.size, 0);
        self.assertEqual(self.ll.type, None);
        return;
    
    # tests LL's get method
    def test_get(self):
        insertArray = xrange(0, 20);
        for el in insertArray:
            self.ll.insert(el);
        for it in insertArray:
            self.assertEqual(self.ll.get(it), it)

        self.assertEqual(self.ll.get(100), False);
        self.assertEqual(self.ll.get('not an int'), False);
        return;

    # tests LL's delete method
    def test_delete(self):
        insertArray = xrange(0, 10);

        self.assertEqual(self.ll.delete(4), False);

        for el in insertArray:
            self.ll.insert(el);

        self.assertEqual(self.ll.delete(20), False);
        self.assertEqual(self.ll.delete(0), True);
        self.assertEqual(self.ll.head.data, 1);
        self.assertEqual(self.ll.size, 9);
        self.assertEqual(self.ll.tail.data, 9);

        self.assertEqual(self.ll.delete(9), True);
        self.assertEqual(self.ll.tail.data, 8)
        self.assertEqual(self.ll.size, 8)

        self.assertEqual(self.ll.delete(4), True);
        self.assertEqual(self.ll.size, 7);
        self.assertEqual(self.ll.head.data, 1);
        self.assertEqual(self.ll.tail.data, 8);
        return;

    def test_fill_delete_fill(self):
        insertArray = xrange(0, 10);

        for el in insertArray:
            self.ll.insert(el);

        self.assertEqual(self.ll.head.data, 0);
        self.assertEqual(self.ll.tail.data, 9);
        self.assertEqual(self.ll.size, 10);
        self.assertEqual(self.ll.type, type(0));

        for el in insertArray:
            self.ll.delete(el);

        self.assertEqual(self.ll.head, None);
        self.assertEqual(self.ll.tail, None);
        self.assertEqual(self.ll.size, 0);
        self.assertEqual(self.ll.type, None);

        insertCharArray = ['a', 'b', 'c', 'd']

        for l in insertCharArray:
            self.ll.insert(l);

        self.assertEqual(self.ll.head.data, 'a');
        self.assertEqual(self.ll.tail.data, 'd');
        self.assertEqual(self.ll.size, 4);
        self.assertEqual(self.ll.type, type('a'));

        return;
    
    def test_sort0(self):
        self.ll.insert(5);
        self.ll.insert(4);
        self.assertEqual(self.ll.size, 2);
        self.assertEqual(self.ll.get_list(), [5, 4]);

        self.ll.sort();

        self.assertEqual(self.ll.get_list(), [4,5]);
        self.assertEqual(self.ll.head.data, 4);
        self.assertEqual(self.ll.tail.data, 5);
        return;

    def test_sort1(self):

        self.ll.insert(5);
        self.ll.insert(4);
        self.ll.insert(3);
        self.assertEqual(self.ll.get_list(), [5, 4, 3]);

        self.ll.sort();

        self.assertEqual(self.ll.get_list(), [3,4,5]);
        self.assertEqual(self.ll.head.data, 3);
        self.assertEqual(self.ll.tail.data, 5);
        return;

    def test_sort2(self):

        self.ll.insert(12);
        self.ll.insert(14);
        self.ll.insert(6);
        self.ll.insert(10);
        self.ll.insert(8);
        self.ll.insert(2);
        self.ll.insert(0);
        self.ll.insert(-5);
        self.ll.insert(20);

        self.ll.sort();
        self.assertEqual(self.ll.get_list(), [-5, 0, 2, 6, 8, 10, 12, 14, 20])
        self.assertEqual(self.ll.head.data, -5);
        self.assertEqual(self.ll.tail.data, 20);
        return;

    def test_sort3(self):

        testArray = xrange(0, 10);
        for el in testArray:
            self.ll.insert(el);

        self.ll.sort();
        self.assertEqual(self.ll.get_list(), [0,1,2,3,4,5,6,7,8,9]);
        return;
    
if __name__ == "__main__":
    unittest.main() # run all tests
