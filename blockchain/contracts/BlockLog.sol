// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BlockLog {

    struct LogEntry {
        bytes32 logHash;
        uint256 timestamp;
        address logger;
    }

    LogEntry[] private logs;

    event LogAdded(bytes32 logHash, uint256 timestamp, address logger);

    function addLog(bytes32 _logHash) public {
        logs.push(LogEntry(_logHash, block.timestamp, msg.sender));
        emit LogAdded(_logHash, block.timestamp, msg.sender);
    }

    function getLog(uint index) public view returns (bytes32, uint256, address) {
        LogEntry memory l = logs[index];
        return (l.logHash, l.timestamp, l.logger);
    }

    function totalLogs() public view returns (uint) {
        return logs.length;
    }
}