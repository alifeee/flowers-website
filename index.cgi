#!/bin/bash
# return webpage with images from images folder

echo "Content-Type: text/html"
echo ""

IMAGES=(`find "./images" -type f -not -path "*/[.]*" -name "*.jpg" -print0 | xargs -0 stat -c"%Y %y %N" | sort -rn | awk '{print $5}' | tr -d "'"`)

# colour of each flower image
declare -a COLOURS
# list of html links to use in template
declare -a LINKS

for key in "${!IMAGES[@]}"; do
	# full filename
  fname="${IMAGES[$key]}"
  # just filename without extension
  basename=$(basename "${fname}" ".jpg")
  # 6 digit hex colour
	colour=$(cat "./images/${basename}.txt")
  # fallback to black
	if [[ ! "${colour}" =~ [0-9a-fA-F]{6} ]]; then
		colour="000000"
	fi
	COLOURS[$key]="${colour}"
	LINKS[$key]="<a href='${fname}' style="--c:#${colour}"></a>"
done

. /var/www/flowers/mo

cat index.mo | mo
