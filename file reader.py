import re
import csv
file = open('sampledna.fa')

with open('mycords.csv', 'w', newline='') as cf:
    writer = csv.writer(cf)
    writer.writerow(['x-cor','y-cor'])
    with open('sampledna.fa') as f:
        for line in f:
            a,b,c,d,e,f,g,h,i,j = line.split(":")
            writer.writerow([f,g])