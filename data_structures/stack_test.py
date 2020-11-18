from stack_dm import Stack
import unittest

class TestStack(unittest.TestCase):
    
    def test_push_pop_one(self): 
        stack = Stack()
        stack.push(5)
        result = stack.pop()
        self.assertEqual(result, 5)
        
    def test_is_empty_true(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        
    def test_is_empty_false(self):
        stack = Stack()
        stack.push(5)
        self.assertFalse(stack.is_empty())
    
    def test_push_pop_three(self):
        stack = Stack()
        for i in range(3):
            stack.push(i)
        while not stack.is_empty(): 
            result = stack.pop()
        self.assertEqual(result, 0)
    
    def test_reverse_string_with_stack(self): 
        string = 'abcdef'
        stack = Stack()
        result = ''
        for i in range(len(string)): 
            stack.push(string[i])
        for i in range(len(string)):
            char = stack.pop()
            result += char
        self.assertEqual(result, 'fedcba')
        
    def test_peek_one(self):
        stack = Stack()
        stack.push(5)
        result = stack.peek()
        self.assertEqual(result, 5)
        
    def test_peek_three(self):
        stack = Stack()
        for i in range(3):
            stack.push(i)
        result = stack.peek()
        self.assertEqual(result, 2)
        
    def test_peek_doesnt_change_size(self): 
        stack = Stack()
        stack.push(5)
        stack.peek()
        self.assertFalse(stack.is_empty())
            
if __name__ == "__main__":
    unittest.main()