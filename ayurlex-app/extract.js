const fs = require('fs');
const path = require('path');

const content = fs.readFileSync('lib/i18n/dictionaries.ts', 'utf8');
const jsonStr = content.replace(/export const dictionaries:\s*Record<string, any>\s*=\s*/, '').trim().replace(/;$/, '');

// Write to a temporary JS file
fs.writeFileSync('temp_dict.js', 'module.exports = ' + jsonStr + ';', 'utf8');

const dicts = require('./temp_dict.js');
const localesDir = path.join(process.cwd(), 'locales');

if (!fs.existsSync(localesDir)) {
    fs.mkdirSync(localesDir);
}

for (const [lang, data] of Object.entries(dicts)) {
    const langDir = path.join(localesDir, lang);
    if (!fs.existsSync(langDir)) {
        fs.mkdirSync(langDir);
    }
    fs.writeFileSync(path.join(langDir, 'ui.json'), JSON.stringify(data, null, 2), 'utf8');
}

fs.unlinkSync('temp_dict.js');
console.log('Successfully extracted locales with correct encoding!');
