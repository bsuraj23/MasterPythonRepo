# from collections import defaultdict



dd = defaultdict(int)  # default value = 0


    print(dd['mango'])  # This will raise KeyError
    print(dd['mango'])  # This will not raise KeyError
dd['apple'] += 1
dd['banana'] += 2   

print(dd)  # {'apple': 1, 'banana': 2}
print(dd['mango'])  # 0 (no KeyError!)


dd_str = defaultdict(str)  # default value = ''
dd_str['name'] += 'John'
print(dd_str)  # {'name': 'John'}
print(dd_str['age'])  # '' (no KeyError!)
dd_list = defaultdict(list)  # default value = []
dd_list['fruits'].append('apple')


