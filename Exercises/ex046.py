from time import sleep
from emoji import emojize

print("\033[1;31m-=\033[m" * 8)
print(f"\033[1mCONTAGEM REGRESSIVA\033[m")
print("\033[1;31m-=\033[m" * 8)
print()
for sec in range(10, -1, -1):
    print(sec)
    sleep(1)
print(emojize(":boom: :boom: :boom: :boom: :boom:", language='alias'))
