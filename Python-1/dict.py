dic = {3:'three',1:'one',2:'two',4:'four'}
dic1 = {'three':3,'one':1,'two':2,'four':4}
sdic = dict(sorted(dic.items()))
print(sdic)

sdic2 = dict(sorted(dic1.items(), key=lambda x:x[1]))

print(sdic2)