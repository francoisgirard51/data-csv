import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # Ignorer l'en-tête (première ligne)
            line_count += 1
        else:
            # Imprimer le nom de famille et le numéro de téléphone
            print(f"{row[1]}: {row[2]}")
            line_count += 1
