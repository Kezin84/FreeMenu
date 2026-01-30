import sys

path = r'c:\FBC PROJECT\template_mau\src\views\baocao.vue'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the symbols in the chart footer line specifically
content = content.replace('↑ Dư:', 'Dư:')
content = content.replace('= Hòa vốn', 'Hòa vốn')
content = content.replace('↓ Thiếu:', 'Thiếu:')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated symbols successfully")
