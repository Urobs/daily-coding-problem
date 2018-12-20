# problem01

## describe

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

## thought

首先想到的算法是根据排列组合的思路从数组第一个元素开始遍历，选定这个元素，然后遍历比该元素索引大的元素相加，看是否与给定值k相等，相等的话就返回true，
这样的时间复杂度就是O(n^2)
进一步思考，先把数组从小到大排序，然后从数组的两端进行遍历（记为i和j），每一轮循环比较`a[i]`和`a[j]`之和，如果小于给定值k那么`i+1`，如果大于给定值那么`j+1`，如果等于那么返回true，每进行一次循环，结果的范围就会缩小1。那这样遍历这个数组的时间复杂度就是O(n)，算法的时间复杂度是排序算法的复杂度。