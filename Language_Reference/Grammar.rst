*********
 Grammar
*********

The grammar of Penguor is written down in abnf, the Augmented Backus-Naur-Form.

Each Penguor program consists out of a head and one or more declarations.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 9
   :linenos:

In the head, various properties of a program, such as the library the code belongs to and the safety level, are defined.
Moreover it includes the libraries to import from.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 13-16
   :linenos:

Penguor provides several structures containing and/or iterating over data.
*(Declarations are subject to change as they currently only are modelled after the ECS approach)!*

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 20-25
   :linenos:

Systems iterate instructions over data, but they barely contain any data on their own.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 28
   :linenos:

Components contain data, but no logic.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 30
   :linenos:

Custom data types define how data of that type is stored and how to work with it.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 32
   :linenos:

Statements are instructions. Penguor supports do, while and for loops as well as if and switch statements.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 36-42
   :linenos:

Block statements group other statements into blocks. For example, they group the contents of systems, components and methods.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 45
   :linenos:

If statements provide control structures that only execute code if a certain condition is true.
Using elif, if statements can be nested to only do something, if a condition is true and previous conditions aren't met.
Finally, code found in the else block

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 47-49
   :linenos:

While loops execute code repeatedly as long as a certain condition is met.
The condition is checked before the code is executed.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 52
   :linenos:

For loops iterate code over every data in an enumerable type. 

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 54
   :linenos:

Do ... while loops execute code repeatedly while a condition is met.
The condition is first checked after the code was executed once.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 56
   :linenos:

Switch statements are a control mechanism executing code contained in a case block base on the value of a variable.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 58-60
   :linenos:

Expression statements are standalone expressions.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 62
   :linenos:

every expression currently is an assignment.
Assignments assign values to variables.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 66-69
   :linenos:

``||`` (or) returns true if one or both of the expressions are true.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 71
   :linenos:

``&&`` (and) returns true if both of the expressions are true.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 73
   :linenos:

| ``==`` returns true if the expressions are equal.
| ``!=`` returns true if the expressions aren't equal.

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 75
   :linenos:

| ``<`` returns true if the expression on the left is smaller than the expression on the right
| ``>`` returns true if the expression on the left is greater than the expression on the right
| ``<=``
| ``>=``

.. literalinclude:: ../Grammar/Penguor.abnf
   :language: abnf
   :lines: 77
   :linenos: