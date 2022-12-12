def reverse(strng):
    if not strng:
        return
    if len(strng)==1:
        return strng
       
    else:
        a = strng[-1]
        strng = list(strng)
        strng = "".join(strng[:-1])

        return  a + reverse(strng)