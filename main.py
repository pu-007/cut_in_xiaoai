from apis import bafa

import config
import secret_envs

bafa.Bafa(secret_envs.BAFA_ID, config.commands_table,
          debug=config.DEBUG).loop_forever()
