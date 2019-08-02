s = str(input())
romval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
intval = 0
for i in range(len(s)):
    if i > 0 and romval[s[i]] > romval[s[i - 1]]:
        intval += romval[s[i]] - 2 * romval[s[i - 1]]
    else:
        intval += romval[s[i]]
print(intval)
