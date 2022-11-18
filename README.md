I have writen a code for compunded words in which we have to find the largest compunded word and second largest compunded word in lexicographical order(if two words having same length).

APPROACH:

loc = r"H:\code_impledge" ---> refers to the path of input file's in the same folder.

I have used the idea of DFS data structure to work with the code in order to avoid the repetition of compunded words.In my code ,dict1={} is used for the same. While implementing the above approach i have used a stack(st=[]) which stores the final length of compounded word and a for loop which indicates connection between the words in compounded words.

An anonumous function(lambda function) is used for sorting the list according to the length and in lexicographical order. I hope the code is fairly straight forward.
