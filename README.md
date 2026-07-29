# TorrentScout — qBittorrent Search Plugin Suite

Python search plugins for qBittorrent. Adds torrent search engines (BitSearch.to) directly into qBittorrent's built-in search tab.

**Live site:** https://TorrentScout-qBittorrent-Search-Plugin-Suite.oriz.in

[![Stars](https://img.shields.io/github/stars/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite?style=flat-square&color=yellow)](https://github.com/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python&logoColor=white)
![qBittorrent](https://img.shields.io/badge/qBittorrent-4.x%2B-green?style=flat-square&logo=qbittorrent&logoColor=white)

## Included plugins

| Plugin | Engine | Categories |
|--------|--------|-----------|
| `bitsearch.py` | [BitSearch.to](https://bitsearch.to) | all, anime, books, games, movies, music, software, tv |

## Install

1. Open qBittorrent → **View → Search Engine** (enable the Search tab if hidden).
2. Click **Search plugins…** at the bottom right.
3. **Install a new plugin → Local file**, and select `bitsearch.py`.
4. The plugin appears in the engine list, ready to search.

Or install from URL:

```
https://raw.githubusercontent.com/chirag127/TorrentScout-qBittorrent-Search-Plugin-Suite/main/bitsearch.py
```

## Usage

Type a query in qBittorrent's Search tab, pick a category, and select **BitSearch** (or *All plugins*). Results stream in with name, size, seeds, leechers, and a magnet/torrent link. Double-click a result to download.

## Develop / test

```bash
python validate_plugin.py     # static checks the plugin against qBittorrent's contract
python -m pytest              # run the test suite (test_bitsearch*.py)
```

The plugin implements qBittorrent's Nova search contract: a class matching the filename, with `url`, `name`, `supported_categories`, `search()`, and `download_torrent()`. It relies on qBittorrent-supplied `helpers` and `novaprinter` modules at runtime.

## License

MIT — see [LICENSE](LICENSE).
