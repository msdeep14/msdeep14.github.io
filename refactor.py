import os
import glob
import re
import json
import sys

files = sorted(glob.glob('/Users/msdeep14/Documents/Code Projects/msdeep14.github.io/projects/*.html'))

chunk_size = 4
chunk_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0

files = files[chunk_idx * chunk_size : (chunk_idx + 1) * chunk_size]

results = []

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3: return
    
    front_matter = f"---\n{parts[1].strip()}\n---\n\n"
    html_content = parts[2]
    
    github_link = ""
    ribbon_match = re.search(r'<div class="ribbon">.*?href="(.*?)".*?</div>', html_content, re.DOTALL | re.IGNORECASE)
    if ribbon_match: github_link = ribbon_match.group(1)
        
    title = ""
    h1_match = re.search(r'<h1[^>]*>.*?<a[^>]*>(.*?)</a>.*?</h1>', html_content, re.DOTALL | re.IGNORECASE)
    if h1_match:
        title = h1_match.group(1).strip()
    else:
        h1_match_2 = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.DOTALL | re.IGNORECASE)
        if h1_match_2:
            title = re.sub(r'<[^>]+>', '', h1_match_2.group(1)).strip()
            
    if not title: title = os.path.basename(filepath).replace('.html', '').capitalize()
        
    desc = ""
    h4_match = re.search(r'<h4[^>]*>(.*?)</h4>', html_content, re.DOTALL | re.IGNORECASE)
    if h4_match: desc = h4_match.group(1).strip()
        
    gallery_html = ""
    gallery_match = re.search(r'<div class\s*=\s*["\']images["\']>(.*?)</div>\s*</body>', html_content, re.DOTALL | re.IGNORECASE)
    if gallery_match:
        gallery_html = gallery_match.group(1)
        gallery_html = re.sub(r'<div class\s*=\s*["\']zoomin["\']>', '', gallery_html, flags=re.IGNORECASE)
        gallery_html = re.sub(r'</div>\s*$', '', gallery_html.strip(), flags=re.IGNORECASE)
    else:
        after_h4 = re.split(r'</h4>', html_content, flags=re.IGNORECASE)
        if len(after_h4) > 1:
            rest = after_h4[-1]
            rest = re.sub(r'</body>|</html>', '', rest, flags=re.IGNORECASE)
            gallery_html = rest.strip()
            
    gallery_html = re.sub(r'<br\s*/?>', '', gallery_html, flags=re.IGNORECASE).strip()
            
    new_html = []
    new_html.append('<div class="project-header">')
    new_html.append(f'  <h1>{title}</h1>')
    if github_link:
        new_html.append(f'  <a href="{github_link}" class="btn-github" target="_blank" rel="noopener noreferrer"><i class="fa fa-github"></i> View on GitHub</a>')
    
    if desc:
        new_html.append(f'  <h4>{desc}</h4>')
    new_html.append('</div>\n')
    
    if gallery_html:
        new_html.append('<div class="project-gallery">')
        new_html.append(gallery_html)
        new_html.append('</div>\n')
        
    final_output = front_matter + "\n".join(new_html) + "\n"
    results.append({"filepath": filepath, "content": final_output})

for file in files:
    process_file(file)

print(json.dumps(results))
