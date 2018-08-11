from pathlib import Path
from typing import Dict
import os
import random
import click
import ruamel.yaml

__author__ = "Eric James Michael Ritz"
__version__ = "0.1.0"


class Tip:
    """A tip for a given topic.

    Objects of this class represent the tips that we display to the
    user, and which we read in from a YAML document.  Normally a tip
    is a dictionary that maps strings to other strings, which is not
    inherently difficult to deal with.

    But providing this class as an effective synonym for that data
    structure affords us both some useful abstraction, e.g. easier
    formatting, and makes it easier to introduce additional content
    to tips in the future, e.g. an optional list of keywords.
    """

    def __init__(self, raw_tip_data: Dict[str, str]):
        self.topic = raw_tip_data["topic"]
        self.tip = raw_tip_data["tip"]

    def __str__(self):
        return f"Tip of the Day: {self.topic}\n\n{self.tip}"


@click.command()
@click.version_option(version=__version__)
def totd():
    """Display a random software or programming tip."""
    path_to_tips_file = Path(os.getenv("TOTD_TIP_FILE", "./Tips.yaml"))
    yaml = ruamel.yaml.YAML(typ="safe")
    tips = yaml.load(path_to_tips_file)
    print(Tip(random.choice(tips)))


if __name__ == "__main__":
    totd()
