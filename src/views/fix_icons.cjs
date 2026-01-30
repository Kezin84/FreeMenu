const fs = require('fs');
const path = 'c:\\FBC PROJECT\\template_mau\\src\\views\\baocao.vue';
let content = fs.readFileSync(path, 'utf8');

// Replace symbols in the chart footer line specifically
content = content.replace('↑ Dư:', 'Dư:');
content = content.replace('= Hòa vốn', 'Hòa vốn');
content = content.replace('↓ Thiếu:', 'Thiếu:');

fs.writeFileSync(path, content, 'utf8');
console.log('Updated symbols successfully');
