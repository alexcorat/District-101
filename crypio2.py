import os
import asyncio
import aiohttp
import logging
import platform
from datetime import datetime
from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH, TRX
from hdwallet.utils import generate_mnemonic
from rich.logging import RichHandler
from rich import print
import ctypes
import pyfiglet
import time
import sys

# Function to check APIs
async def check_apis(api_endpoints, symbol):
    working_apis = []
    async with aiohttp.ClientSession() as session:
        for endpoint in api_endpoints:
            try:
                async with session.get(endpoint, timeout=10) as response:
                    if response.status == 200:
                        # API is functioning
                        working_apis.append(endpoint)
            except Exception as e:
                logging.error(f"[red]Error checking API {endpoint}: {e}[/red]")
    return working_apis

# Your other functions and code here...

async def main(seed_filename=None):  # Make seed_filename optional with a default value of None
    # Validate activation code before starting the program
    validate_activation()

    working_apis_btc = await check_apis(BTC_API_ENDPOINTS, BTC)
    working_apis_eth = await check_apis(ETH_API_ENDPOINTS, ETH)
    working_apis_trx = await check_apis(TRX_API_ENDPOINTS, TRX)

    if not (working_apis_btc or working_apis_eth or working_apis_trx):
        logging.error("[red]No APIs are currently available.[/red]")
        return

    # The rest of your main function...

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Check if command-line arguments are provided
        seed_filename = sys.argv[1]  # Get the filename from command-line arguments
        asyncio.run(main(seed_filename))  # Run main function with the provided filename
    else:
        asyncio.run(main())  # Run main function without a filename
