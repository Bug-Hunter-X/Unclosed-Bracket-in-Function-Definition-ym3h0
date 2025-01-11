def function_with_unclosed_bracket(a):
    if a > 5:
        return a * 2
    else:
        return a + 2 # Missing closing bracket

result = function_with_unclosed_bracket(10)