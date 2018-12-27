# problem04

## describe

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

## thought

按从小到大排序数组，然后遍历这个数组，找到一个最小的满足

- 大于等于0
- `array[i+1] - array[i] = 1`
- `result = array[i] + 1`
- 如果数组越界，那么直接返回array[i] + 1