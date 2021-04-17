***********************
 Design Considerations
***********************

This document contains some design considerations that were taken into account when developing Penguor.
New features should be checked against these considerations to make sure they fit with the general concept of Penguor.

============================
 Learning and Safety Levels
============================

As Penguor has to be very fast, it is possible to write very low-level code with it.
This has the disadvantage that it isn't very easy to learn.

To solve this problem, Penguor features are categorized into three safety levels, going from 0 to 2.
For example, code in level 2 is garbage collected, in level 0 memory is manually allocated and unallocated.

When designing new features, they should be coded in one of those levels.
That doesn't mean though they can only be used in equal or lesser safety levels.

======================
 Programming Paradigm
======================

Penguor is a data-oriented language, which means it is centered around storing and transforming data efficiently.

Features should be centered around the data transformation.
It is essential for features to perform transformations as fast as possible.

=================
 Assembly and IR
=================

Before converting the AST to assembly, Penguor converts it into an intermediate representation to optimize the code even further.

When designing new Penguor features, there should go some thought and, if necessary, research into the IR and assembly representation of that feature.

=================
 Multi-Threading
=================

One of the advantages of data-oriented design is that code is easy to execute on multiple threads.
This is due to the fact that it is easy to determine which code needs access to which things and therefore can or cannot be run in parallel.

Ideally, features should be able to run on multiple threads at once. This isn't a requirement though.