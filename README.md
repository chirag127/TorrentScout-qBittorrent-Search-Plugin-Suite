# qBittorrent BitSearch Plugin

[![Stars](https://img.shields.io/github/stars/chirag127/qbittorrent-bitsearch?style=flat-square&color=yellow)](https://github.com/chirag127/qbittorrent-bitsearch/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python&logoColor=white)

**Live docs:** https://qbittorrent-bitsearch.oriz.in

qBittorrent search plugin for the [BitSearch](https://bitsearch.to) torrent search engine. Adds BitSearch as a search source in qBittorrent's built-in Search tab. Single `.py` file, no external dependencies.

## Install

### From URL (recommended)

1. Open qBittorrent.
2. View → Search Engine (enable Search tab if hidden).
3. Click **Search plugins…** → **Install a new one**.
4. Paste this URL:

```
https://raw.githubusercontent.com/chirag127/qbittorrent-bitsearch/main/src/bitsearch.py
```

### Local file

Download `src/bitsearch.py` and use **Install a new one → Local file** in the same dialog.

## Usage

Type a query in qBittorrent's Search tab, pick a category, select **BitSearch** (or *All plugins*). Results stream in with name, size, seeds, leechers, and a magnet link. Double-click a result to download.

## Supported categories

| qBittorrent | BitSearch mapping |
|-------------|-------------------|
| all | (all) |
| anime | anime |
| books | books |
| games | games |
| movies | movies |
| music | music |
| software | apps |
| tv | tv |

## Repository layout

```
src/
  bitsearch.py        # installable plugin (self-contained, as qBittorrent requires)
tests/
  test_bitsearch.py       # mock-based unit test
  test_bitsearch_real.py  # sample-HTML integration test
  final_test.py           # comprehensive usability test
tools/
  validate_plugin.py  # static + runtime validator
docs/                 # GitHub Pages site (https://qbittorrent-bitsearch.oriz.in)
```

## Development

```bash
# validate plugin contract
python tools/validate_plugin.py

# run tests
python tests/final_test.py
python tests/test_bitsearch_real.py
```

The plugin implements qBittorrent's Nova search contract: a class matching the filename, with `url`, `name`, `supported_categories`, `search()`, and `download_torrent()`. It relies on qBittorrent-supplied `helpers` and `novaprinter` modules at runtime — these are mocked in tests.

## License

MIT — see [LICENSE](LICENSE).
