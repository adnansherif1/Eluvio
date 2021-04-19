# suffix-tree helps build a generalized suffix tree using ukkonens algorithm
from suffix_tree import Tree
from collections import Counter
import bitarray
import glob
import os


# function to find the longest strand of bytes(longest common substring) by finding the deepest shared node in the gst
def longest(root):
    # if a leaf is detected return the [0] (place holder for length), root.string_id(the file it belongs to)
    # and root.path.start(the offset of the root(not leaf) from the start of the file)
    if 'children' not in vars(root):
        return ([0],[[root.str_id]],[[root.path.start]])
    sub_len = []
    files = []
    start = []
    new_start=[]
    # calls the function recursively on each child
    for key,val in root.children.items():
        child_len, child_files, child_start = longest(val)
        sub_len, files, start= sub_len+child_len, files+child_files, start+child_start
        #a shared node only stores information about the first file so the offset of the root from the start 
        # of the file is calculated by checking the path.start of the child.
        #child is not a shared node where this value matters
        new_start.append(root.children[key].path.start)
    # max_val finds the length of the deepest shared node from among its children
    max_val = max(sub_len)
    #if children have shared nodes then details from the one with the deepest node is returned rest are ignored
    #here sub_len[idx] is the length from the root to the shared node so no calculations required at this stage
    #files, start also do not need modification
    if max_val > 0:
        idx = sub_len.index(max_val)
        return ([sub_len[idx]], [files[idx]],[start[idx]])
    # if none of the children have a shared node down the line it means one of two things
    # this could be a shared node or this is also not a shared node 
    else:
        unique_keys={}
        # if the files returned from all of its children are the same then it is not a shared node.
        # if there are 2 or more unique files returned then this is a shared node
        # the values of unique keys dict store the offset from the start of the file for the respective file
        for fil in files:
            assert len(fil) == 1
            unique_keys[fil[0]]=new_start[files.index(fil)] #will only have one element
        # dict keys and values (file names and offsets) are separated to be returned 
        new_files = list(unique_keys.keys())
        new_start = list(unique_keys.values())
        # if it is a shared node return zero for length 
        # else return the length of this node from the root of the tree
        return ([len(root.path) if len(unique_keys) > 1 else 0],[new_files],[new_start])




def main():
    # load all the files into a dictionary data where the keys are the names of the file 
    path = ''
    data = {}

    for filename in glob.glob(os.path.join(path, 'sample.*')):
        with open(os.path.join(os.getcwd(), filename), 'rb') as f: 
            data[filename] = f.read()
            print(filename)

    # length of each file
    '''
    for i in data.values():
      print(len(list(i)))
    '''
    # create a generalized suffix tree by passing in data dict containing file names and content
    t2 = Tree(data)

    # as shown below the:
    # length of the longest common byte substring is 27648
    # the files are sample.3 and sample.2
    # the starting offset for the files are 17408, 3072
    result = longest(t2.root)
    print('the length of the longest common substring(strand):',result[0][0])
    print('the files containing the strings are :',result[1])
    print('the starting offset in the respective files are:',result[2])

if __name__ == "__main__":
    main()
