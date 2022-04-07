"""
Populate Json Files
-------------------
Gather urls from web reources and dump into appropriate json files.
"""

import json
from enum import Enum
from pathlib import Path
from typing import List, NamedTuple

import requests
from requests.models import Response
from requests import HTTPError
from rdflib import Graph
from rdflib.plugins.sparql.processor import SPARQLResult

JSON_DIR = Path(__file__).parent.parent.absolute()


class SPARQL_QUERIES(Enum):
    """
    Helper to holding constants that are SPARQL queries
    """

    IS_A_QUDT_UNIT = """
    SELECT ?url {
        ?url a <http://qudt.org/schema/qudt/Unit>
    }
    """

    IS_A_QUDT_QUANTITY_KIND = """
    SELECT ?url {
        ?url a <http://qudt.org/schema/qudt/QuantityKind> 
    }
    """


class Resource(NamedTuple):
    """
    A class to represent a ...
    """

    url: str
    json_path: Path
    query: str


RESOURCES = [
    Resource(
        url="http://qudt.org/2.1/vocab/quantitykind",
        json_path=Path(JSON_DIR / "quantity-kinds.json"),
        query=SPARQL_QUERIES.IS_A_QUDT_QUANTITY_KIND.value,
    ),
    Resource(
        url="http://qudt.org/2.1/vocab/unit",
        json_path=Path(JSON_DIR / "units.json"),
        query=SPARQL_QUERIES.IS_A_QUDT_UNIT.value,
    ),
]


def get(url: str) -> (Response):
    """
    Helper to get a http response representing an RDF defined list of resources
    """

    r: Response = requests.get(url)
    if not r.ok:
        raise HTTPError(f'Could not get "{url}" with status code {r.status_code}')
    return r


def update_json(json_path: Path, url_list: List[str]):
    """
    Function to update the enum urls in a json file with any urls from the input
    list that are not already present.
    """

    with open(json_path, "r") as jsonFile:
        data = json.load(jsonFile)

        for url in url_list:
            if url not in data["uris"]["enum"]:
                data["uris"]["enum"].append(url)

    with open(json_path, "w") as jsonFile:
        json.dump(data, jsonFile, indent=2)


if __name__ == "__main__":
    """
    main loop that gathers urls from web resources as defined by RESOURCES,
    and dumps those urls in to appropriate json files
    """
    resource: Resource
    for resource in RESOURCES:

        response: Response = get(resource.url)

        g = Graph()
        g.parse(response.content)

        results: SPARQLResult = g.query(resource.query)

        resource_urls = [str(x.get("url")) for x in results.bindings if x.get("url")]

        update_json(resource.json_path, resource_urls)
