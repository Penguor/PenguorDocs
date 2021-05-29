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

## Assembly representation

In assembly, boolean variables are one byte large and are either exactly `1` or `0`.

| literal | assembly representation |
| ------- | ----------------------- |
| true    | 1                       |
| false   | 0                       |
