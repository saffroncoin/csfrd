import sys
import os

"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 42
VERSION_REVISION = 0
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# SFRDirect protocol
TXTYPE_FORMAT = '>I'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 4 * 2016   # Two months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Bitcoin Core
OP_RETURN_MAX_SIZE = 80 # bytes


# Currency agnosticism
BTC = 'BTC'
XCP = 'cSFR'

BTC_NAME = 'Saffroncoin'
BTC_CLIENT = 'saffroncoind'
XCP_NAME = 'SFRDirect'
XCP_CLIENT = 'csfrd'

DEFAULT_RPC_PORT_TESTNET = 49710
DEFAULT_RPC_PORT = 39710

DEFAULT_BACKEND_RPC_PORT_TESTNET = 29716
DEFAULT_BACKEND_RPC_PORT = 19710

UNSPENDABLE_TESTNET = 'STEStYMu2aumYr3Y92yrJiBdya518bojJZ'
UNSPENDABLE_MAINNET = 'SaFFuJKbA91NPwiNfrf17MctVFtG96tGLn'

ADDRESSVERSION_TESTNET = b'\x3f'
# PRIVATEKEY_VERSION_TESTNET =
ADDRESSVERSION_MAINNET = b'\x3f'
# PRIVATEKEY_VERSION_MAINNET =
MAGIC_BYTES_TESTNET = b'\x01\xf5\x55\xa4'   # For bip-0010
MAGIC_BYTES_MAINNET = b'\xcf\x05\x67\xea'   # For bip-0010


BLOCK_FIRST_TESTNET_TESTCOIN = 205530
BURN_START_TESTNET_TESTCOIN = 225260
BURN_END_TESTNET_TESTCOIN = 4017708     # Fifty years
BLOCK_FIRST_TESTNET = 205530
BURN_START_TESTNET = 225260
BURN_END_TESTNET = 4017708              # Fifty years

BLOCK_FIRST_MAINNET_TESTCOIN = 205530
BURN_START_MAINNET_TESTCOIN = 225260
BURN_END_MAINNET_TESTCOIN = 2500000     # A long time.

BLOCK_FIRST_MAINNET = 205530
BURN_START_MAINNET = 225260
BURN_END_MAINNET = 330500


# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in csfrblockd/lib/config.py as well
    # TODO: This should be updated, given their new configurability.
# TODO: The dust values should be lowered by 90%, once transactions with smaller outputs start confirming faster: <https://github.com/mastercoin-MSC/spec/issues/192>
DEFAULT_REGULAR_DUST_SIZE = 5430         # TODO: This is just a guess. I got it down to 5530 satoshis.
DEFAULT_MULTISIG_DUST_SIZE = 7800        # <https://bitcointalk.org/index.php?topic=528023.msg7469941#msg7469941>
DEFAULT_OP_RETURN_VALUE = 0
DEFAULT_FEE_PER_KB = 20000                # Bitcoin Core default is 10000.  # TODO: Lower 10x later, too.


# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%
