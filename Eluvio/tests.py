import unittest
from suffix_tree import Tree
from Eluvio_LCS import longest



class TestLCS(unittest.TestCase):
    def test_1(self):
        """
        Test string common among 2 strings
        """
        tree = Tree({'1':'xabzxa','2':'yabz'})
        result = longest(tree.root)
        self.assertEqual(result[0][0], 3)
        self.assertEqual(result[1][0], ['1', '2'])
        self.assertEqual(result[2][0], [1,1])

    def test_2(self):
        """
        Test string common among 2 strings where the string 1 
        """
        tree = Tree({'1':'axabxzaxabx','2':'ybxzxda'})
        result = longest(tree.root)
        self.assertEqual(result[0][0], 3)
        self.assertEqual(result[1][0], ['1', '2'])
        self.assertEqual(result[2][0], [3,1])
    def test_3(self):
        """
        Test string common among 3 strings
        """
        tree = Tree({'1':'xabzxabxab','2':'yabzdxabx',"3":"zavxabx"})
        result = longest(tree.root)
        self.assertEqual(result[0][0], 4)
        self.assertEqual(result[1][0], ['1', '2', '3'])
        self.assertEqual(result[2][0], [4, 5, 3])

       
        

if __name__ == '__main__':
    unittest.main()
