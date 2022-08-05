var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));

const fs = require('fs');
const solc = require('solc');
const path = require('path');
const __dirname = path.resolve();
const contractName = "Vote.sol";

var contractPath = path.resolve(__dirname,'voteDapp\\contracts\\src',contractName);
var contractSource = fs.readFileSync(contractPath,'utf-8');

// var compileResult = solc.compile(contractSource , 1);

var input = {
  language: 'Solidity',
  sources: {
    'Vote.sol': {
      content: contractSource
    }
  },
  settings: {
    outputSelection: {
      '*': {
        '*': ['*']
      }
    }
  }
};

var compileResult = JSON.parse(solc.compile(JSON.stringify(input)));

// console.log(compileResult);

var abi = compileResult.contracts[contractName].Vote.abi;
var byteCode = compileResult.contracts[contractName].Vote.evm.bytecode.object;
// var deployedBytecode = compileResult.contracts['Vote.sol'].Vote.evm.deployedBytecode;
var _from = "0x0c73A6282A0DabaA2Df525e7141B27E4B799B426";
var _gasPrice = 30000000000;
//部署合约
var optionsObject = {from: _from, gasPrice: _gasPrice};
var deployTxObject = {from: _from, gas: 1500000, gasPrice: _gasPrice};
var VoteContract = new web3.eth.Contract(abi);

var candidateNames = ['0x4170706c65000000000000000000000000000000000000000000000000000000', 
                      '0x4f72616e67650000000000000000000000000000000000000000000000000000', 
                      '0x5065617200000000000000000000000000000000000000000000000000000000'];
VoteContract.deploy({
	data: byteCode,
    arguments: [candidateNames]
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

var contractAddress = '0x5518A5d394f5c4df07f59b1A84A76520E15A4ce0';

