const csv = require("csvtojson");
const request = require('request');
// Convert a csv file with csvtojson
csv().fromStream(request.get('https://fileas.csv'))
  	.then(function(jsonArrayObj){
  		//when parse finished, result will be emitted here.
    	console.log(jsonArrayObj); 
 	});