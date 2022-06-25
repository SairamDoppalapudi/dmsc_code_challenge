#!/usr/bin/env python3

import argparse
import csv


def main(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8-sig', newline='') as source_io, \
            open(output_file, 'w', encoding='utf-8', newline='') as output_io:
        # read in source file as CSV
        reader = csv.DictReader(source_io)
        # copy fieldnames from reader for writer and add the extra field names
        fieldnames = reader.fieldnames + \
                     ['missing_metadata', 'metadata_discrepancy']
        # Define a dict for the audio codes
        audio_config_codes = {
            'Standard Stereo': '20',
            '5.1 (Discrete)': '51',
            '5.0 (Discrete)': '50',
            'Lt-Rt (Dolby Surround)': 'DS',
            'Atmos': 'ATM'
        }
        # open output file as CSV
        writer = csv.DictWriter(output_io, fieldnames=fieldnames)

        # write the fieldnames
        writer.writeheader()
        # Define a list for included asset types values
        included_asset_types = [
            'archive',
            'Audio Stem',
            'Dubbed Audio',
            'OV Audio',
            'package',
            'Restored Audio'
        ]
        # Define a list for metadata columns
        metadata_tracked_columns = [
            'title_gpms_ids',
            'custom_metadata.content_details.language_dubbed',
            'custom_metadata.dcs.dcs_vendor',
            'custom_metadata.format_details.audio_configuration',
            'custom_metadata.format_details.audio_element'
        ]
        for row in reader:
            if (row['asset_type_or_class'] not in included_asset_types
                    or 'Trailer' in row['folder_names']):
                continue
            output_row = row.copy()
            output_row['missing_metadata'] = ''
            output_row['metadata_discrepancy'] = ''
            for col in metadata_tracked_columns:
                if row[col] == '':
                    output_row['missing_metadata'] += f' {col}'
            output_row['missing_metadata'] = output_row['missing_metadata'].lstrip()
            output_row['metadata_discrepancy'] = 'True' \
                if (row['custom_metadata.format_details.audio_configuration'] == '' \
                    or audio_config_codes[ \
                        row['custom_metadata.format_details.audio_configuration']] != \
                    row['name'].split('_')[4]) else 'False'

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
