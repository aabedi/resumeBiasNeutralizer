// server.js

//Require the db connection
//require( './db' );

// modules =================================================
var express        = require('express');
var app            = express();
var bodyParser     = require('body-parser');
//var cookieParser = require('cookie-parser');
var methodOverride = require('method-override');
var session = require('express-session')
var favicon = require('serve-favicon');
var logger = require('morgan');
var db = require('./config/db');
//db is accessible by db.url

var http = require('http')
var port = process.env.PORT || 1337;

// var PythonShell = require('python-shell');
// var pyshell = new PythonShell('parser.py');




// start app ===============================================
// startup our app at http://localhost:8080
app.listen(port);

// http.createServer(function(req, res) {
//   res.writeHead(200, { 'Content-Type': 'text/plain' });
//   res.end('Hello World\n');
// }).listen(port);

app.get('*', function(req, res) {
  res.sendfile('./public/index.html'); // load our public/index.html file
});
//
// app.get('/parse', function(req, res) {
//   // var PythonShell = require('python-shell');
//   // PythonShell.run('parser.py', function (err) {
//   // if (err) throw err;
//   // console.log('finished');
//   // app.get('/public/js/client.js')
//   res.sendfile('./public/result.html')
//   // });
// });




// view engine setup
// app.set('views', path.join(__dirname, 'views'));
// app.set('view engine', 'ejs');
// app.engine('html', require('ejs').renderFile);


// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error.html', {
      message: err.message,
      error: err
    });
  });
}

// production error handler - no stacktraces leaked to user
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.render('error.html', {
    message: err.message,
    error: {}
  });
});
