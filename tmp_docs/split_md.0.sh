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

while IFS= read -r line; do
  if [[ "$line" =~ ^(#+)\ (.*) ]]; then
    level=${#BASH_REMATCH[1]}
    title="${BASH_REMATCH[2]}"
    slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g' | sed -E 's/^-+|-+$//g')
    
    # Build directory path
    if [[ $level -eq 1 ]]; then
      path="$OUTDIR/$slug"
    else
      parent="${level_paths[$((level-1))]}"
      path="$parent/$slug"
    fi
    mkdir -p "$path"
    level_paths[$level]="$path"
    curr_dir="$path"
    echo "# $title" > "$curr_dir/README.md"
  else
    echo "$line" >> "$curr_dir/README.md"
  fi
done < "$INPUT"
