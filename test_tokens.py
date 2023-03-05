"""
cpython/python.exe -m tokenize -e test_tokens.py
"""
def function():
    proceed  # Syntax I created, This is not official syntax of python.

"""
토큰의 위치            토큰의 이름       토큰의 값

0,0-0,0:            ENCODING       'utf-8'        
1,0-1,3:            NAME           'def'          
1,4-1,12:           NAME           'function'     
1,12-1,13:          LPAR           '('            
1,13-1,14:          RPAR           ')'            
1,14-1,15:          COLON          ':'            
1,15-1,16:          NEWLINE        '\n'           
2,0-2,4:            INDENT         '    '         
2,4-2,11:           NAME           'proceed'      
2,11-2,12:          NEWLINE        ''             
3,0-3,0:            DEDENT         ''             
3,0-3,0:            ENDMARKER      '' 
"""
