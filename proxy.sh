#!/bin/bash

# Define the new proxy setting
NEW_PROXY="--proxy socks5://zmiowonw-rotate:kd275manvaz6@p.webshare.io:80"

# Define the list of files to edit
FILES=(
    "/etc/yt-dlp.conf"
    "/etc/yt-dlp/config"
    "/etc/yt-dlp/config.txt"
)

# Loop through each file
for FILE in "${FILES[@]}"; do
    if [ -f "$FILE" ]; then
        # Backup the original file
        cp "$FILE" "$FILE.bak"

        # Remove lines containing the old proxy setting and add the new proxy setting
        awk '!/--proxy/' "$FILE.bak" > "$FILE"
        echo "$NEW_PROXY" >> "$FILE"

        # Clean up backup file
        rm "$FILE.bak"
    else
        echo "File $FILE does not exist."
    fi
done
