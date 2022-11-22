from collections import Counter, defaultdict
def buildDFA(pattern):
    m = len(pattern)
    chars = list(set(list(pattern)))
    chars.sort()
    dfa = []
    for _ in range(m):
        d = defaultdict(lambda: 0)
        d.update(d.fromkeys(chars))
        dfa.append(d)
    for char in chars: 
        dfa[0][char] = 0
    dfa[0][pattern[0]] = 1 
    X = 0
    for i in range(1, m):
        #copy mismatch case
        for char in chars:
            dfa[i][char] = dfa[X][char]
        currentChar = pattern[i]
        dfa[i][currentChar] = i + 1 # set match case
        X = dfa[X][currentChar] # update state X
    
    return dfa
def search(dfa, txt, m):
    i, j, n = 0, 0, len(txt)
    for i in range(n):
        j = dfa[j][txt[i]]
        if j == m:
            return i - m + 1
    return False

pattern = 'ABCABCABEABC'
# 'ABCDABCX'
# ABCDABCD # 7 -> 4
# ABCDACCD # 7 -> 4
dfa = buildDFA(pattern)
for line in dfa:
    print(line)
print(search(dfa, "AAMNPABCDACABCABCABCABCCDEBAMNPEQDCMNPEABCABCABEABAAKABAABCDABCXBABCABCKBEABCMNPEABCDABCDQDABCABCABEABCACAA", len(pattern)))
