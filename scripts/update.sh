#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python "${DIR}/update_site.py"

docker run --rm -it -v $(pwd):/src -v $(pwd)/public:/target klakegg/hugo:0.68.3-ext-alpine --theme book --minify

echo ""
echo "Built latest site."
echo ""
echo "To check it out first, run: docker run --rm -it -v \$(pwd):/src -p 1313:1313 klakegg/hugo:0.68.3-ext-alpine server --theme book --disableFastRender"
