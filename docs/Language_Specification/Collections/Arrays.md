# Arrays

Arrays are structures containing a number of variables.
They have a fixed size, which is determined during initialisation of the array.
The variables in arrays can be accessed by a zero-based index, which is written in square brackets after the name of the array.

## Declaration

Variables are defined to be arrays by putting a pair of square brackets behind their type.
It is also possible to create nested arrays. In that case, multiple pairs of brackets are being put behind the type.
The last variant of arrays available in Penguor are multi-dimensional arrays.
Those are defined by using commas to indicate how many dimensions the array should have.

```Penguor
i32[] numbers  // array
bool[][] uwu   // nested array

i32[,] dimensionalArray1   // 2-dimensional array
i32[,,] dimensionalArray2  // 3-dimensional array

// nested array with a 2-dimensional array inside of a one-dimensional array
char[][,]
```

## Initialisation

Arrays are initialised similar to how other variables are initialised, but instead of taking parameters inside of parentheses,
an array is initialised by putting the number of items  it can hold `n` into square brackets.
`n` can also be a variable of group num.

For multi-dimensional arrays, the size of each dimension is separated by commas.

```Penguor
i32[] numbers = new i32[5]

//initialisation using a variable
n = 3
u8[] bytes = new u8[n]

//initialise a 2-dimensional array
i32[,] twoD = new i32[5, 4]
```

### Initialisation with Values

Arrays can be initialised with values by providing a [collection](./index.md) of values after the type instead of a number inside of the square brackets.
Collections can also directly be assigned to an array.

```Penguor
i32[] digits = new i32[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 }

// direct assignment of a collection to an array
str[] daysOfWeek = { "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" }
```

## Access

To access the values of an array, the zero-based index of the desired value is put into square brackets after the identifier of the array.

```Penguor
print(daysOfWeek[2]) // prints Wednesday
```

## Future additions

- Add support for ranges in array access
