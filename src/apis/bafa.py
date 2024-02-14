from typing import Callable
import paho.mqtt.client as mqtt
import logging
from time import time
from os import chdir
from pathlib import Path

# functions for string commands
from os import system as run


class Bafa(mqtt.Client):
    def __init__(
        self, client_id: str, commands_table: dict[str, str | Callable]
    ) -> None:
        chdir(str(Path(__file__).parents[2]))
        Path("./logs").mkdir(exist_ok=True)
        logging.basicConfig(
            filename="logs/bafa.log",
            level=logging.INFO,
            format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        logging.basicConfig()
        super().__init__(client_id)
        self.commands_table = commands_table
        self.username_pw_set("userName", "passwd")
        self.connect("bemfa.com", 9501, 60)

    def on_connect(self, client, userdata, flags, rc):
        logging.info(f"Connected with result code `{rc}`")
        self.subscribe("PC002")

    def on_message(self, client, userdata, msg):
        trigger = str(msg.payload.decode("utf-8"))
        logging.info(f"Trigger by `{trigger}`")
        try:
            command = self.commands_table[trigger]
            if callable(command):
                command()
            else:
                eval(command)
            logging.info(f"Run `{command}`")
        except KeyError:
            logging.warning(f"Trigger `{trigger}` is not registered")

    def on_subscribe(self, client, userdata, mid, granted_qos):
        logging.info(f"On Subscribed: qos = {granted_qos}")

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            logging.error(f"Unexpected disconnection `{rc}`")
