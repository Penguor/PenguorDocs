# Custom Data Types

!!! warning
    This is a very early draft (almost a year old) and it's not reflecting the current state of Penguor.

Penguor provides a way of creating own data types depending on your needs.

## Defining data types

A data type is defined in a regular Penguor Source File (.pgr). The basic syntax for a simple data type is:

```Penguor
type name < group
{
    size;
    properties
    {
        property1;
        property2;
        ...
    }
    process
    {
        operator +(name a, name b)
        {
            // do something
            return c;
        }
    }
}

```

So let's go through this bit by bit.

Each data type definition starts with `type`. This tells the compiler that the following code is a data type.

The next part is the `name`. It describes exactly what it is called.

`group` in the square brackets defines the group of the data type. Each data type belongs to a group, which describes the content.
E.g. a data type int[num] can only contain numbers. More on this can be found in [groups](../Groups.md#Data_Types)

The reserved size in memory for the data type is set through `size:number` where `number` is the reserved space in memory in bits.

each group

The
