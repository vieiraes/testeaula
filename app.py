#DO aruivo tal, importe o objeto funcao, variavel 
from users import *
from wallets import *

## MONTAR O OBJETO FINAL E EXEUTAR NO TERMINAL
objeto_final = {
    "brenno":{
        "user": user_brenno,
        "wallet": wallet_BRL}
    },{
        "jhon":{
            "user": user_jhon,
            "wallet": wallet_USD,
        }
    },{
        "pedro": {
            "user": user_pedro,
            "wallet": wallet_BTC,
        }
    }


print("OBJETO", objeto_final)