# fmt: off
#VERSION: 1.00
#AUTHORS: Chirag Singhal
#LICENSING INFORMATION: MIT
# fmt: on

import re
import sys
import urllib.parse

from helpers import download_file, retrieve_url
from novaprinter import prettyPrinter


class bitsearch:
    """
    BitSearch.to search engine plugin for qBittorrent
    """

    url = "https://bitsearch.to"
    name = "BitSearch"
    supported_categories = {
        "all": "",
        "anime": "anime",
        "books": "books",
        "games": "games",
        "movies": "movies",
        "music": "music",
        "software": "apps",
        "tv": "tv",
    }

    def __init__(self):
        pass

    def download_torrent(self, info):
        """Download torrent file"""
        print(download_file(info))

    def search(self, what, cat="all"):
        """Search for torrents on bitsearch.to"""
        query = urllib.parse.quote_plus(what)

        if cat == "all":
            search_url = f"{self.url}/search?q={query}"
        else:
            category = self.supported_categories.get(cat, "")
            if category:
                search_url = f"{self.url}/search?q={query}&category={category}"
            else:
                search_url = f"{self.url}/search?q={query}"

        for page in range(1, 4):
            page_url = f"{search_url}&page={page}" if page > 1 else search_url

            try:
                html_content = retrieve_url(page_url)
                if not html_content:
                    continue

                parser = BitSearchParser()
                parser.parse_html(html_content)

                for result in parser.results:
                    if result.get("name") and result.get("link"):
                        prettyPrinter(result)

            except Exception as e:
                print(f"Error searching page {page}: {e!s}", file=sys.stderr)
                continue


class BitSearchParser:
    """HTML parser for bitsearch.to search results"""

    def __init__(self):
        self.results = []

    def parse_html(self, html_content):
        """Parse search results using regex patterns"""
        try:
            html_content = html_content.replace("\n", " ").replace("\r", " ")
            self.extract_bitsearch_results(html_content)
        except Exception as e:
            print(f"Error in HTML parsing: {e!s}", file=sys.stderr)

    def extract_bitsearch_results(self, html_content):
        """Extract results from bitsearch.to specific HTML structure"""
        result_pattern = r'<h3[^>]*>.*?<a[^>]*href="(/torrent/[^"]+)"[^>]*>([^<]+)</a>.*?</h3>(.*?)(?=<h3|<div[^>]*class="[^"]*pagination|$)'
        matches = re.findall(result_pattern, html_content, re.DOTALL | re.IGNORECASE)

        for desc_link_path, title, content_block in matches:
            result = {
                "link": "",
                "name": title.strip(),
                "size": "-1",
                "seeds": "-1",
                "leech": "-1",
                "engine_url": "https://bitsearch.to",
                "desc_link": "https://bitsearch.to" + desc_link_path,
                "pub_date": "-1",
            }

            magnet_match = re.search(r'href="(magnet:[^"]+)"', content_block)
            if magnet_match:
                result["link"] = magnet_match.group(1)

            size_match = re.search(
                r"(\d+(?:\.\d+)?)\s*([KMGT]?B)", content_block, re.IGNORECASE
            )
            if size_match:
                size_bytes = self.parse_size(
                    f"{size_match.group(1)} {size_match.group(2)}"
                )
                if size_bytes > 0:
                    result["size"] = str(size_bytes)

            seeds_match = re.search(r"(\d+)\s+seeders?", content_block, re.IGNORECASE)
            if seeds_match:
                result["seeds"] = seeds_match.group(1)

            leechers_match = re.search(
                r"(\d+)\s+leechers?", content_block, re.IGNORECASE
            )
            if leechers_match:
                result["leech"] = leechers_match.group(1)

            date_match = re.search(r"(\d{1,2}/\d{1,2}/\d{4})", content_block)
            if date_match:
                timestamp = self.parse_date(date_match.group(1))
                if timestamp > 0:
                    result["pub_date"] = str(timestamp)

            if result["name"] and result["link"]:
                self.results.append(result)

        if not self.results:
            self.extract_fallback_results(html_content)

    def extract_fallback_results(self, html_content):
        """Fallback extraction when main pattern fails"""
        magnets = re.findall(r'href="(magnet:[^"]+)"', html_content)
        titles = re.findall(
            r'<a[^>]*href="/torrent/[^"]*"[^>]*>([^<]+)</a>',
            html_content,
            re.IGNORECASE,
        )
        sizes = re.findall(r"(\d+(?:\.\d+)?)\s*([KMGT]?B)", html_content, re.IGNORECASE)
        seeds = re.findall(r"(\d+)\s+seeders?", html_content, re.IGNORECASE)
        leechers = re.findall(r"(\d+)\s+leechers?", html_content, re.IGNORECASE)
        desc_links = re.findall(r'href="(/torrent/[^"]+)"', html_content)

        max_results = min(len(magnets), len(titles)) if titles else len(magnets)

        for i in range(max_results):
            result = {
                "link": magnets[i] if i < len(magnets) else "",
                "name": titles[i].strip() if i < len(titles) else f"Torrent {i + 1}",
                "size": str(self.parse_size(f"{sizes[i][0]} {sizes[i][1]}"))
                if i < len(sizes)
                else "-1",
                "seeds": seeds[i] if i < len(seeds) else "-1",
                "leech": leechers[i] if i < len(leechers) else "-1",
                "engine_url": "https://bitsearch.to",
                "desc_link": f"https://bitsearch.to{desc_links[i]}"
                if i < len(desc_links)
                else "",
                "pub_date": "-1",
            }
            if result["name"] and result["link"]:
                self.results.append(result)

    def parse_size(self, size_str):
        """Convert size string to bytes"""
        try:
            size_str = size_str.upper().replace(",", "").strip()
            match = re.search(r"([\d.]+)\s*([KMGT]?B)", size_str)
            if not match:
                return -1
            multipliers = {
                "B": 1,
                "KB": 1024,
                "MB": 1024**2,
                "GB": 1024**3,
                "TB": 1024**4,
            }
            return int(float(match.group(1)) * multipliers.get(match.group(2), 1))
        except Exception:
            return -1

    def parse_date(self, date_str):
        """Parse date string to unix timestamp"""
        import time
        from datetime import datetime

        date_str = date_str.strip()
        for fmt in [
            "%m/%d/%Y",
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%Y-%m-%d %H:%M:%S",
            "%m/%d/%Y %H:%M:%S",
        ]:
            try:
                return int(time.mktime(datetime.strptime(date_str, fmt).timetuple()))
            except Exception:
                continue
        return -1
