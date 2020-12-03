(1) rawstr=input('Enter a number: ')
(2) try:
    ival=int(rawstr)
except:
    ival=-1

if ival>0:
    print('Nice work')
else:
    print('Not a number')
