from scr.datastr import Node, Stack
import unittest
def test_node_init():
    node = Node(10)
    assert node.data == 10
    assert node.next is None

def test_stac_init():
    stack = Stack()
    assert stack.top == None

def test_stack_push():
    stack = Stack()
    stack.push("a")
    assert stack.top.data == "a"
    assert stack.top.next == None

def test_stac_pop():
    stack = Stack()
    stack.push("1")
    stack.push("a")
    data = stack.pop()
    assert stack.top.data == "1"
    assert stack.top.next == None
    assert data == "a"
class NodeStackTestCase(unittest.TestCase):
    def est_node_init(self):
        node = Node(10)
        self.assertEqual(node.data,10)
        self.assertEquel( node.next, None)
    def test_stack_pop(self):
        stack = Stack()
        stack.push("1")
        stack.push("a")
        data = stack.pop()
        self.assertEqual(stack.top.data, '1')
        self.assertEqual(stack.top.next, None)
        self.assertEqual(data, "a")

    def test_stack_push(self):
        stack = Stack()
        stack.push("a")
        self.assertEqual (stack.top.data, "a")
        self.assertEqual (stack.top.next, None)

    def test_stac_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)


