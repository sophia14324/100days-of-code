def triangle(n):
    return recursive_triangle(n, n)

def recursive_triangle(x, n):

    if type(x) != int or type(n) != int:
        return 'error'
    if x > n:
        x = n
    if x == 0 or n == 0:
        return ''
    star_print = n
    line_number = x
    line_print = ''

    difference = star_print - line_number
    if difference != 0:
        line_print += ' '*difference
        line_print += '*'*line_number

    else:
        line_print += '*'*star_print

    if line_number > 1:
        return line_print+'\n'+str(recursive_triangle(line_number-1, star_print))
    elif line_number == 1:
        return line_print