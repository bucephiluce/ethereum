var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://172.27.80.150:8545"));

/*
部署合约的准备工作：
*/
var _abi=[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Sent","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"minter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"send","outputs":[],"stateMutability":"nonpayable","type":"function"}];

var CoinContract = new web3.eth.Contract(_abi);

var byteCode='0x'+'608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555061057c806100606000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c8063075461721461005157806327e235e31461006f57806340c10f191461009f578063d0679d34146100bb575b600080fd5b6100596100d7565b604051610066919061033d565b60405180910390f35b61008960048036038101906100849190610389565b6100fb565b60405161009691906103cf565b60405180910390f35b6100b960048036038101906100b49190610416565b610113565b005b6100d560048036038101906100d09190610416565b6101c5565b005b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60016020528060005260406000206000915090505481565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461016b57600080fd5b80600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546101ba9190610485565b925050819055505050565b600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205481111561021157600080fd5b80600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825461026091906104db565b9250508190555080600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282546102b69190610485565b925050819055507f3990db2d31862302a685e8086b5755072a6e2b5b780af1ee81ece35ee3cd33453383836040516102f09392919061050f565b60405180910390a15050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000610327826102fc565b9050919050565b6103378161031c565b82525050565b6000602082019050610352600083018461032e565b92915050565b600080fd5b6103668161031c565b811461037157600080fd5b50565b6000813590506103838161035d565b92915050565b60006020828403121561039f5761039e610358565b5b60006103ad84828501610374565b91505092915050565b6000819050919050565b6103c9816103b6565b82525050565b60006020820190506103e460008301846103c0565b92915050565b6103f3816103b6565b81146103fe57600080fd5b50565b600081359050610410816103ea565b92915050565b6000806040838503121561042d5761042c610358565b5b600061043b85828601610374565b925050602061044c85828601610401565b9150509250929050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6000610490826103b6565b915061049b836103b6565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff038211156104d0576104cf610456565b5b828201905092915050565b60006104e6826103b6565b91506104f1836103b6565b92508282101561050457610503610456565b5b828203905092915050565b6000606082019050610524600083018661032e565b610531602083018561032e565b61053e60408301846103c0565b94935050505056fea26469706673582212200d73793e1a67ce74b85a63813b665dc2ca67fd61d3526ac887c144444a624e7264736f6c634300080f0033';

var deployTxObject = {from: "0xb2b756094dff19ddf4d426d211be668df2b3aec0", gas: 1500000, gasPrice: '30000000000'};

/*
开始部署合约：
*/
CoinContract.deploy({
	data: byteCode
}).send(deployTxObject,(error,transactionHash)=>{
	if(!error){
		console.log("TransactionHash 1 :", transactionHash)
	}
}).on('error', function(error){
	console.error()
}).on('transactionHash',function(transactionHash){
	console.log("TransactionHash 2:", transactionHash)
}).on('receipt', function(receipt){
	console.log('Contract Address IS(receipt) :', receipt.contractAddress)
}).on('confirmation',function(confirmationNumber, receipt){
	console.log('ConfirmationNumber : %i ; Contract Address IS : %s', confirmationNumber, receipt.contractAddress)
}).then(function(newContractInstance){
	console.log('Contract Address IS(newContractInstance): ', newContractInstance.options.address)
});

/*
执行之后的返回值：
TransactionHash : 0x248649983b9eb93de20cc1f1ee6f00ecc2b90c2bef562d98ff148d889a6f5b5d
TransactionHash : 0x248649983b9eb93de20cc1f1ee6f00ecc2b90c2bef562d98ff148d889a6f5b5d
0xD6D8aD30C2EacDd07153bAbd4F76A995c92C2BDe
0xD6D8aD30C2EacDd07153bAbd4F76A995c92C2BDe
confirmationNumber : 1 ; Contract Address IS :0xD6D8aD30C2EacDd07153bAbd4F76A995c92C2BDe
*/

/*
开始调用合约：
*/
var coinContractAddress = '0xD6D8aD30C2EacDd07153bAbd4F76A995c92C2BDe'; // 合约地址
var from = '0xb2b756094dff19ddf4d426d211be668df2b3aec0'; // 默认交易对象
var _gasPrice = 20000000000; // 默认交易费用
CoinContract = new web3.eth.Contract(_abi, coinContractAddress, {from: from, gasPrice: _gasPrice});

var BigNumber = require('bignumber.js');
var amount = new BigNumber('135456432156465841321654654156265');

CoinContract.methods.mint(from, amount).send({from:from}).then(function(receipt){console.log(receipt)});

/*
执行之后的输出结果：
{
  blockHash: '0xb18972732f711424d4c044d157a8ebfc98886e5571a8dcd83d76cd99380647aa',
  blockNumber: 8,
  contractAddress: null,
  cumulativeGasUsed: 46956,
  effectiveGasPrice: 20000000000,
  from: '0xb2b756094dff19ddf4d426d211be668df2b3aec0',
  gasUsed: 46956,
  logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
  status: true,
  to: '0xd6d8ad30c2eacdd07153babd4f76a995c92c2bde',
  transactionHash: '0x87708a85a4efe0a3ad541cd72e407614578ced35973f305961cecb677f44953b',
  transactionIndex: 0,
  type: '0x0',
  events: {}
}
confirmationNumber : 2 ; Contract Address is :0xD6D8aD30C2EacDd07153bAbd4F76A995c92C2BDe
*/

CoinContract.methods.balances(from).call({from:from}).then(console.log);

/*
Promise {
  <pending>,
  [Symbol(async_id_symbol)]: 169745,
  [Symbol(trigger_async_id_symbol)]: 169742,
  [Symbol(destroyed)]: { destroyed: false }
}
> 135456432156465841321654654156265
*/