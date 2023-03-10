#print ('2023/03/10 mip')
userName = input ('Input your name: ')
if userName == 'Mike':
    print('Hi, dear ' + userName)
else:
    print('Hi, stagnger' + userName)

print('So, '+userName+'... let us calculate ... fibanachi und factorials, (from beginen to n)')
n = int(input ('Input number n: '))

strFib = '0, '
intCurrentFib = 0;
intPreviousFib = 1;

strFac = ''
intCurrentFac = 1;
iterator = 1;

separator = ", "

while iterator <= n:
    #Fibanachi
    tempFib = intCurrentFib + intPreviousFib;
    intPreviousFib = intCurrentFib;
    intCurrentFib = tempFib;
    strFib = strFib + str(tempFib)

    #Factirials
    intCurrentFac = intCurrentFac * iterator
    strFac = strFac + str(intCurrentFac)

    if iterator == n:
        separator = ". "

    strFib = strFib + separator
    strFac = strFac + separator  

    iterator = iterator+1

print('\nFibanachi first '+str(n)+' Fibanachi numbers (without 0): ')
print(strFib)

print('\nFactrorials from 1 to '+str(n)+': ')
print(strFac)