# Access Modifiers

Access modifiers control the visibility of types and members like system, containers and variables.
There are four access modifiers in Penguor, `public`, `restricted`, `protected` and `private`.
Public types are accessible from everywhere in the code, while the other ones restrict visibility.
This is useful to encapsulate code, so that it's not accessible from everywhere.
Caring about the suiting access modifier will make your code cleaner and safer.

## Public

`public` is the least restrictive access modifier.
Public type members are visible from everywhere.
They should be used for anything you want to share throughout large parts of your code and they can even be accessed outside of the assembly/library.

```Penguor  
public data PositionData
{
    public float x
    public float y
    public float z

    public PositionData(float x, float y, float z)
    {
        this.x = x
        this.y = y
        this.z = z
    }
}

dynamic system Enemy
{
    PositionData position = new PositionData(1, 0, 0)

    public void Move(): position.x++;
}
```

The `public` modifiers make the float variables accessible from everywhere outside the container. The same applies to the constructor.
the `public` before the container makes it visible outside the assembly, it's not restricted to it any more.


> **Note:**
Even though public types are a simple way of sharing data and structures,
they shouldn't be overused in object-oriented programs as the code isn't encapsulated at all.

## Restricted

## Protected

## Private

The `private` modifier restricts the visibility
