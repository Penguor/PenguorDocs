# Access Modifiers

Access modifiers control the visibility of types and members like systems, containers and variables.
There are four access modifiers in Penguor, `public`, `restricted`, `protected` and `private`.
Public types are accessible from everywhere in the code, while the other ones restrict visibility.
This is useful to encapsulate code, so that it's not accessible from everywhere.
Caring about the suiting access modifier will make your code cleaner and safer.

## Public

`public` is the least restrictive access modifier.
Public type members are visible from everywhere.
They should be used for anything you want to share throughout large parts of your code and they can even be accessed outside of the library.

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

!!! note
    Even though public types are a simple way of sharing data and structures,
    they shouldn't be overused in object-oriented programs as the code isn't encapsulated at all.

## Restricted

`restricted` limits the visibility of a type member to the base library.
That way, code in libraries can be hidden from external access, but still
be accessible from the complete project.

```Penguor
library ImageProcessing.Colour
{
    restricted dynamic system InternalColourHandler
    {
        public Colour doSth(Colour a, Colour b) {}
    }
}

library ImageProcessing.Main
{
    system ImageProcessing
    {
        void main()
        {
            InternalColourHandler handler = new InternalColourHandler()
            handler.doSth()
        }
    }
}
```

In this example, the main method is able to access the `InternalColourHandler` because they both share
the same base library `ImageProcessing`.

## Protected

The `protected` modifier restricts the accessibility of a type member
to derived members and itself.

```Penguor
system CharacterController
{
    protected string characterName;
}

system PlayerController : CharacterController
{
    public PlayerController(string playerName): characterName = playerName
}
```

## Private

The `private` modifier restricts the visibility of a structure to the parent structure.
The structure will not be visible from outside the system/container/type.

```Penguor
system CharacterController
{
    private bool beingTranslated;
    private bool beingRotated

    public bool beingTransformed(): return beingTranslated || beingTransformed
}
```

In this example, the two field `beingTranslated` and `beingRotated` are encapsulated
inside the `CharacterController` system. They are used to compute the return value
of the method `beingTransformed()`.
