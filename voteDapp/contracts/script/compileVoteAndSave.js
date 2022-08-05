const fs = require("fs-extra");
const solc = require("solc");
const path = require("path");
const contractName = "Vote.sol";

const compilePath = path.resolve(__dirname, "../compile");
fs.removeSync(compilePath);
fs.ensureDirSync(compilePath);

var contractPath = path.resolve(__dirname, "../src", contractName);
var contractSource = fs.readFileSync(contractPath, "utf-8");

var input = {
    language: "Solidity",
    sources: {
        "Vote.sol": {
            content: contractSource,
        },
    },
    settings: {
        outputSelection: {
            "*": {
                "*": ["*"],
            },
        },
    },
};

var compileResult = JSON.parse(solc.compile(JSON.stringify(input)));

if (Array.isArray(compileResult.errors) && compileResult.errors.length) {
    throw new Error(compileResult.errors[0]);
}

Object.keys(compileResult.contracts).forEach((_name) => {
    let _contractName = _name.replace(/\.sol$/, "");
    let filePath = path.resolve(compilePath, `${_contractName}.json`);
    fs.outputJSONSync(filePath, compileResult.contracts[_name]);
    console.log(`save compiled contract ${_contractName} to ${filePath}`);
});
