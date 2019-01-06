# problem

## describe

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up qies.

## thought

遍历list查找。思考后发现另外一种思路是利用Trie tree,这种方法的时间复杂度能达到O(n)但是空间复杂度会达到O(ALPHABET_SIZEkey_lengthN)