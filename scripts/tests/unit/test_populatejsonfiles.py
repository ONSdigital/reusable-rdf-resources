import pytest
import json

from urllib.error import HTTPError

from scripts.populatejsonfiles import get, update_json

@pytest.mark.vcr
def test_get_unit_url_successfully_retrieved():
    """
    test response from url request is ok
    """
    unit_url = 'http://qudt.org/2.1/vocab/unit'
    r = get(unit_url)
    assert r is r.ok

@pytest.mark.vcr
def test_get_quantity_kind_url_successfully_retrieved():
    """
    test response from url request is ok
    """
    quantity_kind_url = 'http://qudt.org/2.1/vocab/quantitykind'
    r = get(quantity_kind_url)
    assert r is r.ok

@pytest.mark.vcr
def test_get_raises_error():
    """
    test get for expected HTTP error
    """
    url = 'http://this_doesnt_exist'
    r = get(url)
    assert r is not r.ok
    assert r is type(HTTPError)
    assert r == (f'Could not get "{url}" with status code {r.status_code}')

@pytest.mark.vcr
def test_update_json():
    """
    test update json does not add duplicates
    """
    json_path = '/workspaces/reusable-rdf-resources/quantity-kinds.json'
    url_list = ("http://qudt.org/vocab/quantitykind/AbsoluteActivity",
      "http://qudt.org/vocab/quantitykind/AbsoluteHumidity",
      "http://qudt.org/vocab/quantitykind/AbsorbedDose",
      "http://qudt.org/vocab/quantitykind/AbsorbedDoseRate",
      "http://qudt.org/vocab/quantitykind/Absorptance",
      "http://qudt.org/vocab/quantitykind/Acceleration",)

    update_json(json_path, url_list)

    with open(json_path, "r") as jsonFile:
        data = json.load(jsonFile)

    no_duplicates = False
    for url in data['uris']['enum']:
        if data['uris']['enum'].count(url) > 1:
            no_duplicates = True
    
    assert no_duplicates == True



if __name__ == "__main__":
    pytest.main()