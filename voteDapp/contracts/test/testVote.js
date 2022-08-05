const path = require("path");
const assert = require("assert");
const ganache = require("ganache-cli");
const Web3 = require("web3");
const web3 = new Web3(ganache.provider());

const filePath = path.resolve(__dirname, "../compile/Vote.json");
const voteObject = require(filePath);
const abi = voteObject.Vote.abi;
const byteCode = voteObject.Vote.evm.bytecode.object;

let accounts;
let contract;
const candidateNames = [web3.utils.utf8ToHex("Tom"), web3.utils.utf8ToHex("Bob"), web3.utils.utf8ToHex("Jim")];

describe("#Vote", () => {
    // 每次跑单测时需要部署全新的合约实例，起到隔离的作用

    before(async () => {
        console.log("合约测试开始");
        accounts = await web3.eth.getAccounts();
        console.time("deploy contract time : ");
        contract = await new web3.eth.Contract(abi)
            .deploy({ data: byteCode, arguments: [candidateNames] })
            .send({ from: accounts[0], gas: 1500000 });
        console.timeEnd("deploy contract time : ");

        console.log("Contract Address : ", contract.options.address);
    });
    beforeEach(() => {
        console.log("每个测试开始");
    });
    after(() => {
        console.log("合约测试结束");
    });
    afterEach(() => {
        console.log("每个测试结束");
    });
    // 编写单元测试
    it("deployed contract is ok ", () => {
        assert.ok(contract.options.address);
    });

    it("vote sucess Tom has 1", async () => {
        let candidate = web3.utils.utf8ToHex("Tom");
        await contract.methods.voteForCandidate(candidate).send({ from: accounts[0], gasPrice: 30000000 });
        let voteNum = await contract.methods.totalVotesFor(candidate).call();
        assert.equal(voteNum, 1);
    });
});
