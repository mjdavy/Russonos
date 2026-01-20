import asyncio
import logging

from aiorussound.connection import RussoundTcpConnectionHandler
from aiorussound.rio import RussoundClient


async def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    )

    connection = RussoundTcpConnectionHandler("192.168.1.213", 9621)
    client = RussoundClient(connection)

    await client.connect()
    await client.load_zone_source_metadata()

    print("RIO version:", client.rio_version)
    print("Controllers:", list(client.controllers.keys()))

    for controller_id, controller in client.controllers.items():
        print(f"Controller {controller_id} type={controller.controller_type} zones={len(controller.zones)}")
        for zone_id, zone in controller.zones.items():
            print(f"  Zone {zone_id}: name={zone.name} status={zone.status} source={zone.current_source}")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
