# problem

## describe

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

## thought

常规思路是遍历然后得出size，然而更好的方法是使用![reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)算法.![正确性证明](../image/reservoir_sample.svg)