from tree import Node
import unittest


class TestNodeTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Node(data="a")

        self.subtree1 = Node("b")
        self.leaf1 = Node("c")
        self.leaf2 = Node("d")
        self.subtree1.insert(self.leaf1)
        self.subtree1.insert(self.leaf2)

        self.subtree2 = Node("e")
        self.leaf3 = Node("f")
        self.leaf4 = Node("g")
        self.subtree2.insert(self.leaf3)
        self.subtree2.insert(self.leaf4)

        self.tree.insert(self.subtree1)
        self.tree.insert(self.subtree2)

        return super().setUp()

    def test_tree_has_leaf(self):
        self.assertTrue(self.tree.has_descendant(self.leaf4))

    def test_tree_has_self_as_descendant(self):
        self.assertTrue(self.tree.has_descendant(self.tree))

    def test_tree_does_not_have_orphan(self):
        self.assertFalse(self.tree.has_child(Node("h")))

    def test_cannot_insert_int(self):
        with self.assertRaises(TypeError):
            self.tree.insert(0)

    def test_cannot_insert_str(self):
        with self.assertRaises(TypeError):
            self.tree.insert("")

    def test_cannot_insert_object(self):
        with self.assertRaises(TypeError):
            self.tree.insert(object)

    def test_cannot_insert_builtin_class(self):
        with self.assertRaises(TypeError):
            self.tree.insert(int)


if __name__ == "__main__":
    unittest.main()
