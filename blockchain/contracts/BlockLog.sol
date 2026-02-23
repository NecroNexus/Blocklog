// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title BlockLog
 * @dev Blockchain-based immutable logging system
 * Stores cryptographic hashes of logs for integrity verification
 */
contract BlockLog {

    struct LogEntry {
        bytes32 logHash;     // Hash of the original log
        uint256 timestamp;  // Time when log was stored
        address logger;     // Address that submitted the log
    }

    // Private storage of logs (immutable once added)
    LogEntry[] private logs;

    // Event emitted whenever a log is added
    event LogAdded(bytes32 logHash, uint256 timestamp, address logger);

    /**
     * @dev Add a log hash to the blockchain
     * @param _logHash Keccak256 hash of the log message
     */
    function addLog(bytes32 _logHash) external {
        logs.push(LogEntry(_logHash, block.timestamp, msg.sender));
        emit LogAdded(_logHash, block.timestamp, msg.sender);
    }

    /**
     * @dev Get a specific log entry by index
     */
    function getLog(uint256 index)
        external
        view
        returns (bytes32 logHash, uint256 timestamp, address logger)
    {
        require(index < logs.length, "Log index out of range");
        LogEntry memory l = logs[index];
        return (l.logHash, l.timestamp, l.logger);
    }

    /**
     * @dev Get total number of logs stored
     */
    function totalLogs() external view returns (uint256) {
        return logs.length;
    }
}