#!/bin/bash
# return webpage with images from images folder

echo "Content-Type: text/html"
echo ""

IMAGES=(`find "./images" -type f -not -path "*/[.]*" -print0 | xargs -0 stat -c"%Y %y %N" | sort -rn | awk '{print $5}'`)

. /var/www/flowers/mo

cat index.mo | mo
