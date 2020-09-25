import csv

def main():
    filename = "./baseball_card_data.csv"
    header = ("Year", "Brand", "First", "Last", "Number", "Avg Price")

    data = [
        (1991, 'Donruss', 'Tim', 'Teufel', 370, 0.06),
        (1989, 'Donruss', 'Tim', 'Leary', 552, 1.60),
        (1989, 'Donruss', 'Rolando', 'Roomes', 577, 6.25),
        (1989, 'Donruss', 'Darren', 'Daulton', 549, 4.49)
    ]
    writer(header, data, filename, "write")
    updater(filename)

# creation
def writer(header, data, filename, option):
    with open (filename, "w", newline = "") as csvfile:
        if option == "write":
            cards = csv.writer(csvfile)
            cards.writerow(header)
            for x in data:
                cards.writerow(x)
        elif option == "update":
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
            writer.writerows(data)
        else:
            print("Option is not known")

# updating
# needs to be refactored to allow type of update
def updater(filename):
    with open (filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        #print(readData)
        readData[0]['Avg Price'] = '2.00'
    
    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")

main()
