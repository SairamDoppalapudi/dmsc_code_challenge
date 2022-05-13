import csv
import os
import pathlib
import tempfile

import pytest

import dmsc_code_challenge.validate_metadata as described_module

_dir = pathlib.Path(__file__).resolve().parent

def describe_validate_metadata():
    # pylint:disable=unused-variable

    @pytest.fixture()
    def source_file():
        return _dir.joinpath('fixtures', 'example.csv')

    @pytest.fixture()
    def output_file():
        temp = tempfile.mkstemp(suffix='.csv', text=True)[1]
        yield temp
        os.remove(temp)

    @pytest.fixture()
    def parsed_output(output_file):
        with open(output_file, 'r', encoding='utf-8', newline='') as output_io:
            reader = csv.DictReader(output_io)
            return { r['name']:r for r in reader }

    @pytest.fixture(autouse=True)
    def subject(source_file, output_file):
        described_module.main(source_file, output_file)

    @pytest.fixture()
    def non_archive_assets():
        return (
            'NETUMA_108_TV_DEU_Spotters Guide.xlsx',
            'NETUMA_107_TV_DEU_Spotters Guide.xlsx',
            'NETUMA_111_TV_DEU_Script.docx',
            'NETUMA_110_TV_DEU_Script.docx',
            'NETUMA_106_TV_DEU_Spotters Guide.xlsx',
            'NETUMA_109_3_TV_DEU_End Card.tif',
            'NETUMA_109_2_TV_DEU_End Card.tif',
            'NETUMA_109_1_TV_DEU_End Card.tif',
            'NETUMA_111_3_TV_DEU_End Card.tif',
            'NETUMA_112_TV_DEU_Script.docx',
        )

    @pytest.fixture()
    def trailers_assets():
        return (
            'MORBIU_D_R1-6_LAS_51_TH_DXSM_24_48_20220309.sitx',
        )

    def it_removes_assets_with_the_wrong_asset_type(parsed_output, non_archive_assets):
        for name in non_archive_assets:
            assert name not in parsed_output.keys()

    def it_excludes_assets_in_any_folder_with_trailer_in_name(parsed_output, trailers_assets):
        for name in trailers_assets:
            assert name not in parsed_output.keys()

    def it_verifies_audio_config_in_filename_against_metadata(parsed_output):
        assert parsed_output['NETUMA_TV_206_LAS_50_V_DXSM_2398_48K_20220309.zip']\
                .get('metadata_discrepancy') == 'TRUE'

    @pytest.fixture()
    def expected_missing():
        return {
            'NETUMA_TV_110_DEU_DS_V_CM_25_48K_20220303.zip': {
                'custom_metadata.content_details.language_dubbed'
            },
            'NETUMA_TV_109_DEU_51_V_CM_25_48K_20220303.zip': {
                'title_gpms_ids',
                'custom_metadata.dcs.dcs_vendor',
            },
            'MORBIU_D_R1-6_LAS_51_TH_PM_24_48_20220309.sitx': {
                'custom_metadata.format_details.audio_configuration',
                'custom_metadata.format_details.audio_element'
            }
        }

    def it_annotates_missing_metadata(parsed_output, expected_missing):
        for name, expected in expected_missing.items():
            actual = set(parsed_output.get(name, {}).get('missing_metadata', '').split(' '))
            assert actual == expected
