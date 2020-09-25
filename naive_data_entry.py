data = []
sum = 0

while True:
    inc_data = [x for x in input("Enter Year, Brand, FN, LN, Number, Price separated by spaces (Type EXIT when finished): ").split()]
    if inc_data[0] != 'EXIT' and len(inc_data) == 6:
        try:
            inc_data[5] = float(inc_data[5])
        except Exception:
            pass
        tpl = tuple(inc_data)
        data.append(tpl)
    else:
        print("You have exited. Here is the data: \n")
        break

for card in data:
    if type(card[5]) is float:
        sum += card[5]

print('Total worth: ', sum)
print('Data: \n\n')
for i in data:
    print(i)

        
    
