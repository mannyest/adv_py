
import mymod as mm



print('* mymod.REPODIR *')
print(mm.REPODIR)

print(); print()



print('* mymod.SERVER_LIST *')
for item in mm.SERVER_LIST:
    print(item)

print(); print()



print('* calling mymod.addthese *')
mysum = mm.addthese(5, 10)
print(mysum)