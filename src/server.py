from apis import bafa
import config

commands_table = {"on": "run('wol 08:BF:B8:A6:7C:E2')"}

bafa.Bafa(config.client_id, commands_table).loop_forever()
