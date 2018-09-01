Changelog
=========

We document all notable changes to "Tip of the Day" (ToTD) in this file.
Please read ["Keep a Changelog"](https://keepachangelog.com/en/1.0.0/)
for greater details about the purpose and format.  This project follows
[Semantic Versioning](https://semver.org/) for its version numbers.

## Unreleased

## [0.2.0] - 2018-08-31

### Added
- List of required packages to use with `pip`, specifically
  `pip install -r requirements.txt` now installs dependencies.
- `--tip-file` option to load tips from a given file.
  - The user can provide the option multiple times.
  - ToTD will randomly select one file as a source of tips.
  - The `test-multiple-tip-files` recipe tests this behavior.
    However, the test depends on data which is currently not
    part of the repository.
- Support multiple files via the `TOTD_TIP_FILE` environment variable.
- Tips for `vifm`.
### Fixed
- Spacing on tips with one or more line-breaks.
### Changed
- Releasing updates via `just push` will fail if any linters fail.
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
