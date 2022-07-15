// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Vote {
    mapping(bytes32 => uint8) public votesReceived;
    bytes32[] public candidateList;
    constructor(bytes32[] memory candidateNames) {
        candidateList = candidateNames;
    }

    function totalVotesFor(bytes32 candidate) public view returns(uint8) {
        require(validCandidate(candidate), "is not candidate");
        return votesReceived[candidate];
    }

    function voteForCandidate(bytes32 candidate) public {
        require(validCandidate(candidate), "is not candidate");
        votesReceived[candidate] += 1;
    }

    function validCandidate(bytes32 candidate) internal view returns(bool) {
        for(uint i = 0; i <= candidateList.length; i++){
            if(candidate == candidateList[i]){
                return true;
            }
        }
        return false;
    }
}