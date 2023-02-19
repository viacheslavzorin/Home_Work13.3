from scr.datastr import Node, Stack

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