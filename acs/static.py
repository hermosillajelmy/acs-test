NULL_LIST = [-555555555, -999999999, -222222222, -666666666, -333333333]

LIST_STATE = ['28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '44', '45', '46', '47',
              '48', '50', '49', '51', '53', '54', '55', '56', '72', '01', '02', '04', '05', '06', '08', '10', '11', '09', '12', 
              '13', '16', '15', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']

FIPS_CODE = {
    'us': '01000US',
    'state': '04000US',
    'county': '05000US',
    'place': '16000US',
    'public use microdata area': '79500US',
    'msa': '31000US',
    'tract': '14000US',
    'congressional district': '50000US',
    'zip code tabulation area': '86000US'
}

DICT_APIS = {
    'acs_yg_gini': ['https://api.census.gov/data/{}/acs/acs{}?get=B19083_001E,B19083_001M&for={}&key={}', 
                    'https://api.census.gov/data/{}/acs/acs{}?get=B19083_001E,B19083_001M&for={}&key={}&in=state:{}'],
    'acs_health_coverage_s': ['https://api.census.gov/data/{}/acs/acs{}/subject?get=S2703_C02_003E,S2703_C02_004E,S2703_C02_005E,S2703_C02_007E,S2703_C02_008E,S2703_C02_009E,S2703_C02_011E,S2703_C02_012E,S2703_C02_013E,S2704_C02_003E,S2704_C02_004E,S2704_C02_005E,S2704_C02_007E,S2704_C02_008E,S2704_C02_009E,S2704_C02_011E,S2704_C02_012E,S2704_C02_013E,S2701_C04_011E,S2701_C04_012E,S2701_C04_013E,S2703_C01_003E,S2703_C01_004E,S2703_C01_005E,S2703_C01_001E,S2703_C02_003M,S2703_C02_004M,S2703_C02_005M,S2703_C02_007M,S2703_C02_008M,S2703_C02_009M,S2703_C02_011M,S2703_C02_012M,S2703_C02_013M,S2704_C02_003M,S2704_C02_004M,S2704_C02_005M,S2704_C02_007M,S2704_C02_008M,S2704_C02_009M,S2704_C02_011M,S2704_C02_012M,S2704_C02_013M,S2701_C04_011M,S2701_C04_012M,S2701_C04_013M,S2703_C01_003M,S2703_C01_004M,S2703_C01_005M,S2703_C01_001M&for={}&key={}', 
                              'https://api.census.gov/data/{}/acs/acs{}/subject?get=S2703_C02_003E,S2703_C02_004E,S2703_C02_005E,S2703_C02_007E,S2703_C02_008E,S2703_C02_009E,S2703_C02_011E,S2703_C02_012E,S2703_C02_013E,S2704_C02_003E,S2704_C02_004E,S2704_C02_005E,S2704_C02_007E,S2704_C02_008E,S2704_C02_009E,S2704_C02_011E,S2704_C02_012E,S2704_C02_013E,S2701_C04_011E,S2701_C04_012E,S2701_C04_013E,S2703_C01_003E,S2703_C01_004E,S2703_C01_005E,S2703_C01_001E,S2703_C02_003M,S2703_C02_004M,S2703_C02_005M,S2703_C02_007M,S2703_C02_008M,S2703_C02_009M,S2703_C02_011M,S2703_C02_012M,S2703_C02_013M,S2704_C02_003M,S2704_C02_004M,S2704_C02_005M,S2704_C02_007M,S2704_C02_008M,S2704_C02_009M,S2704_C02_011M,S2704_C02_012M,S2704_C02_013M,S2701_C04_011M,S2701_C04_012M,S2701_C04_013M,S2703_C01_003M,S2703_C01_004M,S2703_C01_005M,S2703_C01_001M&for={}&key={}&in=state:{}'],
    'acs_yg_household_income': ['https://api.census.gov/data/{}/acs/acs{}?get=B19001_002E,B19001_003E,B19001_004E,B19001_005E,B19001_006E,B19001_007E,B19001_008E,B19001_009E,B19001_010E,B19001_011E,B19001_012E,B19001_013E,B19001_014E,B19001_015E,B19001_016E,B19001_017E,B19001_002M,B19001_003M,B19001_004M,B19001_005M,B19001_006M,B19001_007M,B19001_008M,B19001_009M,B19001_010M,B19001_011M,B19001_012M,B19001_013M,B19001_014M,B19001_015M,B19001_016M,B19001_017M&for={}&key={}', 
                                'https://api.census.gov/data/{}/acs/acs{}?get=B19001_002E,B19001_003E,B19001_004E,B19001_005E,B19001_006E,B19001_007E,B19001_008E,B19001_009E,B19001_010E,B19001_011E,B19001_012E,B19001_013E,B19001_014E,B19001_015E,B19001_016E,B19001_017E,B19001_002M,B19001_003M,B19001_004M,B19001_005M,B19001_006M,B19001_007M,B19001_008M,B19001_009M,B19001_010M,B19001_011M,B19001_012M,B19001_013M,B19001_014M,B19001_015M,B19001_016M,B19001_017M&for={}&key={}&in=state:{}'],
    'acs_yg_housing_median_value': ['https://api.census.gov/data/{}/acs/acs{}?get=B25077_001E,B25077_001M&for={}&key={}', 
                                    'https://api.census.gov/data/{}/acs/acs{}?get=B25077_001E,B25077_001M&for={}&key={}&in=state:{}'],
    'acs_yg_total_population': ['https://api.census.gov/data/{}/acs/acs{}?get=B01003_001E,B01003_001M&for={}&key={}', 
                                'https://api.census.gov/data/{}/acs/acs{}?get=B01003_001E,B01003_001M&for={}&key={}&in=state:{}'],
    'acs_ygc_citizenship_status': ['https://api.census.gov/data/{}/acs/acs{}?get=B05001_002E,B05001_003E,B05001_004E,B05001_005E,B05001_006E,B05001_002M,B05001_003M,B05001_004M,B05001_005M,B05001_006M&for={}&key={}', 
                                   'https://api.census.gov/data/{}/acs/acs{}?get=B05001_002E,B05001_003E,B05001_004E,B05001_005E,B05001_006E,B05001_002M,B05001_003M,B05001_004M,B05001_005M,B05001_006M&for={}&key={}&in=state:{}'],
    'acs_ygcs_median_age_by_citizenship_status_by_gender': ['https://api.census.gov/data/{}/acs/acs{}?get=B05004_001E,B05004_002E,B05004_003E,B05004_004E,B05004_005E,B05004_006E,B05004_007E,B05004_008E,B05004_009E,B05004_010E,B05004_011E,B05004_012E,B05004_014E,B05004_015E,B05004_001M,B05004_002M,B05004_003M,B05004_004M,B05004_005M,B05004_006M,B05004_007M,B05004_008M,B05004_009M,B05004_010M,B05004_011M,B05004_012M,B05004_014M,B05004_015M&for={}&key={}', 
                                                           'https://api.census.gov/data/{}/acs/acs{}?get=B05004_001E,B05004_002E,B05004_003E,B05004_004E,B05004_005E,B05004_006E,B05004_007E,B05004_008E,B05004_009E,B05004_010E,B05004_011E,B05004_012E,B05004_014E,B05004_015E,B05004_001M,B05004_002M,B05004_003M,B05004_004M,B05004_005M,B05004_006M,B05004_007M,B05004_008M,B05004_009M,B05004_010M,B05004_011M,B05004_012M,B05004_014M,B05004_015M&for={}&key={}&in=state:{}'],
    'acs_ygs_median_age_total': ['https://api.census.gov/data/{}/acs/acs{}?get=B01002_001E,B01002_002E,B01002_003E,B01002_001M,B01002_002M,B01002_003M&for={}&key={}', 
                                 'https://api.census.gov/data/{}/acs/acs{}?get=B01002_001E,B01002_002E,B01002_003E,B01002_001M,B01002_002M,B01002_003M&for={}&key={}&in=state:{}'],
    'acs_ygs_aggregate_travel_time_to_work': ['https://api.census.gov/data/{}/acs/acs{}?get=B08013_002E,B08013_003E,B08013_002M,B08013_003M&for={}&key={}', 
                                              'https://api.census.gov/data/{}/acs/acs{}?get=B08013_002E,B08013_003E,B08013_002M,B08013_003M&for={}&key={}&in=state:{}'],
    'acs_ygr_race_with_hispanic': ['https://api.census.gov/data/{}/acs/acs{}?get=B03002_003E,B03002_004E,B03002_005E,B03002_006E,B03002_007E,B03002_008E,B03002_010E,B03002_011E,B03002_013E,B03002_014E,B03002_015E,B03002_016E,B03002_017E,B03002_018E,B03002_020E,B03002_021E,B03002_003M,B03002_004M,B03002_005M,B03002_006M,B03002_007M,B03002_008M,B03002_010M,B03002_011M,B03002_013M,B03002_014M,B03002_015M,B03002_016M,B03002_017M,B03002_018M,B03002_020M,B03002_021M&for={}&key={}', 
                                   'https://api.census.gov/data/{}/acs/acs{}?get=B03002_003E,B03002_004E,B03002_005E,B03002_006E,B03002_007E,B03002_008E,B03002_010E,B03002_011E,B03002_013E,B03002_014E,B03002_015E,B03002_016E,B03002_017E,B03002_018E,B03002_020E,B03002_021E,B03002_003M,B03002_004M,B03002_005M,B03002_006M,B03002_007M,B03002_008M,B03002_010M,B03002_011M,B03002_013M,B03002_014M,B03002_015M,B03002_016M,B03002_017M,B03002_018M,B03002_020M,B03002_021M&for={}&key={}&in=state:{}'],
    'acs_ygo_tenure': ['https://api.census.gov/data/{}/acs/acs{}?get=B25003_002E,B25003_003E,B25003_002M,B25003_003M&for={}&key={}', 
                       'https://api.census.gov/data/{}/acs/acs{}?get=B25003_002E,B25003_003E,B25003_002M,B25003_003M&for={}&key={}&in=state:{}'],
    'acs_ygmt_mortgage_status_by_real_estate_taxes': ['https://api.census.gov/data/{}/acs/acs{}?get=B25102_003E,B25102_004E,B25102_005E,B25102_006E,B25102_007E,B25102_008E,B25102_010E,B25102_011E,B25102_012E,B25102_013E,B25102_014E,B25102_015E,B25102_003M,B25102_004M,B25102_005M,B25102_006M,B25102_007M,B25102_008M,B25102_010M,B25102_011M,B25102_012M,B25102_013M,B25102_014M,B25102_015M&for={}&key={}', 
                                                      'https://api.census.gov/data/{}/acs/acs{}?get=B25102_003E,B25102_004E,B25102_005E,B25102_006E,B25102_007E,B25102_008E,B25102_010E,B25102_011E,B25102_012E,B25102_013E,B25102_014E,B25102_015E,B25102_003M,B25102_004M,B25102_005M,B25102_006M,B25102_007M,B25102_008M,B25102_010M,B25102_011M,B25102_012M,B25102_013M,B25102_014M,B25102_015M&for={}&key={}&in=state:{}'],
    'acs_ygh_occupied_households_lacking_plumbing': ['https://api.census.gov/data/{}/acs/acs{}?get=B25048_002E,B25048_003E,B25048_002M,B25048_003M&for={}&key={}', 
                                                     'https://api.census.gov/data/{}/acs/acs{}?get=B25048_002E,B25048_003E,B25048_002M,B25048_003M&for={}&key={}&in=state:{}'],
    'acs_ygh_occupied_households_lacking_kitchen': ['https://api.census.gov/data/{}/acs/acs{}?get=B25052_002E,B25052_003E,B25052_002M,B25052_003M&for={}&key={}', 
                                                    'https://api.census.gov/data/{}/acs/acs{}?get=B25052_002E,B25052_003E,B25052_002M,B25052_003M&for={}&key={}&in=state:{}'],
    'acs_ygh_households_with_no_internet_2016': ['https://api.census.gov/data/{}/acs/acs{}?get=B28002_002E,B28002_012E,B28002_013E,B28002_002M,B28002_012M,B28002_013M&for={}&key={}', 
                                                 'https://api.census.gov/data/{}/acs/acs{}?get=B28002_002E,B28002_012E,B28002_013E,B28002_002M,B28002_012M,B28002_013M&for={}&key={}&in=state:{}'],
    'acs_ygh_homeowners_with_mortgage_spending_30_percent_on_costs': ['https://api.census.gov/data/{}/acs/acs{}?get=B25092_002E,B25092_003E,B25092_002M,B25092_003M&for={}&key={}', 
                                                                      'https://api.census.gov/data/{}/acs/acs{}?get=B25092_002E,B25092_003E,B25092_002M,B25092_003M&for={}&key={}&in=state:{}'],
    'acs_ygv_veterans': ['https://api.census.gov/data/{}/acs/acs{}?get=B21002_002E,B21002_003E,B21002_004E,B21002_005E,B21002_006E,B21002_007E,B21002_008E,B21002_009E,B21002_010E,B21002_011E,B21002_012E,B21002_013E,B21002_014E,B21002_015E,B21002_016E,B21002_002M,B21002_003M,B21002_004M,B21002_005M,B21002_006M,B21002_007M,B21002_008M,B21002_009M,B21002_010M,B21002_011M,B21002_012M,B21002_013M,B21002_014M,B21002_015M,B21002_016M&for={}&key={}', 
                         'https://api.census.gov/data/{}/acs/acs{}?get=B21002_002E,B21002_003E,B21002_004E,B21002_005E,B21002_006E,B21002_007E,B21002_008E,B21002_009E,B21002_010E,B21002_011E,B21002_012E,B21002_013E,B21002_014E,B21002_015E,B21002_016E,B21002_002M,B21002_003M,B21002_004M,B21002_005M,B21002_006M,B21002_007M,B21002_008M,B21002_009M,B21002_010M,B21002_011M,B21002_012M,B21002_013M,B21002_014M,B21002_015M,B21002_016M&for={}&key={}&in=state:{}'],
    'acs_ygt_travel_time_to_work': ['https://api.census.gov/data/{}/acs/acs{}?get=B08303_002E,B08303_003E,B08303_004E,B08303_005E,B08303_006E,B08303_007E,B08303_008E,B08303_009E,B08303_010E,B08303_011E,B08303_012E,B08303_013E,B08303_002M,B08303_003M,B08303_004M,B08303_005M,B08303_006M,B08303_007M,B08303_008M,B08303_009M,B08303_010M,B08303_011M,B08303_012M,B08303_013M&for={}&key={}', 
                                    'https://api.census.gov/data/{}/acs/acs{}?get=B08303_002E,B08303_003E,B08303_004E,B08303_005E,B08303_006E,B08303_007E,B08303_008E,B08303_009E,B08303_010E,B08303_011E,B08303_012E,B08303_013E,B08303_002M,B08303_003M,B08303_004M,B08303_005M,B08303_006M,B08303_007M,B08303_008M,B08303_009M,B08303_010M,B08303_011M,B08303_012M,B08303_013M&for={}&key={}&in=state:{}'],
    'acs_ygt_means_of_transportation_to_work': ['https://api.census.gov/data/{}/acs/acs{}?get=B08301_003E,B08301_005E,B08301_006E,B08301_007E,B08301_008E,B08301_009E,B08301_011E,B08301_012E,B08301_013E,B08301_014E,B08301_015E,B08301_016E,B08301_017E,B08301_018E,B08301_019E,B08301_020E,B08301_021E,B08301_003M,B08301_005M,B08301_006M,B08301_007M,B08301_008M,B08301_009M,B08301_011M,B08301_012M,B08301_013M,B08301_014M,B08301_015M,B08301_016M,B08301_017M,B08301_018M,B08301_019M,B08301_020M,B08301_021M&for={}&key={}', 
                                                'https://api.census.gov/data/{}/acs/acs{}?get=B08301_003E,B08301_005E,B08301_006E,B08301_007E,B08301_008E,B08301_009E,B08301_011E,B08301_012E,B08301_013E,B08301_014E,B08301_015E,B08301_016E,B08301_017E,B08301_018E,B08301_019E,B08301_020E,B08301_021E,B08301_003M,B08301_005M,B08301_006M,B08301_007M,B08301_008M,B08301_009M,B08301_011M,B08301_012M,B08301_013M,B08301_014M,B08301_015M,B08301_016M,B08301_017M,B08301_018M,B08301_019M,B08301_020M,B08301_021M&for={}&key={}&in=state:{}'],
    'acs_ygt_aggregate_travel_time_to_work_by_transportation': ['https://api.census.gov/data/{}/acs/acs{}?get=B08136_003E,B08136_005E,B08136_006E,B08136_008E,B08136_009E,B08136_010E,B08136_011E,B08136_012E,B08136_003M,B08136_005M,B08136_006M,B08136_008M,B08136_009M,B08136_010M,B08136_011M,B08136_012M&for={}&key={}', 
                                                                'https://api.census.gov/data/{}/acs/acs{}?get=B08136_003E,B08136_005E,B08136_006E,B08136_008E,B08136_009E,B08136_010E,B08136_011E,B08136_012E,B08136_003M,B08136_005M,B08136_006M,B08136_008M,B08136_009M,B08136_010M,B08136_011M,B08136_012M&for={}&key={}&in=state:{}'],
    'acs_ygsv_gender_of_workers_by_vehicles_available': ['https://api.census.gov/data/{}/acs/acs{}?get=B08014_009E,B08014_010E,B08014_011E,B08014_012E,B08014_013E,B08014_014E,B08014_016E,B08014_017E,B08014_018E,B08014_019E,B08014_020E,B08014_021E,B08014_009M,B08014_010M,B08014_011M,B08014_012M,B08014_013M,B08014_014M,B08014_016M,B08014_017M,B08014_018M,B08014_019M,B08014_020M,B08014_021M&for={}&key={}', 
                                                         'https://api.census.gov/data/{}/acs/acs{}?get=B08014_009E,B08014_010E,B08014_011E,B08014_012E,B08014_013E,B08014_014E,B08014_016E,B08014_017E,B08014_018E,B08014_019E,B08014_020E,B08014_021E,B08014_009M,B08014_010M,B08014_011M,B08014_012M,B08014_013M,B08014_014M,B08014_016M,B08014_017M,B08014_018M,B08014_019M,B08014_020M,B08014_021M&for={}&key={}&in=state:{}'],
    'acs_ygf_place_of_birth_for_foreing_born_1': ['https://api.census.gov/data/{}/acs/acs{}?get=B05006_005E,B05006_006E,B05006_007E,B05006_008E,B05006_009E,B05006_010E,B05006_011E,B05006_012E,B05006_014E,B05006_015E,B05006_016E,B05006_017E,B05006_018E,B05006_019E,B05006_020E,B05006_022E,B05006_023E,B05006_024E,B05006_025E,B05006_026E,B05006_027E,B05006_029E,B05006_030E,B05006_031E,B05006_032E,B05006_033E,B05006_034E,B05006_035E,B05006_036E,B05006_037E,B05006_038E,B05006_039E,B05006_040E,B05006_041E,B05006_042E,B05006_043E,B05006_044E,B05006_045E,B05006_046E,B05006_050E,B05006_051E,B05006_052E,B05006_053E,B05006_054E,B05006_055E,B05006_057E,B05006_058E,B05006_059E,B05006_060E,B05006_061E&for={}&key={}', 
                                                  'https://api.census.gov/data/{}/acs/acs{}?get=B05006_005E,B05006_006E,B05006_007E,B05006_008E,B05006_009E,B05006_010E,B05006_011E,B05006_012E,B05006_014E,B05006_015E,B05006_016E,B05006_017E,B05006_018E,B05006_019E,B05006_020E,B05006_022E,B05006_023E,B05006_024E,B05006_025E,B05006_026E,B05006_027E,B05006_029E,B05006_030E,B05006_031E,B05006_032E,B05006_033E,B05006_034E,B05006_035E,B05006_036E,B05006_037E,B05006_038E,B05006_039E,B05006_040E,B05006_041E,B05006_042E,B05006_043E,B05006_044E,B05006_045E,B05006_046E,B05006_050E,B05006_051E,B05006_052E,B05006_053E,B05006_054E,B05006_055E,B05006_057E,B05006_058E,B05006_059E,B05006_060E,B05006_061E&for={}&key={}&in=state:{}'],
    'acs_ygf_place_of_birth_for_foreing_born_2': ['https://api.census.gov/data/{}/acs/acs{}?get=B05006_062E,B05006_063E,B05006_064E,B05006_065E,B05006_066E,B05006_068E,B05006_069E,B05006_070E,B05006_071E,B05006_072E,B05006_073E,B05006_074E,B05006_075E,B05006_076E,B05006_077E,B05006_079E,B05006_080E,B05006_081E,B05006_082E,B05006_083E,B05006_084E,B05006_085E,B05006_086E,B05006_087E,B05006_088E,B05006_089E,B05006_090E,B05006_093E,B05006_094E,B05006_095E,B05006_096E,B05006_097E,B05006_099E,B05006_100E,B05006_102E,B05006_103E,B05006_104E,B05006_105E,B05006_107E,B05006_108E,B05006_110E,B05006_111E,B05006_112E,B05006_113E,B05006_114E,B05006_115E,B05006_116E,B05006_119E,B05006_120E,B05006_121E&for={}&key={}', 
                                                  'https://api.census.gov/data/{}/acs/acs{}?get=B05006_062E,B05006_063E,B05006_064E,B05006_065E,B05006_066E,B05006_068E,B05006_069E,B05006_070E,B05006_071E,B05006_072E,B05006_073E,B05006_074E,B05006_075E,B05006_076E,B05006_077E,B05006_079E,B05006_080E,B05006_081E,B05006_082E,B05006_083E,B05006_084E,B05006_085E,B05006_086E,B05006_087E,B05006_088E,B05006_089E,B05006_090E,B05006_093E,B05006_094E,B05006_095E,B05006_096E,B05006_097E,B05006_099E,B05006_100E,B05006_102E,B05006_103E,B05006_104E,B05006_105E,B05006_107E,B05006_108E,B05006_110E,B05006_111E,B05006_112E,B05006_113E,B05006_114E,B05006_115E,B05006_116E,B05006_119E,B05006_120E,B05006_121E&for={}&key={}&in=state:{}'],
    'acs_ygf_place_of_birth_for_foreing_born_3': ['https://api.census.gov/data/{}/acs/acs{}?get=B05006_122E,B05006_126E,B05006_127E,B05006_128E,B05006_129E,B05006_130E,B05006_131E,B05006_132E,B05006_133E,B05006_134E,B05006_135E,B05006_136E,B05006_137E,B05006_139E,B05006_140E,B05006_141E,B05006_142E,B05006_143E,B05006_144E,B05006_145E,B05006_146E,B05006_147E,B05006_149E,B05006_150E,B05006_151E,B05006_152E,B05006_153E,B05006_154E,B05006_155E,B05006_156E,B05006_157E,B05006_158E,B05006_159E,B05006_161E,B05006_162E,B05006_005M,B05006_006M,B05006_007M,B05006_008M,B05006_009M,B05006_010M,B05006_011M,B05006_012M,B05006_014M,B05006_015M,B05006_016M,B05006_017M,B05006_018M,B05006_019M,B05006_020M&for={}&key={}', 
                                                  'https://api.census.gov/data/{}/acs/acs{}?get=B05006_122E,B05006_126E,B05006_127E,B05006_128E,B05006_129E,B05006_130E,B05006_131E,B05006_132E,B05006_133E,B05006_134E,B05006_135E,B05006_136E,B05006_137E,B05006_139E,B05006_140E,B05006_141E,B05006_142E,B05006_143E,B05006_144E,B05006_145E,B05006_146E,B05006_147E,B05006_149E,B05006_150E,B05006_151E,B05006_152E,B05006_153E,B05006_154E,B05006_155E,B05006_156E,B05006_157E,B05006_158E,B05006_159E,B05006_161E,B05006_162E,B05006_005M,B05006_006M,B05006_007M,B05006_008M,B05006_009M,B05006_010M,B05006_011M,B05006_012M,B05006_014M,B05006_015M,B05006_016M,B05006_017M,B05006_018M,B05006_019M,B05006_020M&for={}&key={}&in=state:{}'],
    'acs_ygf_place_of_birth_for_foreing_born_4': ['https://api.census.gov/data/{}/acs/acs{}?get=B05006_022M,B05006_023M,B05006_024M,B05006_025M,B05006_026M,B05006_027M,B05006_029M,B05006_030M,B05006_031M,B05006_032M,B05006_033M,B05006_034M,B05006_035M,B05006_036M,B05006_037M,B05006_038M,B05006_039M,B05006_040M,B05006_041M,B05006_042M,B05006_043M,B05006_044M,B05006_045M,B05006_046M,B05006_050M,B05006_051M,B05006_052M,B05006_053M,B05006_054M,B05006_055M,B05006_057M,B05006_058M,B05006_059M,B05006_060M,B05006_061M,B05006_062M,B05006_063M,B05006_064M,B05006_065M,B05006_066M,B05006_068M,B05006_069M,B05006_070M,B05006_071M,B05006_072M,B05006_073M,B05006_074M,B05006_075M,B05006_076M,B05006_077M&for={}&key={}', 
                                                  'https://api.census.gov/data/{}/acs/acs{}?get=B05006_022M,B05006_023M,B05006_024M,B05006_025M,B05006_026M,B05006_027M,B05006_029M,B05006_030M,B05006_031M,B05006_032M,B05006_033M,B05006_034M,B05006_035M,B05006_036M,B05006_037M,B05006_038M,B05006_039M,B05006_040M,B05006_041M,B05006_042M,B05006_043M,B05006_044M,B05006_045M,B05006_046M,B05006_050M,B05006_051M,B05006_052M,B05006_053M,B05006_054M,B05006_055M,B05006_057M,B05006_058M,B05006_059M,B05006_060M,B05006_061M,B05006_062M,B05006_063M,B05006_064M,B05006_065M,B05006_066M,B05006_068M,B05006_069M,B05006_070M,B05006_071M,B05006_072M,B05006_073M,B05006_074M,B05006_075M,B05006_076M,B05006_077M&for={}&key={}&in=state:{}'],
    'acs_ygf_place_of_birth_for_foreing_born_5': ['https://api.census.gov/data/{}/acs/acs{}?get=B05006_079M,B05006_080M,B05006_081M,B05006_082M,B05006_083M,B05006_084M,B05006_085M,B05006_086M,B05006_087M,B05006_088M,B05006_089M,B05006_090M,B05006_093M,B05006_094M,B05006_095M,B05006_096M,B05006_097M,B05006_099M,B05006_100M,B05006_102M,B05006_103M,B05006_104M,B05006_105M,B05006_107M,B05006_108M,B05006_110M,B05006_111M,B05006_112M,B05006_113M,B05006_114M,B05006_115M,B05006_116M,B05006_119M,B05006_120M,B05006_121M,B05006_122M,B05006_126M,B05006_127M,B05006_128M,B05006_129M,B05006_130M,B05006_131M,B05006_132M,B05006_133M,B05006_134M,B05006_135M,B05006_136M,B05006_137M,B05006_139M,B05006_140M&for={}&key={}', 
                                                  'https://api.census.gov/data/{}/acs/acs{}?get=B05006_079M,B05006_080M,B05006_081M,B05006_082M,B05006_083M,B05006_084M,B05006_085M,B05006_086M,B05006_087M,B05006_088M,B05006_089M,B05006_090M,B05006_093M,B05006_094M,B05006_095M,B05006_096M,B05006_097M,B05006_099M,B05006_100M,B05006_102M,B05006_103M,B05006_104M,B05006_105M,B05006_107M,B05006_108M,B05006_110M,B05006_111M,B05006_112M,B05006_113M,B05006_114M,B05006_115M,B05006_116M,B05006_119M,B05006_120M,B05006_121M,B05006_122M,B05006_126M,B05006_127M,B05006_128M,B05006_129M,B05006_130M,B05006_131M,B05006_132M,B05006_133M,B05006_134M,B05006_135M,B05006_136M,B05006_137M,B05006_139M,B05006_140M&for={}&key={}&in=state:{}'],
    'acs_ygf_place_of_birth_for_foreing_born_6': ['https://api.census.gov/data/{}/acs/acs{}?get=B05006_141M,B05006_142M,B05006_143M,B05006_144M,B05006_145M,B05006_146M,B05006_147M,B05006_149M,B05006_150M,B05006_151M,B05006_152M,B05006_153M,B05006_154M,B05006_155M,B05006_156M,B05006_157M,B05006_158M,B05006_159M,B05006_161M,B05006_162M&for={}&key={}', 
                                                  'https://api.census.gov/data/{}/acs/acs{}?get=B05006_141M,B05006_142M,B05006_143M,B05006_144M,B05006_145M,B05006_146M,B05006_147M,B05006_149M,B05006_150M,B05006_151M,B05006_152M,B05006_153M,B05006_154M,B05006_155M,B05006_156M,B05006_157M,B05006_158M,B05006_159M,B05006_161M,B05006_162M&for={}&key={}&in=state:{}'],
    'acs_ygh_health_care_coverage_overall_1': ['https://api.census.gov/data/{}/acs/acs{}?get=B27010_004E,B27010_005E,B27010_006E,B27010_007E,B27010_008E,B27010_009E,B27010_011E,B27010_012E,B27010_013E,B27010_014E,B27010_015E,B27010_016E,B27010_017E,B27010_020E,B27010_021E,B27010_022E,B27010_023E,B27010_024E,B27010_025E,B27010_027E,B27010_028E,B27010_029E,B27010_030E,B27010_031E,B27010_032E,B27010_033E,B27010_036E,B27010_037E,B27010_038E,B27010_039E,B27010_040E,B27010_041E,B27010_043E,B27010_044E,B27010_045E,B27010_046E,B27010_047E,B27010_048E,B27010_049E,B27010_050E,B27010_053E,B27010_054E,B27010_055E,B27010_056E,B27010_057E,B27010_059E,B27010_060E,B27010_061E,B27010_062E,B27010_063E&for={}&key={}', 
                                               'https://api.census.gov/data/{}/acs/acs{}?get=B27010_004E,B27010_005E,B27010_006E,B27010_007E,B27010_008E,B27010_009E,B27010_011E,B27010_012E,B27010_013E,B27010_014E,B27010_015E,B27010_016E,B27010_017E,B27010_020E,B27010_021E,B27010_022E,B27010_023E,B27010_024E,B27010_025E,B27010_027E,B27010_028E,B27010_029E,B27010_030E,B27010_031E,B27010_032E,B27010_033E,B27010_036E,B27010_037E,B27010_038E,B27010_039E,B27010_040E,B27010_041E,B27010_043E,B27010_044E,B27010_045E,B27010_046E,B27010_047E,B27010_048E,B27010_049E,B27010_050E,B27010_053E,B27010_054E,B27010_055E,B27010_056E,B27010_057E,B27010_059E,B27010_060E,B27010_061E,B27010_062E,B27010_063E&for={}&key={}&in=state:{}'],
    'acs_ygh_health_care_coverage_overall_2': ['https://api.census.gov/data/{}/acs/acs{}?get=B27010_064E,B27010_065E,B27010_066E,B27010_004M,B27010_005M,B27010_006M,B27010_007M,B27010_008M,B27010_009M,B27010_011M,B27010_012M,B27010_013M,B27010_014M,B27010_015M,B27010_016M,B27010_017M,B27010_020M,B27010_021M,B27010_022M,B27010_023M,B27010_024M,B27010_025M,B27010_027M,B27010_028M,B27010_029M,B27010_030M,B27010_031M,B27010_032M,B27010_033M,B27010_036M,B27010_037M,B27010_038M,B27010_039M,B27010_040M,B27010_041M,B27010_043M,B27010_044M,B27010_045M,B27010_046M,B27010_047M,B27010_048M,B27010_049M,B27010_050M,B27010_053M,B27010_054M,B27010_055M,B27010_056M,B27010_057M,B27010_059M,B27010_060M&for={}&key={}', 
                                               'https://api.census.gov/data/{}/acs/acs{}?get=B27010_064E,B27010_065E,B27010_066E,B27010_004M,B27010_005M,B27010_006M,B27010_007M,B27010_008M,B27010_009M,B27010_011M,B27010_012M,B27010_013M,B27010_014M,B27010_015M,B27010_016M,B27010_017M,B27010_020M,B27010_021M,B27010_022M,B27010_023M,B27010_024M,B27010_025M,B27010_027M,B27010_028M,B27010_029M,B27010_030M,B27010_031M,B27010_032M,B27010_033M,B27010_036M,B27010_037M,B27010_038M,B27010_039M,B27010_040M,B27010_041M,B27010_043M,B27010_044M,B27010_045M,B27010_046M,B27010_047M,B27010_048M,B27010_049M,B27010_050M,B27010_053M,B27010_054M,B27010_055M,B27010_056M,B27010_057M,B27010_059M,B27010_060M&for={}&key={}&in=state:{}'],
    'acs_ygh_health_care_coverage_overall_3': ['https://api.census.gov/data/{}/acs/acs{}?get=B27010_061M,B27010_062M,B27010_063M,B27010_064M,B27010_065M,B27010_066M&for={}&key={}', 
                                               'https://api.census.gov/data/{}/acs/acs{}?get=B27010_061M,B27010_062M,B27010_063M,B27010_064M,B27010_065M,B27010_066M&for={}&key={}&in=state:{}'],
}