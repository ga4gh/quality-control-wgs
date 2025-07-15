#!/bin/bash

INPUT="$1"
OUTDIR="$2"

if [[ -z "$INPUT" || -z "$OUTDIR" ]]; then
  echo "Usage: $0 <input.md> <output_dir>"
  exit 1
fi

mkdir -p "$OUTDIR"
curr_dir="$OUTDIR"
declare -a level_paths
declare -a file_paths

while IFS= read -r line; do
  if [[ "$line" =~ ^(#+)\ (.*) ]]; then
    level=${#BASH_REMATCH[1]}
    title="${BASH_REMATCH[2]}"
    slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g' | sed -E 's/^-+|-+$//g')

    # Determine current path and file
    if [[ $level -eq 1 ]]; then
      path="$OUTDIR/$slug"
    else
      parent="${level_paths[$((level-1))]}"
      path="$parent/$slug"
    fi

    mkdir -p "$path"
    file="$path/$slug.md"

    level_paths[$level]="$path"
    file_paths[$level]="$file"
    curr_file="$file"

    echo "# $title" > "$curr_file"
  else
    echo "$line" >> "$curr_file"
  fi
done < "$INPUT"
