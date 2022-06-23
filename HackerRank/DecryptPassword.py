def decryptPassword(s):
    # Write your code here
    lenght = len(s)
    res = ""
    digits = []
    index = 0
    while index < lenght:
        ch = s[index]
        if ch.isdigit():
            if ch == '0':
                res += digits.pop()
            else:
                digits.append(ch)
        elif ch != '*':
            if index + 2 < lenght and s[index].isupper() and s[index + 1].islower() and s[index + 2] == '*':
                res += s[index + 1] + s[index]
                index += 2
            else:
                res += ch
        index += 1                       
    return res