# Fix: Find the cut-off task 4 and replace with complete content
old_tail = """          <div class="task-ratings">
            <div class="task-rating">
            <div class="tool">GitHub Copilot</div>
              <div class="verdict">High productivity — low cognitive load upfront</div>
              <div class="rating r-high">✅ Best for fast prototyping</div>
            </div>
            <div class="task-rating">
              <div class="tool">Cursor</div>
              <div class="verdict">High productivity — AI-native editing accelerates prototyping</div>
              <div class="rating r-high">✅ Best for fast prototyping</div>
            </div>
            <div class="task-rating">
              <div class="tool">ChatGPT</div>
              <div class="verdict">Moderate — conversations are slower for rapid iteration</div>
              <div class="rating r-mid">⚡ Moderate</div>
            </div>
            <div class="task-rating">
              <div class="tool">Claude Code</div>
              <div class="verdict">Moderate — thorough but slower for pure prototyping</div>
              <div class="rating r-mid">⚡ Moderate</div>
            </div>
            <div class="task-rating">
              <div class="tool">Codeium</div>
              <div class="verdict">Moderate — decent completions, less context than Copilot</div>
              <div class="rating r-mid">⚡ Moderate</div>
            </div>
          </div>"""

import os
path = '/Users/nightcoder/Desktop/TheClearing/coding-ai-tools-comparison.html'
with open(path, 'r') as f:
    content = f.read()

# Find the cut-off point — look for the broken task 4 section
# Find "</section>" near the prototyping area and truncate after that
idx = content.find('task-ratings')
# find second occurrence of task-ratings
idxs = [i for i in range(len(content)) if content.startswith('task-ratings', i)]
print(f"Found task-ratings at indices: {idxs}")

# Check if the file ends properly
ends_ok = content.rstrip().endswith('</html>') or content.rstrip().endswith('</body>')
print(f"File ends properly: {ends_ok}")
print(f"Last 200 chars: {repr(content[-200:])}")
