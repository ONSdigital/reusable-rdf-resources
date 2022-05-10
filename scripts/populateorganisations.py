from pathlib import Path
import json
import logging

import pandas as pd

_column_name_to_extract = "Identifier (registered site)"

logger = logging.getLogger(__name__)


def populate_organisations(csv_input: Path, json_output: Path):
    organisation_uris = list(pd.read_csv(csv_input)[_column_name_to_extract])

    logger.debug("Acquired organisations from CSV file.")

    with open(json_output, "r") as f:
        file_contents = json.load(f)

        logger.debug(f"Loaded JSON from {json_output}")

        file_contents["uris"]["enum"] = organisation_uris

    with open(json_output, "w") as f:
        logger.debug(f"Writing JSON to {json_output}")
        json.dump(file_contents, f, indent=4)
    
    logger.debug("Done")


if __name__ == "__main__":
    populate_organisations(Path("rdf-definitions") / "organisations" / "organisations.csv", Path("organisations.json"))
