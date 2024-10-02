#!/bin/bash
# remove the image with the filename from POST data "photo"

declare -A param
while IFS='=' read -r -d '&' key value && [[ -n "$key" ]]; do
    param["$key"]=$value
done <<< "$(cat /dev/stdin)&"

# cat /dev/stdin
todel="${param[photo]}"
delme=$(echo "${todel}" | pcregrep -o1 'images%2F(.*)%27')
basename="${delme%.*}"

rm "/var/www/flowers/images/${delme}"
rm "/var/www/flowers/images/${basename}.txt"

echo "Location: /flowers/edit.cgi"
echo ""
echo ""
