# Data Types

Data types are the basic values of the language.

## Data Type Groups

Data type groups or static data types are a bit like interfaces or type classes in other languages.
There are different groups for data types. The most common ones are `num` for numeric data types and `char` for data types containing characters.

## Built-In Data Types

Penguor includes some basic data types. These are handled by the compiler, but nonetheless they must be defined in the standard library.

### Signed Integers

With the exception of `i8`, signed integers are the standard types being used for numbers.
`i32` is the standard type for signed integer numbers.

| Type | Also known as | Size    | Group |
| ---- | ------------- | ------- | ----- |
| i8   | sbyte         | 1 byte  | num   |
| i16  | short         | 2 bytes | num   |
| i32  | int           | 4 bytes | num   |
| i64  | long          | 8 bytes | num   |

### Unsigned Integers

`u32` is the standard type for signed integer numbers.

| Type | Also known as | Size    | Group |
| ---- | ------------- | ------- | ----- |
| u8   | byte          | 1 byte  | num   |
| u16  | ushort        | 2 bytes | num   |
| u32  | uint          | 4 bytes | num   |
| u64  | ulong         | 8 bytes | num   |

### Floating-Point Numbers

| Type | Also known as | Size    | Group |
| ---- | ------------- | ------- | ----- |
| f32  | float         | 4 bytes | num   |
| f64  | double        | 8 bytes | num   |

### Character-Containers

| Type | Also known as | Size     | Group |
| ---- | ------------- | -------- | ----- |
| char | char          | 12 bytes | char  |
| str  | string        | 0-?      | char  |

### Bool

| Type | Also known as | Size   | Group |
| ---- | ------------- | ------ | ----- |
| bool | boolean       | 1 byte | -     |

### Void

| Type | Also known as | Size | Group |
| ---- | ------------- | ---- | ----- |
| void | -             | -    | -     |

## Custom Data Types

Penguor provides the possibility of creating custom data types. A full guide can be found [here](./Custom_Data_Types.md)
