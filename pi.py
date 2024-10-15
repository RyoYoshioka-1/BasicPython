import re

text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

words = text.split()

words = [re.sub(r"[,.]", "", item) for item in words]

words = list(map(len, words))

result = "".join(str(item) for item in words)

print(int(result))
