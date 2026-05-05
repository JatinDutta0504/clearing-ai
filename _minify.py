#!/usr/bin/env node
// CSS + JS minifier for The Clearing — Phase 3 Performance Sprint
const fs = require('fs');
const path = require('path');

function minifyCSS(input) {
  return input
    .replace(/\/\*[\s\S]*?\*\//g, '') // remove comments
    .replace(/\s+/g, ' ')              // collapse whitespace
    .replace(/\s*([{}:;,])\s*/g, '$1')  // remove space around syntax chars
    .replace(/;\}/g, '}')               // remove trailing semicolon before }
    .replace(/\{([0-9.]+(?:px|em|rem|%|vh|vw|vmin|vmax|s|ms))/g, '{ $1') // space after { before numbers
    .replace(/([0-9.]+(?:px|em|rem|%|vh|vw|vmin|vmax|s|ms))\}/g, '$1 }') // space before } after numbers
    .replace(/:\s+/g, ': ')            // no space after colons
    .replace(/,\s+/g, ', ')             // space after commas
    .replace(/;\s+/g, '; ')             // space after semicolons
    .replace(/' "/g, "'\"")            // normalize quotes
    .trim();
}

function minifyJS(input) {
  return input
    .replace(/\/\*[\s\S]*?\*\//g, '') // remove block comments
    .replace(/\/\/[^\n]*/g, '')       // remove line comments
    .replace(/\s+/g, ' ')             // collapse whitespace
    .replace(/\s*([{};,:])\s*/g, '$1')// remove space around syntax
    .trim();
}

const srcCSS = path.join(__dirname, 'css/style.css');
const outCSS = path.join(__dirname, 'css/style.min.css');
const srcJS = path.join(__dirname, 'js/main.js');
const outJS = path.join(__dirname, 'js/main.min.js');

const css = fs.readFileSync(srcCSS, 'utf8');
const js = fs.readFileSync(srcJS, 'utf8');

const minCSS = minifyCSS(css);
const minJS = minifyJS(js);

fs.writeFileSync(outCSS, minCSS, 'utf8');
fs.writeFileSync(outJS, minJS, 'utf8');

console.log('CSS: ' + css.length + ' → ' + minCSS.length + ' bytes (' + Math.round((css.length - minCSS.length) / css.length * 100) + '% saved)');
console.log('JS:  ' + js.length + ' → ' + minJS.length + ' bytes (' + Math.round((js.length - minJS.length) / js.length * 100) + '% saved)');