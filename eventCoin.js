var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://172.27.80.150:8545"));

var _from = '0xb2b756094dff19ddf4d426d211be668df2b3aec0'; // 默认交易发送方，即对合约的调用者
var _to = '0x66b9492d1f68b5e3f03afebf5cc672d0d9ff5472'; // 测试合约时的接收方
var _gasPrice = 2000000000; // 默认交易费用

var abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Sent","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"minter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"send","outputs":[],"stateMutability":"nonpayable","type":"function"}];
var coinContractAddress = '0xD6D8aD30C2EacDd07153bAbd4F76A995c92C2BDe'; // 合约地址
var optionsObject = {from: _from, gasPrice: _gasPrice};

var coinContractInstance = new web3.eth.Contract(abi , coinContractAddress , optionsObject);

/*
事件
*/
coinContractInstance.events.Sent({fromBlock: 'earliest'}, function(error, result){
	console.log(result);
}).on("connected", function(subscriptionId){
	console.log(subscriptionId);
}).on('data', function(result){
	console.log('data ',result.returnValues);
}).on('changed', function(result){
	// 从本地数据库中删除事件
}).on('error', function(error, receipt){
	// 如果交易被网络拒绝并带有交易收据，第二个参数将是交易收据。
});
