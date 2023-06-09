
strings = ["sun", "bed", "car"]
n = 1
print(sorted(sorted(strings), key=lambda x:x[n]))

strings = ["sun", "bed", "car"]
strings.sort()
print(sorted(strings, key=lambda x:x[n]))