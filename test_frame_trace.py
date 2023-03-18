import sys
import dis
import traceback
import io

def my_trace(frame, event, args):
    """
    cmd -> cpython/python.exe test_frame_trace.py
    """
    frame.f_trace_opcodes = True
    stack= traceback.extract_stack(frame)
    pad = "   "*len(stack) + "|"
    if event == "opcode":
        with io.StringIO() as out:
            dis.disco(frame.f_code, frame.f_lasti, file=out)
            lines= out.getvalue().split('\\n')
            [print(f"{pad}{l}") for l in lines]
    elif event == "call":
        print(f"{pad} Calling {frame.f_code}")
    elif event == "return":
        print(f"{pad} Returning {args}")
    elif event == "line":
        print(f"{pad} Changing line to {frame.f_lineno}")
    else:
        print(f"{pad}{frame} ({event} - {args})")
    print(f"{pad}----------------------------------------")
    return my_trace

sys.settrace(my_trace) # Set my_trace as a default trace function in thread
eval('"-".join([letter for letter in "hello"])')

"""
      | Calling <code object <module> at 0x10553f3a0, file "<string>", line 1>
      |----------------------------------------
      | Changing line to 1
      |----------------------------------------
      |  1 -->       0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
    -->       2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
    -->       4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
    -->       6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
    -->       8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
    -->      10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
    -->      12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
    -->      14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
         | Calling <code object <listcomp> at 0x10553f2f0, file "<string>", line 1>
         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1 -->       0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
    -->       2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
    --> >>   14 RETURN_VALUE

         |----------------------------------------
         | Returning ['h', 'e', 'l', 'l', 'o']
         |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
    -->      16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x10553f2f0, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
    -->      18 RETURN_VALUE

      |----------------------------------------
      | Returning h-e-l-l-o
      |----------------------------------------
(base) parkbosungui-MacBookAir:cpython parkbosung$ /usr/local/bin/python3 /Users/parkbosung/Desktop/cpython/test_frame_trace.py
      | Calling <code object <module> at 0x7fa2381300e0, file "<string>", line 1>
      |----------------------------------------
      | Changing line to 1
      |----------------------------------------
      |  1 -->       0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
    -->       2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
    -->       4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
    -->       6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
    -->       8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
    -->      10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
    -->      12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
    -->      14 CALL_FUNCTION            1
             16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
         | Calling <code object <listcomp> at 0x7fa238130030, file "<string>", line 1>
         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1 -->       0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
    -->       2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
    -->       6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
    -->       8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
    -->      10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
    -->      12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         | Changing line to 1
         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
    --> >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
        >>   14 RETURN_VALUE

         |----------------------------------------
         |  1           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 14)
              6 STORE_FAST               1 (letter)
              8 LOAD_FAST                1 (letter)
             10 LIST_APPEND              2
             12 JUMP_ABSOLUTE            4
    --> >>   14 RETURN_VALUE

         |----------------------------------------
         | Returning ['h', 'e', 'l', 'l', 'o']
         |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
    -->      16 CALL_METHOD              1
             18 RETURN_VALUE

      |----------------------------------------
      |  1           0 LOAD_CONST               0 ('-')
              2 LOAD_METHOD              0 (join)
              4 LOAD_CONST               1 (<code object <listcomp> at 0x7fa238130030, file "<string>", line 1>)
              6 LOAD_CONST               2 ('<listcomp>')
              8 MAKE_FUNCTION            0
             10 LOAD_CONST               3 ('hello')
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 CALL_METHOD              1
    -->      18 RETURN_VALUE

      |----------------------------------------
      | Returning h-e-l-l-o
      |----------------------------------------
"""