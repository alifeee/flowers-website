#!/bin/bash
# return webpage with two forms, one for adding images, one for removing

echo "Content-Type: text/html"
echo ""

IMAGES=(`find "./images" -type f -not -path "*/[.]*" -not -name "*.txt" -print0 | xargs -0 stat -c"%Y %y %N" | sort -rn | awk '{print $5}'`)

. /var/www/flowers/mo

cat edit.mo | mo
