"""
Coma Separated Values
Why working with CSV?
To represent large amount of data in txt file
"""

import csv
file = open('b.csv')
file_reader = csv.reader(file)

"""
#converting csv to list data
data = list(file_reader)
print(data)
print(data[0][2])
"""



#row by row traversing using loop from file reade
for row in file_reader:
    print('Row no =', str(file_reader.line_num), str(row))

#Write data on csv
output_file = open('out.csv', 'w', newline='')
output_writer = csv.writer(output_file, delimiter= '.')
output_writer.writerow([1,'Polok', 'Zaman', 19])
output_writer.writerow([2,'Abdus', 'Salam', 20])
output_file.close()

#append

update_file = open('out.csv', 'a', newline='')
file_updater = csv.writer(update_file, delimiter= '.')
file_updater.writerow([3,'Polok', 'Zaman', 19])
file_updater.writerow([4,'Abdus', 'Salam', 20])
output_file.close()





