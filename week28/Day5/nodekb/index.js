const express = require("express");
const { append } = require("vary");
const index =express();
index.get('/', function(req, res){
    res.send("Hellow world");
})
index.listen(3000,function(){
    console.log('Server started on port 3000')

})