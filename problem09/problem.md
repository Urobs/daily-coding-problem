# problem

## describe

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

## thought

定义两个变量incl 和 excl分别代表当前遍历的元素的包含前一个元素的sum和不包含前一个元素的sum，然后每次循环把当前元素与excl相加作为下一轮循环的incl，然后取Max(当前incl, excl) 作为下一轮的excl，这样就保证了每一轮循环返回的都为incl和excl的sum的最大值。基本思路就是保证每一轮循环都能在满足规则的前提下取到最大值，试着吧序列从小区间里面切割，把关注点放在每两个元素上，这样一般的假设只有两个元素的序列就是直接返回两个中的最大值，然后在思考具有第三个元素的序列，那么对于这个序列来说有两种情况，一种是第一个元素与第三个相加，另一种就是第二个元素。进一步抽象，把这几个元素封装起来作为一个黑箱，黑箱返回的是序列的满足规则的最大值，那么对于下一个元素来说要么本身大于黑箱的返回值，要么继续还是黑箱的值。这里的黑箱还需要满足规定的条件也就是说必须不相邻。