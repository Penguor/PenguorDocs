# Collections

Collections are groups of variables of a specific type.
There are fixed-size collections, like [arrays](./Arrays.md), as well as dynamically sized collections.

## Code Representation

Collections can be represented in code by a comma-separated list of expressions inside of a block expression.

```Penguor
char[] hi = { 'H', 'e', 'l', 'l', 'o' }
i32[] evenNumbers =
    {
        1 * 2,
        2 * 2,
        3 * 2,
        4 * 2
    }
```

## Access

As collections are an abstract concept, there is no defined way to access the values inside of a collection.
Instead this depends on the structure which it is assigned to, which can, for example, be an [array](./Arrays.md) or a [list](./Lists.md).
