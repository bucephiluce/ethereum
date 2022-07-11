var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://172.27.80.150:8545"));

//var _from = web3.eth.accounts[0];
let accounts = await web3.eth.getAccounts();
web3.eth.defaultAccount = accounts[0];

var _from = accounts[0];
var _to = "0x66b9492d1f68b5e3f03afebf5cc672d0d9ff5472";

var _value = 5000000000;

web3.eth.sendTransaction({from: _from, to: _to, value: _value}, (err, res)=>{
	if(!err){
		console.log("Result is : ", res);
	}else{
		console.error("Error is : ", err);
	}
});