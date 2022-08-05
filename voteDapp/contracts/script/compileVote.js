const fs = require('fs');
const solc = require('solc');
const path = require('path');
const contractName = "Vote.sol";

var contractPath = path.resolve(__dirname,'..\\src',contractName);
var contractSource = fs.readFileSync(contractPath,'utf-8');

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
var abi = compileResult.contracts[contractName].Vote.abi;
var byteCode = compileResult.contracts[contractName].Vote.evm.bytecode.object;

console.log('ABI IS :' , abi);
console.log('ByteCode IS :' , byteCode);