rn = int(input())

dict_49 = {'C': {4:'CD',9:'CM'},
           'X': {4:'XL',9:'XC'},
           'I': {4:'IV',9:'IX'}}

rn_dict = {'M': int((rn-rn%1000)/1000),
           'C': int(((rn-rn%100)/100)%10),
           'X': int(((rn-rn%10)/10)%10),
           'I': rn%10}

for k,v in rn_dict.items():
    if k != 'M' and v in (4,9):
        rn_dict[k] = dict_49.get(k).get(v)
    elif v >= 5:
        rn_dict[k] = {'C':'D', 'X':'L', 'I':'V'}.get(k) + (k*(v%5))
    else:
        rn_dict[k] = k*v
final = ''.join([rn_dict.get(x) for x in ['M','C','X','I']])
print(rn, final)
