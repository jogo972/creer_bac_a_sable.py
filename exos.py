import os

elements = sorted(os.listdir("/home/jogo/bac-a-sable"))
for e in elements:
    print(e)
print(len(elements))   