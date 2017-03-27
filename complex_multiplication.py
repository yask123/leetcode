

def complex_mult(a,b):
    a_real, a_imz = map(parse_str_number, a.split('+'))
    b_real, b_imz = map(parse_str_number, b.split('+'))


    result_read, result_imz = map(parse_int_number,  multiply([a_real, a_imz], [b_real, b_imz]))

    return result_read + 'i' + result_imz






def parse_str_number(str_number):
    if str_number[-1] == 'i':
        str_number = str_number[:-1]

    is_positive = True

    if str[0] == '-':
        is_positive = False

        number = int(str_number[1:])
    elif str[0] == '+':
        number = int(str_number[1:])
    else:
        number = int(str_number)

    if is_positive:
        return number
    else:
        return -1 * number


def multiply(a,b):

    real_part = (a[0] * b[0]) + (a[1]*b[1])
    imz_part = (a[0] * b[1]) +  (a[1] * b[0])

    return [real_part, imz_part]