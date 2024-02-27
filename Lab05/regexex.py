# Exercise 1
import re
txt1 = "abbb"
x = re.search(r"ab*", txt1)
print(x)

# Exercise 2
import re
txt2 = "abbb"
x = re.search(r"ab{2,3}", txt2)
print(x)

# Exercise 3
import re
txt3 = "abcd_"
x = re.search(r"[a-z]+\_", txt3)
print(x)

# Exercise 4
import re
txt4 = "Abcd"
x = re.search(r"[A-Z][a-z]+", txt4)
print(x)

# Exercise 5
import re
txt5 = "adspopsodb"
x = re.search(r"a\w+b", txt5)
print(x)

# Exercise 6
import re
txt6 = "a b c,d,e.f.g"
x = re.sub("[\s\,\.]", ":", txt6)
print(x)

# Exercise 7
import re
txt7 = "abc_def"
comp = txt7.split('_')
camel = comp[0] + ''.join(x.title() for x in comp[1:])
print(camel)


# Exercise 8
import re
txt8 = "AbcDefGhi"
x = re.findall("[A-Z][a-z]*", txt8)
print(x)

# Exercise 9
import re
txt9 = "HelloWorldAndPeople"
x = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt9)
print(x)

# Exercise 10
import re
txt10= "HelloWorldAndPeople"
snake = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt10).lower()
print(snake)
