# Eluvio
Core softwware engineering

Thanks for introducing me to this problem and the resulting mindblowing algorithms.

**Runtime:**
The solution runs in LINEAR TIME o(KN) with respect to the number of files and the length of each file. Here K is the number of files and N is the average number 
of bytes in a file.

**Solution:**
Ukkonen's algorithm is used to create a generalized suffix tree in o(KN) time (library).

custom function (longest) finds the longest common substring by finding the deepest node in the suffix tree that is shared by two or more of the files. Runs in o(KN)
  -the length of the longest common substring (strand of bytes) is the length of the path from the root to the deepest shared node.
  -Offset is the offset of the root from the beginning of the file for each of the files.
 
**Future improvements**

Use parallel computing and cache optimization if possible to further speed up ukkonens algorithm.
