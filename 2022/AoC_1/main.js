var fs = require('fs');
fs.readFile('input_ex.txt', function (err, data) {
  if (err) return console.error(err);
  console.log(data.toString());
});



