# https://buwizz.com/BuWizz_3.0_API_3.6_web.pdf
import time
import asyncio
import logging

from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

logger = logging.getLogger(__name__)

#TODO: https://github.com/hbldh/bleak/blob/master/examples/uart_service.py
# Get down to each GATT Characteristic and start playing

async def discover_buwizz_devices():
    print("scanning for 5 seconds, please wait...")

    devices = await BleakScanner.discover(
        return_adv=True, cb=dict(use_bdaddr=True)
    )

    return [(d, a) for d, a in devices.values() if d.name and "buwizz" in d.name.lower()]

async def scan_device_services(device: BLEDevice, advertisement_data: AdvertisementData):
    logger.info("connecting to device...")

    async with BleakClient(
        device,
        services=advertisement_data.service_uuids,
    ) as client:
        logger.info("connected")

        for service in client.services:
            logger.info("[Service] %s", service)

            for char in service.characteristics:
                if "read" in char.properties:
                    try:
                        value = await client.read_gatt_char(char.uuid)
                        logger.info(
                            "  [Characteristic] %s (%s), Value: %r",
                            char,
                            ",".join(char.properties),
                            value,
                        )
                    except Exception as e:
                        logger.error(
                            "  [Characteristic] %s (%s), Error: %s",
                            char,
                            ",".join(char.properties),
                            e,
                        )

                else:
                    logger.info(
                        "  [Characteristic] %s (%s)", char, ",".join(char.properties)
                    )

                for descriptor in char.descriptors:
                    try:
                        value = await client.read_gatt_descriptor(descriptor.handle)
                        logger.info("    [Descriptor] %s, Value: %r", descriptor, value)
                    except Exception as e:
                        logger.error("    [Descriptor] %s, Error: %s", descriptor, e)

        logger.info("disconnecting...")

    logger.info("disconnected")


async def main():
    buwizz_devices = await discover_buwizz_devices()
    for d, a in buwizz_devices:
        await scan_device_services(d, a)

    

if __name__ == "__main__":
    log_level = logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
    )

    asyncio.run(main())