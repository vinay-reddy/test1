
import re,csv


# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
#
# a = phoneNumRegex.search('this is a string 111-222-3333')
# b= a.groups()
# print(type(a.group(1)))
#
# print(a.group(1))
# print(a.group(2))
# print(a.group(3))
# print(a.group(0))
# print(a.group())
#
# print(b)
#
# print(list(b))

'''

>>> mo.groups()
('415', '555-4242')
>>> areaCode, mainNumber = mo.groups()
>>> print(areaCode)
415
>>> print(mainNumber)
555-4242

>>> phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
>>> mo.group(1)
'(415)'
>>> mo.group(2)
'555-4242'

>>> heroRegex = re.compile (r'Batman|Tina Fey')
>>> mo1 = heroRegex.search('Batman and Tina Fey.')
>>> mo1.group()
'Batman'

>>> mo2 = heroRegex.search('Tina Fey and Batman.')
>>> mo2.group()
'Tina Fey'


>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'


>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'


>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo1 = phoneRegex.search('My number is 415-555-4242')
>>> mo1.group()
'415-555-4242'

>>> mo2 = phoneRegex.search('My number is 555-4242')
>>> mo2.group()
'555-4242'


'''

#creating a regex object

reexob = re.compile(r'load average: ([\d .,]*)')

#print(type(reexob))


# with open('/Users/vinayreddy/Desktop/logs/project_load_plotting/a.log', 'r') as file:
#     for line in file.readlines():
#         a=reexob.search(line)
# #        print(type(a))
#         b=type(a)
#         if type(a) is None:
#             continue
#         else:
#             a.group()


#mo=reexob.search('top - 17:27:01 up 0 min,  0 users,  load average: 1.27, 0.33, 0.11')


with open('/Users/vinayreddy/Desktop/logs/project_load_plotting/a.log', 'r') as file:
    for line in file.read().split('\n'):
#        print(line)
        a = reexob.search(line)
        if a is None:
            continue
        else:
            print(a.group(1))

#print(mo.group(1))





