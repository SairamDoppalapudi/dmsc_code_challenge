#!/usr/bin/env python3

import argparse
import csv

def main(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8-sig', newline='') as source_io, \
         open(output_file, 'w', encoding='utf-8', newline='') as output_io:
        # read in source file as CSV
        reader = csv.DictReader(source_io)
        # copy fieldnames from reader for writer
        fieldnames = reader.fieldnames + []

        # open output file as CSV
        writer = csv.DictWriter(output_io, fieldnames=fieldnames)

        # write the fieldnames
        writer.writeheader()

        for row in reader:
            output_row = row.copy()
            # Do Something
            writer.writerow(output_row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'source_file',
        help='Runner inventory CSV report'
    )
    parser.add_argument(
        'output_file',
        help='Filename of the resulting report'
    )
    args = parser.parse_args()
    main(args.source_file, args.output_file)
