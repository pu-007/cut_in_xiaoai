from typing import Callable
import paho.mqtt.client as mqtt
import logging
from time import strftime
from os import chdir
from pathlib import Path


class Bafa(mqtt.Client):

    def __init__(self, client_id: str, commands_table: dict[str, Callable],
                 debug: bool) -> None:
        chdir(str(Path(__file__).parents[2]))
        Path("./logs").mkdir(exist_ok=True)
        logging.basicConfig(
            filename=f"logs/{strftime('%Y%m%d')}.log",
            level=logging.DEBUG if debug else logging.INFO,
            format=
            "%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        logging.basicConfig()
        super().__init__(mqtt.CallbackAPIVersion.VERSION1, client_id)
        self.commands_table = commands_table
        self.username_pw_set("userName", "passwd")
        self.connect("bemfa.com", 9501, 60)

    def on_connect(self, client, userdata, flags, rc):
        logging.debug(f"Connected with result code `{rc}`")
        self.subscribe("PC002")

    def on_message(self, client, userdata, msg):
        trigger = str(msg.payload.decode("utf-8"))
        logging.debug(f"Trigger by `{trigger}`")
        try:
            command = self.commands_table[trigger]
            logging.debug(f"Run `{command}`")
            command()
        except KeyError:
            logging.warning(f"Trigger `{trigger}` is not registered")

    def on_subscribe(self, client, userdata, mid, granted_qos):
        logging.debug(f"On Subscribed: qos = {granted_qos}")

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            logging.error(f"Unexpected disconnection `{rc}`")
