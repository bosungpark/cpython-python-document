from pprint import pprint
import parser
import symbol
import token

# st = parser.expr('a+1')
# pprint(parser.st2list(st=st))

def lex(expression:str):
    symbols = {v:k for k,v in symbol.__dict__.items() if isinstance(v, int)}
    tokens = {v:k for k,v in token.__dict__.items() if isinstance(v,int)}

    lexicon = {**symbols, **tokens}
    st = parser.expr(expression)
    st_list= parser.st2list(st=st)

    def replace(l:list):
        r = []
        for i in l:
            if isinstance(i, list):
                r.append(replace(i))
            else:
                if i in lexicon:
                    r.append(lexicon[i])
                else:
                    r.append(i)
        return r
    return replace(st_list)

pprint(lex("a+1"))
"""
['eval_input',
 ['testlist',
  ['test',
   ['or_test',
    ['and_test',
     ['not_test',
      ['comparison',
       ['expr',
        ['xor_expr',
         ['and_expr',
          ['shift_expr',
           ['arith_expr',
            ['term',
             ['factor', ['power', ['atom_expr', ['atom', ['NAME', 'a']]]]]],
            ['PLUS', '+'],
            ['term',
             ['factor',
              ['power', ['atom_expr', ['atom', ['NUMBER', '1']]]]]]]]]]]]]]]]],
 ['NEWLINE', ''],
 ['ENDMARKER', '']]
"""
##################### PARSER ###############################
"""
This cmd will show ast in web
>>> pip install instaviz
>>> python

>>> import instaviz

>>> def foo():
        a=1
        b=a+1
        return b

>>> instaviz.show(foo)
"""
"""
import ast
m= ast.parse('1~=2')
m.body[0].value.ops[0]

>>>
"""

