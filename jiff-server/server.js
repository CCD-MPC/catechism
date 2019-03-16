var express = require('express');
var app = express();
var http = require('http').Server(app);
var jiff_instance = require('/app/jiff//lib/jiff-server').make_jiff(http, { logs: true });

app.use("/app/jiff//demos", express.static("demos"));
app.use("/app/jiff//lib", express.static("lib"));
app.use("/app/jiff//lib/ext", express.static("lib/ext"));

http.listen(9000, function()
{
	console.log('listening on *:9000');
});

