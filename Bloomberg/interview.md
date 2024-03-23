# Bloomberg Interview Research
- Know Before You Go
- (Discussion)[https://leetcode.com/discuss/interview-question/329221/Bloomberg-or-Phone-screen-or-Software-Development-Internship-2019]
    * Algos: Search, sort, traverse
    * Problem solving techniques: 2 points, recognize [first in, first out] ops, combining several data structures
- Asked questions:
    - Technical
        - Specific Questions:
            * BFS Graph Traversal, Binary Tree Backtracking, Hashing
            * min stack problem (2)
            * [LC High Frequency](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/)
            * Invalid Transactions
            * Shuffle LL randomly, Graph Problem: number of island (2)
            * dfs search on BST w/ no limit of leaves for each level
            * build stock class where you get last stock added to portfolio
            * word search (medium)
            * [top 100 lc questions](https://leetcode.com/discuss/interview-question/4258631/Top-100-DSA-Interview-Questions)
            * create ds for subway system tracking system
            * ll with random pointers
            * implement ll from scratch, determine if ll is circular
            * merge linked list with down pointer
                - linked list with next, down node (higher priority) -> convert to normal list
            * meeting rooms 2
            * variation of merge sort
            * validate bst
            * __LRU CACHE__
            * decode a string
            * balanced parentheses
        - Topics:
            * questions related to hash maps, trees
            * anagrams
            * array, bsts
            * memoization
            * explain how hash maps work
            * scale a process with multi threading
            * bfs, recursion, trees, hashmaps, bst
            * ll, dp, hash table, stacks
        - Managerial round
            * grokking course - sys design
        - [Reddit Interview](https://www.reddit.com/r/csMajors/comments/xmw0sh/my_bloomberg_interview_experience/)
            * verbose min stack problem (solved nc)
            * balanced parentheses
            * all paths from source to destination
            * hashmap problem
    - Behavioral:
        * why bloomberg, every line on resume, recent projects, successes
        * [PREP](https://docs.google.com/document/d/1s3Z4BEtSlXJkGaiz2gHOfMORRP7bVY7GpUfPODayJFI/edit)


- Phone Interview Questions
    1.
    ```
    Eg. String "abc" should output
        empty string
        a
        b
        c
        ab
        bc
        ac
        abc
    ```
    2. Two City Scheduling
    3. Electronic Exchange
    ```
    You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of
    product name and its traded volume of stocks. Eg: {name: vodafone, volume: 20}. What data structure will you
    maintain if:
    * You have to tell top k products traded by volume at end of day.
    * You have to tell top k products traded by volume throughout the day.
    ```
    4. Insert Delete Get Random O(1)
    ```
        Design a data structure with requirements:
        You have a <Key, Value> structured input data for all objects
        Where you have
        Insert : O(1)
        Lookup : O(1)
        Delete : O(1)
        You can traverse the added elements in the order they were inserted.
    ```
    5. 1D Candy Crush
    6. Remove Parentheses to make Balanced
    7. LRU Cache
    8. Decode String
    9. Valid Anagram
    10. Palindrome Number, Flatten multi-level doubly LL
    11. Output data from stream in order
    ```
        Input: (1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl")

        Write a program to output the data from the stream in realtime in order, so 1,2,3,4,5..
        You cannot queue up the incoming data from the stream.
        So for example if the first incoming bit of data is (1, "abcd"), and the second is (4, "mnop"), you cannot output (4, "mnop") until you get 2, 3.
    ```
    12. Find min steps to generate number given only two operations
    13. Reorder array based on dict
    14. Word Break 2, Subsets
    16. Longest substr w/o repeating chars
    17. First Unique Element, Flatten Linked List
    18. File Diffs with RAM Constraints
    19. Right side of binary tree, Word Search I

    * Example Process
        - Why Bloomberg
        - OOP Questions
        - Python v Java v Javascript
            1. intersection of 2 linked lists
            2. Candy crush
            3. merge intervals
            4. add 2 numbers
            5. interleaving strings
            6. insert delete getRandom
            7. Occurence sort: given a string sort the string based on the number of times a letter appears in the string from most occurring to least occurring. For letters having the same occurrence sort based on lexicographical order
            8. Trap rain water
            9. Two sum
            10. iterative, recursive Binary search
            11. 3sum
            12. def of BST, coding Q: find kth largest element in BST
