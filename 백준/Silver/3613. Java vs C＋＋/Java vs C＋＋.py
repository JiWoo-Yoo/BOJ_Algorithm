# C++ -> Java, Java -> C++

variable = input()
answer = ''
is_error = False

if not variable:
    answer = 'Error!'
elif '_' in variable: # C++ => Java
    if '__' in variable or variable[0] == '_' or variable[-1] == '_':
        answer = 'Error!'
    else:
        for c in variable:
            if c.isupper():
                answer = 'Error!'
                is_error = True
                break
        if not is_error:
            temp_str = variable.split('_')
            answer += temp_str[0]
            for word in temp_str[1:]:
                answer += word[0].upper() + word[1:]
    print(answer)
        
else: # Java -> C++
    if variable[0].isupper():
        answer = 'Error!'
    else:
        for c in variable:
            if c.isupper():
                answer += '_' + c.lower()
            else:
                answer += c
    print(answer)