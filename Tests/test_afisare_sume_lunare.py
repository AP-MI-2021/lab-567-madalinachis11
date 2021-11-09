from Logic.afisare_sume_lunare import afisare_sume_lunare
from Tests.test_crud import get_data


def test_afisare_sume_lunare():
    cheltuieli = get_data()
    result = afisare_sume_lunare(cheltuieli)
    expected_result = {}
    expected_result[8] = {1: [345]}
    expected_result[9] = {2: [764]}
    expected_result[5] = {3: [99.99]}
    expected_result[2] = {4: [960]}
    expected_result[3] = {5: [425.43]}
    assert result == expected_result

test_afisare_sume_lunare()
