# problem

## describe

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

## thought

这道题目，给出一个不确定位数的编码数据,求能解码出几个字符数据，实质上可以转化为求对这个字符串分区间的问题，因为给出的映射表只有1位或者两位，且给出的信息是可编码的，那不妨对于每一个具体的字符去考虑，对于每一个字符，我们的编码方式只有两种，单个字符编码，或者和旁边的字符组成一个编码，那么我们就可以递归地去处理这个问题，也就是说每次选定一个字符,递归地解决问题。注意下面边界条件

- 字符串最后一个数为0
- 遍历到单个字符为0
- 最后的递归区间只剩下1个数