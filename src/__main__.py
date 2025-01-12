from apis import bafa
import config

bafa.Bafa(config.client_id, config.commands_table).loop_forever()
