var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://172.27.80.150:8545"));

//var _from = web3.eth.accounts[0];
//let accounts = web3.eth.getAccounts();
//web3.eth.defaultAccount = accounts[0];

var _from = "0xb2b756094dFF19ddF4d426D211bE668DF2B3aec0";

/*
	_to: 从命令行中获取转币地址
	_value: 从命令行中获取转多少币
*/
var arguments = process.argv.splice(2);

if(!arguments || arguments.length != 2){
	console.error("Parameter error!");
	return;
}

var _to = arguments[0];
var _value = arguments[1];

web3.eth.sendTransaction({from: _from, to: _to, value: _value}, (err, res)=>{
	if(!err){
		console.log("Transaction Hash is : ", res);
	}else{
		console.error("Error is : ", err);
	}
});