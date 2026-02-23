a1 = "Hello"
a2 = 'Python'
a3 = """Multi
line
string"""

s = "Python"
print(len(s))   

#indexing 
print(s[0])    # P (first index)
print(s[-1])   # n (last index)

#slicing 
print(s[0:3])   # Pyt
print(s[2:])    # thon
print(s[:4])    # Pyth
print(s[::-1])  # nohtyP (reverse)

#string repetation
print(s * 3)   # PythonPythonPython

#subsrting 
s1 = "Python Programming"

print("Python" in s1)    # True
print("Java" not in s1)  # True

#case conversion 
s2 = "PyThOn"

print(s2.lower())   # python
print(s2.upper())   # PYTHON
print(s2.title())   # Python

#count and find 
s3 = "banana"

print(s3.count("a"))   # 3
print(s3.find("n"))    # 2
