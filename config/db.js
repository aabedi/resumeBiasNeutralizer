// config/db.js
/*
This document is responsible for:
    1) setting up the mongo schema
    2) connecting to the DB
The document will create schema
*/

var mongoose = require('mongoose');
var Schema   = mongoose.Schema;

module.exports = {
    url : 'mongodb://user:password@ds019054.mlab.com:19054/biasneutralizer'
}

var ResumeTextFile = new Schema({
	name: {type: String, required: true},
  student_id: {type: Number, required: true},
	text: {type: String, required: true}
});

// var ResumeCandidateRelation = new Schema({
//   name: {type: String, required: true},
//   student_id: { type: Number, required: true}
// });

var Candidate = new Schema({
	_id: { type: Number, required: true},
	first_name: { type: String, required: true},
	last_name: { type: String, required: true},
	school: { type: String, required: true},
  major: { type: String},
	gpa: { type: String},
  experience: {type: String},
	skills: { type: Array},
  charged_Words: { type: Array},
  score: { type: Number}
})
