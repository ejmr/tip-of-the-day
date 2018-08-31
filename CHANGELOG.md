Changelog
=========

We document all notable changes to "Tip of the Day" in this file.
Please read ["Keep a Changelog"](https://keepachangelog.com/en/1.0.0/)
for greater details about the purpose and format.  This project follows
[Semantic Versioning](https://semver.org/) for its version numbers.

## Unreleased

### Added
- `--tip-file` option to load tips from a given file.
- Tips for `vifm`.
### Fixed
- Spacing on tips with one or more line-breaks.
### Removed
- Default value for the tips file, meaning users now *must* either
  define the `TOTD_TIP_FILE` environment variable or use the new
  `--tip-file` option on invocation.

## [0.1.0] - 2018-08-10

**Note:** This is the initial public release, hence the very
generalized, broad-stroke descriptions of what we "added" to this
release.  The most honest, blunt, and accurate description of what
we added for this relaese is: *everything.*

### Added
- An example in the README of how to add tips.
- An optional environment variable naming the tips file.
- Justfile recipes to lint the code, data, and documentation.
- A file containing some of my (ejmr) tips to act as a larger example
  than what we describe in the README.
