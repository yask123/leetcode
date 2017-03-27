'''
0  1  2 3 4

'''
def reverse_string_k(s, k):

    s_list = list(s)
    i = 0

    while i < len(s_list):
        if i + k - 1 <= len(s_list) - 1:
            reverse_substring(s_list, i, i + k - 1)

        i = i + 2*k

    return  ''.join(s_list)

def reverse_substring(s,s_i, e_i):

    i = s_i
    j = e_i

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

s = "ab"

k = 3

print reverse_string_k(s, k)


