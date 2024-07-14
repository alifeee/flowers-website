#!/bin/bash
# remove the image with the filename from POST data "photo"

declare -A param
while IFS='=' read -r -d '&' key value && [[ -n "$key" ]]; do
    param["$key"]=$value
done <<< "$(cat /dev/stdin)&"

# cat /dev/stdin
todel="${param[photo]}"
delme=$(echo "${todel}" | pcregrep -o1 'images%2F(.*)%27')
rm "/var/www/flowers/images/${delme}"

echo "Location: /flowers/edit.cgi"
echo ""
echo ""
