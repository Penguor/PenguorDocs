# Declarations

## Modifiers

Certain declarations may have modifiers. Modifiers further specify the behaviour of a declaration.
There are both [access modifiers](../Modifiers/Access_Modifiers.md) and [non-access modifiers](../Modifiers/Non_Access_Modifiers.md).
A declaration may have zero or one access modifier, same goes with non-access modifiers.

The access modifier must come before the non-access modifier, like in the example below.
`private` is the access modifier and `static` is the non-access modifier.

```Penguor
private static void help() {
    print("Help:\n")
}
```
