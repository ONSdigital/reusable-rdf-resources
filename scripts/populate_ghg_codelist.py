import click
import pandas as pd
from pathlib import Path
import json

'''Generates a high level code list for Greenhouse gases. Code list is created using this table https://github.com/GSS-Cogs/family-climate-change/blob/master/reference/codelists/ghg.csv
in family climate change repo. Greenhouse gases are linked to the respective DBPedia resource, this is included in the Same As column'''

@click.command()
@click.option(
    "--url",
    default=("https://github.com/GSS-Cogs/family-climate-change/blob/master/reference/codelists/ghg.csv?raw=True"),
    help="The url for the csv.",
)
@click.option(
    "--output",
    "-o",
    default=Path("./ghg-code-list.json"),
    type=click.Path(path_type=Path),
    help="The output file",
)
def ghgcodelist(url: Path, output: Path) -> None:
    template = {
    "$schema": "https://purl.org/csv-cubed/code-list-config/v1",
    "title": "Greenhouse gases code list",
    "summary": "List of greenhouse gases",
    "description": "Automated non-hierarchical greenhouse gases code list linked to DBPedia",
    "creator": "https://www.gov.uk/government/organisations/office-for-national-statistics",
    "publisher": "https://www.gov.uk/government/organisations/office-for-national-statistics",
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "sort": {
      "by": "label",
      "method": "ascending"
    },
    "concepts": []
  }

    df = pd.read_csv(url)

    df = df[["Label", "Notation", "Same As"]].rename(columns={"Label": "label", "Notation": "notation", "Same As": "same_as"})

    df = df[["label", "notation", "same_as"]]

    code_list = json.loads(df.to_json(orient="records"))

    template["concepts"] = code_list

    with open(output, "w") as f:
        json.dump(template, f, indent=4)

    return

if __name__ == "__main__":
    ghgcodelist()