"""
cmd: python ./test_symviz.py

symbol table manage the scope of variables
"""
import tabulate
import symtable

code = """
def cal_pow(a,b):
    return a**b

a=1
b=2
c= cal_pow(a,b)
"""

_st = symtable.symtable(code, "test_symviz.py", "exec")

def show(table):
    print("Symtable {0} ({1})".format(table.get_name(), table.get_type()))

    print(
        tabulate.tabulate(
        [
            (
                symbol.get_name(),
                symbol.is_global(),
                symbol.is_local(),
                symbol.get_namespaces(),
            )
        for symbol in table.get_symbols()
        ],
        headers=["name","global", "local", "namespaces"],
        tablefmt="grid"
        )
    )

    if table.has_children():
        [show(child) for child in table.get_children()]

show(_st)
"""
Symtable top (module)
+---------+----------+---------+--------------------------------------------------------+
| name    | global   | local   | namespaces                                             |
+=========+==========+=========+========================================================+
| cal_pow | True     | True    | [<Function SymbolTable for cal_pow in test_symviz.py>] |
+---------+----------+---------+--------------------------------------------------------+
| a       | True     | True    | ()                                                     |
+---------+----------+---------+--------------------------------------------------------+
| b       | True     | True    | ()                                                     |
+---------+----------+---------+--------------------------------------------------------+
| c       | True     | True    | ()                                                     |
+---------+----------+---------+--------------------------------------------------------+
Symtable cal_pow (function)
+--------+----------+---------+--------------+
| name   | global   | local   | namespaces   |
+========+==========+=========+==============+
| a      | False    | True    | ()           |
+--------+----------+---------+--------------+
| b      | False    | True    | ()           |
+--------+----------+---------+--------------+
"""