#!/bin/bash

# Script to add contact widget to all HTML pages

# Find all HTML files (excluding site-deploy, backup-site-deploy, wp-content, and already modified files)
find . -name "index.html" \
    -not -path "./site-deploy/*" \
    -not -path "./backup-site-deploy/*" \
    -not -path "./wp-content/*" \
    -not -path "./contact-widget.html" \
    -not -path "./contact-widget-demo.html" | while read file; do
    
    # Check if widget is already added
    if grep -q "contactWidget" "$file"; then
        echo "✓ Widget already in: $file"
        continue
    fi
    
    # Determine relative path for CSS/JS based on file location
    # Count directory depth
    dir_depth=$(echo "$file" | tr -cd '/' | wc -c)
    
    if [ "$dir_depth" -eq 0 ]; then
        # Root level: ./index.html
        css_path="contact-widget.css"
        js_path="contact-widget.js"
    else
        # Subdirectory: generate ../ based on depth
        css_path=$(printf '../%.0s' $(seq 1 $dir_depth))"contact-widget.css"
        js_path=$(printf '../%.0s' $(seq 1 $dir_depth))"contact-widget.js"
    fi
    
    # Find the line number of </body>
    body_line=$(grep -n "</body>" "$file" | tail -1 | cut -d: -f1)
    
    if [ -z "$body_line" ]; then
        echo "✗ No </body> found in: $file"
        continue
    fi
    
    # Create temporary file with widget
    temp_file=$(mktemp)
    
    # Insert widget before </body>
    head -n $((body_line - 1)) "$file" > "$temp_file"
    echo "<!-- Contact Widget -->" >> "$temp_file"
    echo "<link rel=\"stylesheet\" href=\"$css_path\">" >> "$temp_file"
    echo "<script src=\"$js_path\"></script>" >> "$temp_file"
    echo "<div id=\"contactWidget\"></div>" >> "$temp_file"
    tail -n +"$body_line" "$file" >> "$temp_file"
    
    # Replace original file
    mv "$temp_file" "$file"
    
    echo "✓ Added widget to: $file"
done

echo ""
echo "✅ Done! Contact widget added to all pages."

