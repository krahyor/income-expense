import pynecone as pc



def home():
    return pc.box(
        
        pc.menu(
        pc.menu_button("MENU"),
        pc.menu_list(
            pc.menu_button("Assets"),
            pc.menu_list(
                pc.link("Cash in Wallet", href = "/cashinwallet"),
                pc.menu_divider(),
                pc.link("Checking Account",href = "/checkingaccount"),
                pc.menu_divider(),
                pc.link("Saving Account",href ="/saveaccount"),         
                ),
            pc.menu_button("Equity"),
            pc.menu_list(
                pc.link("Opening Balances",href ="/openingbalance"),
                ),
            pc.menu_button("Liabilitie"),
            pc.menu_list(
                pc.link("Credit Card",href = "/creditcard"),
            ),
        ),
    ),
    pc.vstack(
        pc.text("Dashboard"),
        pc.box(
            "+150",
            bg="yellow",
            border_radius="sm",
            width="20%",
        ),
        pc.text("Assets"),
        pc.box(
            "+150",
            bg="blue",
            border_radius="sm",
            width="20%",
            front_position = "center",
        ),
        pc.text("Equity"),
        pc.box(
            "+1000",
            bg="pink",
            border_radius="sm",
            width="20%",
        ),
        pc.text("Liabilitie"),
        )
    )