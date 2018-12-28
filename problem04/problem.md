# problem04

## describe

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

## thought

按从小到大排序数组，然后遍历这个数组，找到一个最小的满足:

- 大于等于0
- `array[i+1] - array[i] = 1`
- `result = array[i] + 1`
- 如果数组越界，那么直接返回array[i] + 1

(**注意这里有一个负数和正数之间的边界条件，也就是说第一个正数一定是1，然后再从这个1开始判断是否符合的重复逻辑,还有数组只有一个元素时候的边界条件**)，这种方法的时间复杂度是O(nlogn)

Google了一下之后发现其实还有更好的解决方法，能使时间复杂度降低到O(n)，这种思路利用了其实数组的index和数组的element的值其实是高度相关的关系，我们知道，缺失的最小元素，他的值的范围一定会在数组正数的size和1之间，即`1<=x<=size`，这样的话，我们就可以构造一个size等于数组的最大正数的全为0的数组，每遍历正数数组的元素时，就把元素的值减掉1对应的索引打上1，这样缺失的最小正数肯定是0数组第一个为0的索引加1，或者就等于数组的size。这种算法的时间复杂度是O(n)