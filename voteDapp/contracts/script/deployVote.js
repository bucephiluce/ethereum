const Web3 = require("web3");
const web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
const path = require("path");

const filePath = path.resolve(__dirname, "../compile/Vote.json");
const voteObject = require(filePath);
const abi = voteObject.Vote.abi;
const byteCode = voteObject.Vote.evm.bytecode.object;

(async () => {
    let accounts = await web3.eth.getAccounts();
    let candidateNames = [web3.utils.utf8ToHex("Tom"), web3.utils.utf8ToHex("Bob"), web3.utils.utf8ToHex("Jim")];

    console.time("deploy time : ");
    let result = await new web3.eth.Contract(abi)
        .deploy({ data: byteCode, arguments: [candidateNames] })
        .send({ from: accounts[0], gas: 1500000 });
    console.timeEnd("deploy time : ");

    console.log("Contract Address : ", result.options.address);
})();
