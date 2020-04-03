#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Ryan Kanno <ryankanno@localkinegrinds.com>
#
# Distributed under terms of the MIT license.

from datetime import datetime
from datetime import timezone
import os
import pytz
import re
import requests
import tempfile


SHARE_URL = "https://drive.google.com/uc?export=download&id=1Nah9sM0ZPS4MjdRX06UXnctzkjJWBkVr"
PREPEND_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    f"prepend.md")
OUTPUT_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', 'content', '_index.md')


def _get_secure_download_link(url):
    r = requests.head(url, allow_redirects=True)
    return r.url


def _get_content_as_tempfile(url):
    r = requests.get(url)
    with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as f:
        f.write(r.content)
        f.flush()
        return f.name


def _get_current_hst_as_str(dt_format="%A, %B %-d, %Y %-I:%M %p HST"):
    HST = pytz.timezone('US/Hawaii')
    return datetime.now(timezone.utc).astimezone(HST).strftime(dt_format)


def _prepend_strip_content(content, prepend_file_path):
    stripped_content = '## Introduction\n\n' + re.split('\\## Introduction\\b', content)[-1]
    stripped_content = stripped_content.replace("![image alt text](image_0.png)", '')
    with open(prepend_file_path, 'r') as w:
        prepend_content = w.read()
        return prepend_content + f"\nLast Updated: _{_get_current_hst_as_str()}_\n\n" + stripped_content


def _update_content(tempfile_path, prepend_file_path):
    with open(tempfile_path, 'r') as f:
        updated_content = _prepend_strip_content(f.read(), prepend_file_path)
        with open(OUTPUT_FILE_PATH, 'w') as o:
            o.write(updated_content)


if __name__ == "__main__":
    tmp = _get_content_as_tempfile(SHARE_URL)
    _update_content(tmp, PREPEND_FILE_PATH)
    print(f"Successfully updated: {OUTPUT_FILE_PATH}")


# vim: fenc=utf-8
# vim: filetype=python
