
# Runner Metadata Validation

## Description

As a DMSC member, I’d like the creation of Asset Lists that identify the assets
that will be processed through SDVI to be created using more automation.
Currently, the Asset List is created by multiple team members and involves
multiple steps. A more automated process will free up the time required to
create the list manually and ensure that the creation of the list does not
require highly skilled team members.

## Acceptance Criteria
Write an executable python script that takes a Runner report csv, and writes a
new csv with the following changes:

- [ ] Include only assets that match:
  `asset_type_or_class`:
  * archive
  * Audio Stem
  * Dubbed Audio
  * OV Audio
  * package
  * Restored Audio

- [ ] Exclude files that match:
  `folder_names`:
  * Trailer

- [ ] Missing Metadata
  Add a `missing_metadata` column that includes a space-separated list of any of
  the following columns **if they are empty** :

  * `title_gpms_ids`
  * `custom_metadata.content_details.language_dubbed`
  * `custom_metadata.dcs.dcs_vendor`
  * `custom_metadata.format_details.audio_configuration`
  * `custom_metadata.format_details.audio_element`

- [ ] Flag Data Discrepancy (Filename vs. Metadata):
  Parse out audio config code from file name and compare against metadata.
  Add a `metadata_discrepancy` column to and set it to `TRUE` if the code does
  NOT match the metadata value.

  Example:
  `SWAT17_TV_510_LAS_20_V_DXSM_2398_48K_20220131.zip`
  Extracted Code: `20`
  `custom_metadata.format_details.audio_configuration`: `Standard Stereo`

  Audio Configuration Code Mapping
  
  code  | metadata value
  ----- | ------------------
  20    | Standard Stereo
  51    | 5.1 (Discrete)
  50    | 5.0 (Discrete)
  DS    | Lt-Rt (Dolby Surround)
  ATM   | Atmos

