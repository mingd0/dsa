import unittest

from queue_dm import Queue

class TestQueue(unittest.TestCase):
    
    def test_is_empty_true(self): 
        queue = Queue()
        self.assertTrue(queue.is_empty())
        
    def test_is_empty_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(5)
        queue.dequeue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.front, -1)
        self.assertEqual(queue.rear, -1)
    
    def test_is_empty_false(self):
        queue = Queue()
        queue.enqueue(5)
        self.assertFalse(queue.is_empty())
        
    def test_enqueue_one(self):
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.queue, [5])
        self.assertEqual(queue.front, 0)
        self.assertEqual(queue.rear, 0)
        
    def test_enqueue_two(self): 
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(6)
        self.assertEqual(queue.queue, [5, 6])
        self.assertEqual(queue.front, 0)
        self.assertEqual(queue.rear, 1)
        
    def test_enqueue_three(self):
        queue = Queue()
        for i in range(3):
            queue.enqueue(i)
        self.assertEqual(queue.queue, [0, 1, 2])
        self.assertEqual(queue.front, 0)
        self.assertEqual(queue.rear, 2)
        
    def test_enqueue_dequeue_three(self):
        queue = Queue()
        for i in range(3):
            queue.enqueue(i)
        result = []
        while not queue.is_empty():
            result.append(queue.dequeue())
        self.assertEqual(result, [0, 1, 2])
        
    def test_string(self): 
        string = 'abcdef'
        queue = Queue()
        result = ''
        for i in range(len(string)): 
            queue.enqueue(string[i])
        for i in range(len(string)):
            char = queue.dequeue()
            result += char
        self.assertEqual(result, string)
        
if __name__ == '__main__':
    unittest.main()