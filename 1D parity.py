# 1-D parity
def get_parity(value):
    count = 0
    for i in range(len(value)): 
        if value[i] == '1':
            count+=1
        else:
            continue

    if count % 2 == 0:
        print("parity bit is 0")
        return 0 
    
    else:
        print("parity bit is 1")
        return 1  

in_par = input('Enter the parity: ')
parity = get_parity(in_par)
new_par = input('Enter a new parity to check: ') 
new_parity = get_parity(new_par)
if (new_parity == parity):
    print("\nThis is a valid segment")
else:
    print("\nThis is an invalid segment")

    