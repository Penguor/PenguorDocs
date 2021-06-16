# If/Else Statements

If/Else Statements execute code based on a condition.
In an if/else statement, zero or one of the possible branches are executed.

## If Statement

an if statement executes code based on a condition written in parentheses directly after the `if` keyword.
If the condition evaluates to `true`, the code will be executed. Otherwise the embedded code will be skipped.

```Penguor
if (true || false) {
    print("hit the if")
}
```

## Else If Statement

An `else if` statement executes its embedded code if none of the preceding `if` or `else if` statements evaluated to true and its condition
is true.

`else if` statements must directly follow an `if` or `else if` statement.

```Penguor
if (false) {
    // this will never execute
} else if (false) {
    //this will also never execute
} else if (true) {
    //this will execute
}
```

## Else Statement

Like the `else if` statement, an `else` statement executes its embedded code if none of the preceding `if` or `else if` statements evaluated to true.
It does however always execute the embedded code in that case, as it does not have a condition which must be met.

The `else` statement must directly follow an `if` or `else if` statement.
Therefore there may only be one else statement in an if/else statement.

```Penguor
void hasRemainder(i32 dividend, i32 divisor) {
    if(dividend % divisor == 0) {
        print("number has a remainder")
    } else {
        print("number has no remainder")
    }
}
```
