*********
 Penguor
*********

.. code-block:: none

   !#
    # library:docs
    # safety:2
    #!

   system Welcome
   {
       fn execute()
       {
           print("Welcome");
       }
   }

.. code-block:: none
   
   > Penguor Welcome.pgr
   Welcome

Welcome to the documentation of Penguor, a data-oriented programming language. This site covers the Penguor language reference as well as the developer documentation of the different Penguor projects.

Overview of the project:

.. toctree::
   :maxdepth: 2
   :name: Table of Contents
   
   Overview/index
   Language Reference/index

-------
 Links
-------

* Documentation source: https://github.com/Penguor/PenguorDocs
* PenguorCS compiler (currently being rewritten in Haskell): https://github.com/Penguor/PenguorCS
* Issue tracker: https://github.com/Penguor/PenguorCS/issues
