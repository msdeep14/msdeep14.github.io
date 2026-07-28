import re
import sys
import os

books_file = '/Users/msdeep14/Documents/Code Projects/msdeep14.github.io/_includes/books.html'
sass_file = '/Users/msdeep14/Documents/Code Projects/msdeep14.github.io/_sass/_books.scss'

with open(books_file, 'r') as f:
    content = f.read()

# Extract all <style> blocks
styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)

# Write to _sass/_books.scss
with open(sass_file, 'w') as f:
    f.write('// _sass/_books.scss\n\n')
    for style in styles:
        # Modernize some hardcoded colors
        style = re.sub(r'#ddd|#ccc|#e8e8e8|#eee', 'var(--border-color)', style)
        style = re.sub(r'#f9f9f9|#f1f1f1', 'var(--card-bg)', style)
        style = re.sub(r'#333|#222|#444|#555', 'var(--text-color)', style)
        style = re.sub(r'rgba\(0,\s*0,\s*0,\s*0\.\d+\)', 'var(--card-shadow)', style)
        style = re.sub(r'background-color:\s*white;', 'background-color: var(--card-bg);', style)
        style = re.sub(r'color:\s*white;', 'color: var(--btn-text);', style)
        style = re.sub(r'Arial,\s*sans-serif', 'var(--font-sans)', style)
        f.write(style + '\n')

# Remove all <style> blocks from books.html
new_content = re.sub(r'<style[^>]*>.*?</style>\s*', '', content, flags=re.DOTALL)

with open(books_file, 'w') as f:
    f.write(new_content)

print("Refactoring complete.")
