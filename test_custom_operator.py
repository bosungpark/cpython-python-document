"""
cmd: cpython/python.exe
"""
import ast

m= ast.parse('1~=2')
m.body[0].value.ops[0] # <ast.AlE object at 0x100dcb220>

assert 1.0~=1.01 # This is my custom operator, Test it in cmd line