string1 = "Becomes"
string1 = string1.lower()
print(string1.startswith("be"))

string2 = "becomes"
print(string2.startswith("be"))
#string2 unchanged

string3 = "BEAR"
string3 = string3.lower()
print(string3.startswith("be"))

string4 = "    bEautiful"
string4 = string4.lower().lstrip()
print(string4.startswith("be"))
