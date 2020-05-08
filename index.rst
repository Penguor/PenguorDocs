*********
 Penguor
*********

.. code-block:: c

    #safety 2

    library Docs
    {
        system Welcome
        {
            fn void execute()
            {
                print("Welcome");
            }
        }
    }

.. code-block:: none
   
    > Penguor Welcome.pgr
    Welcome

Welcome to the documentation of Penguor, a data-oriented programming language.
This site covers the Penguor language reference as well as the developer documentation of the different Penguor projects.

.. toctree::
    :maxdepth: 2
    :name: mastertoc
    :includehidden:
    
    Overview/index
    Language_Reference/index
    Developer_Documentation/index

-------
 Links
-------

* Documentation source: https://github.com/Penguor/PenguorDocs
* PenguorHS compiler: https://github.com/Penguor/PenguorHS
* Issue tracker: https://github.com/Penguor/PenguorHS/issues
