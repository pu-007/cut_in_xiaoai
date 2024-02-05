from apis import bafa
from config import client_id, commands_table


bafa.Bafa(client_id, commands_table).loop_forever()
