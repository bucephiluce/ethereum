var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://172.27.80.150:8545"));

var _from = '0xb2b756094dff19ddf4d426d211be668df2b3aec0'; // 默认交易发送方，即对合约的调用者
var _to = '0x66b9492d1f68b5e3f03afebf5cc672d0d9ff5472'; // 测试合约时的接收方
var _gasPrice = 2000000000; // 默认交易费用
var _amount = 5000000000;

var abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Sent","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"minter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"send","outputs":[],"stateMutability":"nonpayable","type":"function"}];
var coinContractAddress = '0xD6D8aD30C2EacDd07153bAbd4F76A995c92C2BDe'; // 合约地址
var optionsObject = {from: _from, gasPrice: _gasPrice};

var coinContractInstance = new web3.eth.Contract(abi , coinContractAddress , optionsObject);

// 调用合约的balances 
coinContractInstance.methods.balances(_from).call(optionsObject).then(console.log);
coinContractInstance.methods.balances(_to).call(optionsObject).then(console.log);

// 调用合约的send
coinContractInstance.methods.send(_to, _amount).send(optionsObject,function(error, transactionHash){
	if(!error)
		console.log('TransactionHash IS 1: ' , transactionHash);
}).on('transactionHash' , function(transactionHash){
	console.log('TransactionHash IS 2: ' , transactionHash);
}).on('confirmation', function(confirmationNumber, receipt){
	console.log('ConfirmationNumber : %s  ; Receipt IS2 : %o' , confirmationNumber , receipt);
}).on('receipt', function(receipt){
	console.log('Receipt IS1 : ' , receipt);
}).on('error', function(error, receipt){ 
	console.error('Receipt IS Error : ' , receipt);
}).then(function(receipt){
	console.log('Receipt IS3 : ' , receipt);
});

/*
estimateGas
*/
var _gasAmount = 5000000;
var _gasOptions = {from: _from, gas: _gasAmount};

coinContractInstance.methods.send(_to, _amount).estimateGas(_gasOptions).then(function(gasAmount){
	console.log('Estimate Gas IS : %i , My Gas IS %i', gasAmount , _gasAmount);
}).catch(function(error){
	console.error;
});

/*
事件
*/
var _event = 'Sent';
coinContractInstance.once(_event, {fromBlock:0}, function(error, event){
	console.log(event);
});

coinContractInstance.events.Sent({fromBlock: 'earliest'}, function(error, event){
	console.log(event);
}).on("connected", function(subscriptionId){
	console.log(subscriptionId);
}).on('data', function(event){
	console.log(event);
}).on('changed', function(event){
	// 从本地数据库中删除事件
}).on('error', function(error, receipt){
	// 如果交易被网络拒绝并带有交易收据，第二个参数将是交易收据。
});

coinContractInstance.getPastEvents(_event, {fromBlock: 0, toBlock: 'latest'}/*, function(error, events){
	console.log(events);
}*/).then(function(events){
	console.log(events) // same results as the optional callback above
});

/*
订阅日志
*/
var subscription = web3.eth.subscribe('logs', {
	address: coinContractAddress,
	fromBlock: 0
}, function(error, result){
	if(!error)
		console.log(result);
}).on("connected", function(subscriptionId){
    console.log(subscriptionId);
}).on("data", function(log){
    console.log(log);
}).on("changed", function(log){
});

// 取消订阅
subscription.unsubscribe(function(error, success){
    if(success)
        console.log('Successfully unsubscribed!');
});