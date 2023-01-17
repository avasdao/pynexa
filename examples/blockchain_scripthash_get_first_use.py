#!/usr/bin/env python3
import pynexa

from pynexa.rostrum import Rostrum
from pynexa.rostrum.svr_info import ServerInfo
from pynexa.core import CBlockHeader, x
from pynexa.wallet import CBitcoinAddress
import asyncio

pynexa.SelectParams("testnet")
scripthash = CBitcoinAddress("bchtest:qq2ckhgcz4fvna8jvlqdu692ujtrqsue8yarpm648v").to_scriptHash()

async def rostrum_stuff():
    cli = Rostrum()

    await cli.connect(ServerInfo("localhost", hostname="localhost", ports=["t60001"]))

    print(await cli.RPC('blockchain.scripthash.get_first_use', scripthash))

    await cli.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(rostrum_stuff())
loop.close()
