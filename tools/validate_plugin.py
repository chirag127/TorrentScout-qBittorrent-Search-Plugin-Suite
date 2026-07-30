#!/usr/bin/env python3
"""
Validation script for bitsearch.py qBittorrent plugin
Run from repo root or tools/ directory.
"""

import importlib.util
import os
import re
import sys

_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")
_PLUGIN_PATH = os.path.join(_SRC, "bitsearch.py")
sys.path.insert(0, _SRC)


def validate_plugin_structure():
    """Validate the plugin file structure and requirements"""
    print("=== Validating Plugin Structure ===")

    if not os.path.exists(_PLUGIN_PATH):
        print("FAIL: bitsearch.py file not found")
        return False

    try:
        spec = importlib.util.spec_from_file_location("bitsearch", _PLUGIN_PATH)
        bitsearch_module = importlib.util.module_from_spec(spec)

        # Mock deps before exec
        class _MockHelpers:
            @staticmethod
            def retrieve_url(url):
                return ""

            @staticmethod
            def download_file(info):
                return ""

        class _MockNovaPrinter:
            @staticmethod
            def prettyPrinter(result):
                pass

        sys.modules.setdefault("helpers", _MockHelpers())
        sys.modules.setdefault("novaprinter", _MockNovaPrinter())

        spec.loader.exec_module(bitsearch_module)

        if not hasattr(bitsearch_module, "bitsearch"):
            print("FAIL: bitsearch class not found in plugin")
            return False

        plugin_class = bitsearch_module.bitsearch

        for attr in ["url", "name", "supported_categories"]:
            if not hasattr(plugin_class, attr):
                print(f"FAIL: Required attribute '{attr}' not found")
                return False

        if not hasattr(plugin_class, "search"):
            print("FAIL: Required method 'search' not found")
            return False

        categories = plugin_class.supported_categories
        if not isinstance(categories, dict):
            print("FAIL: supported_categories must be a dictionary")
            return False

        for cat in [
            "all",
            "anime",
            "books",
            "games",
            "movies",
            "music",
            "software",
            "tv",
        ]:
            if cat not in categories:
                print(
                    f"FAIL: Required category '{cat}' not found in supported_categories"
                )
                return False

        print("PASS: Plugin structure validation passed")
        return True

    except Exception as e:
        print(f"FAIL: Error importing plugin: {e}")
        return False


def validate_plugin_metadata():
    """Validate plugin metadata"""
    print("\n=== Validating Plugin Metadata ===")

    try:
        with open(_PLUGIN_PATH, encoding="utf-8") as f:
            content = f.read()

        if not re.search(r"#VERSION:\s*[\d.]+", content):
            print("FAIL: VERSION metadata not found")
            return False

        if not re.search(r"#AUTHORS:", content):
            print("FAIL: AUTHORS metadata not found")
            return False

        if not re.search(r"#LICENSING INFORMATION:", content):
            print("FAIL: LICENSING INFORMATION metadata not found")
            return False

        print("PASS: Plugin metadata validation passed")
        return True

    except Exception as e:
        print(f"FAIL: Error reading plugin file: {e}")
        return False


def validate_output_format():
    """Validate that the plugin outputs in the correct format"""
    print("\n=== Validating Output Format ===")

    try:
        with open(_PLUGIN_PATH, encoding="utf-8") as f:
            content = f.read()

        if "from novaprinter import prettyPrinter" not in content:
            print("FAIL: prettyPrinter not imported correctly")
            return False

        if "prettyPrinter(" not in content:
            print("FAIL: prettyPrinter not used in search method")
            return False

        print("PASS: Output format validation passed")
        return True

    except Exception as e:
        print(f"FAIL: Error validating output format: {e}")
        return False


def validate_error_handling():
    """Validate error handling"""
    print("\n=== Validating Error Handling ===")

    try:
        with open(_PLUGIN_PATH, encoding="utf-8") as f:
            content = f.read()

        if "try:" not in content or "except" not in content:
            print("FAIL: No error handling found")
            return False

        if "file=sys.stderr" not in content:
            print("FAIL: Errors should be printed to stderr")
            return False

        print("PASS: Error handling validation passed")
        return True

    except Exception as e:
        print(f"FAIL: Error validating error handling: {e}")
        return False


def validate_url_construction():
    """Validate URL construction"""
    print("\n=== Validating URL Construction ===")

    try:

        class MockHelpers:
            @staticmethod
            def retrieve_url(url):
                return ""

            @staticmethod
            def download_file(info):
                return ""

        class MockNovaPrinter:
            @staticmethod
            def prettyPrinter(result):
                pass

        sys.modules["helpers"] = MockHelpers()
        sys.modules["novaprinter"] = MockNovaPrinter()

        import importlib

        if "bitsearch" in sys.modules:
            importlib.reload(sys.modules["bitsearch"])
        from bitsearch import bitsearch

        plugin = bitsearch()

        if plugin.url != "https://bitsearch.to":
            print(f"FAIL: Incorrect base URL: {plugin.url}")
            return False

        expected_categories = {
            "all": "",
            "anime": "anime",
            "books": "books",
            "games": "games",
            "movies": "movies",
            "music": "music",
            "software": "apps",
            "tv": "tv",
        }

        if plugin.supported_categories != expected_categories:
            print("FAIL: Incorrect category mapping")
            return False

        print("PASS: URL construction validation passed")
        return True

    except Exception as e:
        print(f"FAIL: Error validating URL construction: {e}")
        return False


def validate_parsing_logic():
    """Validate parsing logic with sample data"""
    print("\n=== Validating Parsing Logic ===")

    try:
        sample_html = """
        <h3><a href="/torrent/test123">Test Torrent</a></h3>
        Other/DiskImage 1.95 GB 4/18/2019
        28 seeders 41 leechers 1403 downloads
        <a href="magnet:?xt=urn:btih:TEST123">Magnet</a>
        """

        import importlib

        if "bitsearch" in sys.modules:
            importlib.reload(sys.modules["bitsearch"])
        from bitsearch import BitSearchParser

        parser = BitSearchParser()
        parser.parse_html(sample_html)

        if len(parser.results) == 0:
            print("FAIL: Parser failed to extract results from sample HTML")
            return False

        result = parser.results[0]

        for key in [
            "link",
            "name",
            "size",
            "seeds",
            "leech",
            "engine_url",
            "desc_link",
            "pub_date",
        ]:
            if key not in result:
                print(f"FAIL: Missing key '{key}' in result")
                return False

        if result["name"] != "Test Torrent":
            print(f"FAIL: Incorrect name extraction: {result['name']}")
            return False

        if not result["link"].startswith("magnet:"):
            print(f"FAIL: Incorrect magnet link extraction: {result['link']}")
            return False

        if result["seeds"] != "28":
            print(f"FAIL: Incorrect seeds extraction: {result['seeds']}")
            return False

        if result["leech"] != "41":
            print(f"FAIL: Incorrect leechers extraction: {result['leech']}")
            return False

        print("PASS: Parsing logic validation passed")
        return True

    except Exception as e:
        print(f"FAIL: Error validating parsing logic: {e}")
        return False


def main():
    """Run all validations"""
    print("Starting comprehensive bitsearch.py plugin validation...")
    print("=" * 60)

    validations = [
        validate_plugin_structure,
        validate_plugin_metadata,
        validate_output_format,
        validate_error_handling,
        validate_url_construction,
        validate_parsing_logic,
    ]

    results = []
    for validation in validations:
        try:
            results.append(validation())
        except Exception as e:
            print(f"FAIL: Validation failed with error: {e}")
            results.append(False)

    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY:")
    print("=" * 60)

    names = [
        "Plugin Structure",
        "Plugin Metadata",
        "Output Format",
        "Error Handling",
        "URL Construction",
        "Parsing Logic",
    ]

    for name, result in zip(names, results):
        print(f"{name:20} {'PASS' if result else 'FAIL'}")

    all_passed = all(results)
    print("\n" + "=" * 60)

    if all_passed:
        print("ALL VALIDATIONS PASSED!")
        print("The plugin is ready for use with qBittorrent")
    else:
        print("SOME VALIDATIONS FAILED")

    return all_passed


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
