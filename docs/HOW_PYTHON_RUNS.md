# How Python Runs

When running `python scratch/hello.py`, Python executes the file as a script from top to bottom.

When importing `hello`, Python loads the module and executes its top-level code.

Python caches imported modules as compiled bytecode (`.pyc`) inside a `__pycache__` directory.

The `__pycache__` directory can appear when a module is imported.

With `python -i hello.py`, Python first executes the file and then keeps the interpreter open.

An imported module is stored in `sys.modules`.

If `import hello` is executed again in the same Python session, Python does not execute the module again.

Running a file and importing it are therefore different: running executes it as the main script, while importing loads it as a module.

The `-i` option is useful because it lets us inspect variables created by the executed script.

`__pycache__` improves import performance by allowing Python to reuse compiled bytecode.
