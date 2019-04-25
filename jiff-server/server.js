var express = require('express');
var app = express();
var http = require('http').Server(app);
var jiff_instance = require('/app/jiff//lib/jiff-server').make_jiff(http, { logs: false });

var jiffBigNumberServer = require('/app/jiff/lib/ext/jiff-server-bignumber');
jiff_instance.apply_extension(jiffBigNumberServer);

app.use("/app/jiff//demos", express.static("demos"));
app.use("/app/jiff//lib", express.static("lib"));
app.use("/app/jiff//lib/ext", express.static("lib/ext"));
app.use("/app/jiff/bignumber.js", express.static("node_modules/bignumber.js"));

http.listen(9000, function()
{
	console.log('listening on *:9000');
});

