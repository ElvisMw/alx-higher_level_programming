#!/usr/bin/node
if (process.argv.length === 2) { // 1st & 2nd arguments are for executable path & file path respectively
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
