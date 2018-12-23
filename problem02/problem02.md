# problem

## describe

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

## thought

首先想到的思路是将数组的所有数相乘，得到一个数`total_sum`，然后遍历这个数组，得到的结果就是`total_sum/array[i]`，**需要考虑的是数组中有一个或者多个0的边界条件**。这样的时间复杂度是O(n)。还有没有其他不用除法的解法呢？目前想到的思路只有两轮循环暴力解决，这样的好处是不需要考虑边界条件，缺点是时间复杂度无论如何都是O(n)。然后在stackoverflow上看到一个![很聪明的解法](https://stackoverflow.com/questions/2680548/given-an-array-of-numbers-return-array-of-products-of-all-other-numbers-no-div)，这种解法的时间复杂度是O(n)而且不需要使用除法，核心思路是构造两个数组。首先以length为4为example思考，那么结果就是`{ a[3]*a[2]*a[1], a[0]*[2]*a[3], a[1]*a[3]*a[0], a[0]*a[1]*a[2] }`，继续将问题抽象，会发现`{ 1, a[0], a[0]*a[1], a[0]*a[1]*a[2]}` 和`{a[1]*a[2]*a[3], a[2]*a[3], a[3], 1}`两数组对应索引相乘正好是正确结果（也需要判断为0的边界条件）