import pynecone as pc
from .login import login
from .home import home
from .singin import signin
from .src.Cash_in_Wallet import Cash_in_Wallet
from .src.Checking_Account import Checking_Account
from .src.Saving_Account import Saving_Account
from .src.Opening_Balances import Opening_Balances
from .src.Credit_Card import Credit_Card


app = pc.App()
app.add_page(login,route="/")
app.add_page(home)
app.add_page(signin)
app.add_page(Cash_in_Wallet,route ="/cashinwallet")
app.add_page(Checking_Account,route ="/checkingaccount")
app.add_page(Saving_Account,route ="/saveaccount")
app.add_page(Opening_Balances,route ="/openingbalance")
app.add_page(Credit_Card,route = "/creditcard")
app.compile()