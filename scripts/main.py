from enum import Enum
from pathlib import Path
from typing import List

import json
import requests
from requests.models import Response
from requests import HTTPError
from rdflib import Graph
from rdflib.plugins.sparql.processor import SPARQLResult
from rdflib.plugins.sparql.sparql import FrozenBindings

RESOURCE_URLS = {
    'http://qudt.org/2.1/vocab/unit' : 'units.json',
    'http://qudt.org/2.1/vocab/quantitykind' : 'quantity-kinds.json',
}


class SPARQL_QUERIES(Enum):
    """
    Helper to holding constants that are SPARQL queries
    """

    IS_A_QUDT_UNIT = """
    SELECT ?unit {
        ?unit a <http://qudt.org/schema/qudt/Unit>
    }
    """

    IS_A_QUDT_QUANTITY_KIND = """
    SELECT ?quantitykind (
        ?quantitykind a <http://qudt.org/schema/qudt/QuantityKind> 
    )
    """


def get(url: str) -> Response:
    """
    Helper to get a http response representing an RDF defined list of resources 
    """

    r: Response = requests.get(url)
    if not r.ok:
        raise HTTPError(f'Could not get "{url}" with status code {r.status_code}')
    return r


def update_json(json_name: str, url_list: List[str]):
    """
    Function to update the enum urls in a json file with any urls from the input
    list that are not already present.
    """

    json_file = Path(__name__).parent/json_name

    with open(json_file, "r") as jsonFile:
        data = json.load(jsonFile)

        #data['enum'].append(url_list)
        for url in url_list:
            #data['uris']["enum"].append(url)
            data['enum'] += url

    with open(json_file, "w") as jsonFile:
        json.dump(data, jsonFile)
    # Read in the target json file

    # Add any urls from url_list that are not in the enum field within the json file

    # Write it back now its updated.



for resource_url, json_name in RESOURCE_URLS.items():
    
    response: Response = get(resource_url)

    g = Graph()
    g.parse(response.content)

    results: SPARQLResult= g.query(SPARQL_QUERIES.IS_A_QUDT_UNIT.value)

    resource_urls = [str(x.get('unit')) for x in results.bindings]

    update_json(json_name, resource_urls)
