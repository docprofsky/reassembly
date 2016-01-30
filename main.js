var express = require('express');
var app = express();

var bodyParser = require('body-parser')
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({
  extended: true
}));

app.post('/compile', function (req, res) {
  console.log('Code: ', req.body.code);
  res.sendFile(__dirname + '/index.html');
});

app.use('/', express.static(__dirname));
app.listen(3000, function() { console.log('listening')});