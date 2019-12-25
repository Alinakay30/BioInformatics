import re
import csv
file = open('sampledna.fa')

with open('mycords.csv', 'w', newline='') as cf:
    writer = csv.writer(cf)
    writer.writerow(['Name','x-cor','y-cor'])

    with open('sampledna.fa') as f:
        for line in f:
            a,b,c,d,e,f,g,h,i,j = line.split(":")
            instrument = a
            run_number = b
            flowcell_ID = c
            lane = d
            title = e
            x_pos = f
            y_pos = g
            is_filtered = h
            control = i
            index_sequence = j
            writer.writerow([title,x_pos, y_pos])