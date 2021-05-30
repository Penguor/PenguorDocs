# Bool

Variables of type `bool` contain a boolean value (`true` or `false`).

## Code representation

Boolean variables are being represented by the two literals`true` and `false`.
They can be assigned to any variable of type `bool` and boolean operations such as and (`&&`), or (`||`) and equals (`==`) can be performed on them.

```Penguor
str beverage;
bool withSparkles = true

if (withSparkles) {
    beverage = "Schorle"
} else {
    beverage = "Saft"
}
```

## Control Structures

Most control structures in Penguor choose which branch to follow based on a boolean value.
This can either be a `bool` variable or a boolean literal, or it can be anything that evaluates to a boolean value, e.g.
a method or a comparison.

```Penguor
i32 i = 0

// using a comparison to determine if the loop should be run
while(i < 5) {
    print(i)
    i++
}
```

## Boolean Operations

Boolean operators are discussed more in-depth in the [Operators](../../Operators/index.md) documentation, but the table below provides on overview
over the operations which can be done with boolean operators in penguor.

| Name        | Operator | description                                                                |
| ----------- | -------- | -------------------------------------------------------------------------- |
| Logical And | `&&`     | returns `true` if both variables are `true`                                |
| Logical Or  | `||`     |  returns `true` if at least one variable is `true`                         |
| Equals      | `==`     | returns `true` if both variables are equal                                 |
| Not Equals  | `!=`     | returns `true` if exactly one `bool`-variable is `true` and one is `false` |
| Not         | `!`      | inverts the `bool`-variable                                                |

## Assembly representation

In assembly, boolean variables are one byte large and are either exactly `1` or `0`.

| literal | assembly representation |
| ------- | ----------------------- |
| true    | 1                       |
| false   | 0                       |
