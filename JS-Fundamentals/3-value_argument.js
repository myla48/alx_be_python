// 3-value_argument.js

const args = process.argv.slice(2);
console.log(args[0] !== undefined ? args[0] : 'No argument');
