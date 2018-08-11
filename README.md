Tip of the Day
==============

## SYNOPSIS

    $ totd.py
    $ totd.py --help

    # ¯\_(ツ)_/¯
    $ echo "totd.py | cowsay -f hellokitty" >> ~/.bashrc

## DESCRIPTION

*Tip of the Day* (TotD) is a program which displays a random tip about
software, programming, et cetera.  It selects tips from a user-defined
[YAML][] document; see below on how to configure the location of that file.
The YAML file represents a list of entries (i.e. what many programming
languages call 'hash-maps', 'dictionaries', 'tables', so on) where each
entry has two keys:

1. `topic`: The name of the program or language the tip describes.
2. `tip`: The text of the tip itself.

Here is an example tip for [Git](https://git-scm.org/), and note well
that whitespace is significant:

    -
      topic: Git
      tip: >
        You can run `git rev-parse --show-toplevel` to see the
        top-level directory of any repository.  This is valuable
        in shell scripts when you need to ensure some action
        occurs in a repository's root directory, e.g. creating
        a path to the local hooks for that repository.

The indentation can be any number of spaces as long as the spacing is
consistent.  A full description of indentation rules for YAML is beyond
the scope of this document, so please see the official specification
for complete details.

The content of each tip *should* be valid [Markdown (for Pandoc)][pan-md]
but this is not mandatory, simply a strong recommendation.  Future
updates, specifically with regard to formatting or output options,
will always assume that tip content *might* by Markdown.

## REQUIREMENTS

* [Python](https://python.org/) >= 3.6
* [Click](http://click.pocoo.org/6/) >= 6.0
* [ruamel.yaml](http://yaml.readthedocs.io/en/latest/index.html) >= 0.15

## ENVIRONMENT

The program uses the following environment variables:

* `TOTD_TIP_FILE`:
  This must be an absolute path to the `Tips.yaml` file containing the
  actual tips.  If undefined then the program assumes `Tips.yaml` is in
  the same directory as the program itself.

## AUTHOR

[Eric James Michael Ritz][ejmr]

## COPYRIGHT

[Creative Commons Zero][CC0] 2018

## SEE ALSO

- [fortune(6)](https://linux.die.net/man/6/fortune)
- [cowsay](https://en.wikipedia.org/wiki/Cowsay)



[pan-md]: http://pandoc.org/MANUAL.html#pandocs-markdown
[ejmr]: https://github.com/ejmr/
[CC0]: https://creativecommons.org/publicdomain/zero/1.0/legalcode
[YAML]: http://yaml.org/
