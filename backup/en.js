/*
    var key = '39383033327777772e313530732e636e';
    key = CryptoJS.enc.Hex.parse(key)
    var enc = CryptoJS.AES.encrypt(title ,key)
    var enced = enc.ciphertext.toString()
*/

var fun1 = require('./myjs');

var title = "张学良";
var key = '39383033327777772e313530732e636e';
//var window = {};
key = fun1.enc.Hex.parse(key);
var enc = fun1.AES.encrypt(title ,key);
var enced = enc.ciphertext.toString();

console.log(enced);