import pynecone as pc

CheckingAccount =[
                ("12/04/2566", 1, "ค่าเช่ารถ","Car","n",0,1500,-1500),
                ("12/04/2566", 2, "ได้เงินค่าเทอม","Car","n",500,0,-1000),
            ]

def Checking_Account():
    return pc.vstack(
        pc.text("Checking account"),
        pc.table_container(
        pc.table(
            headers=["Date", "Num", "Description","Transfer","R","Deposit","Withdrawal","Balance"],
            rows = CheckingAccount ,
            variant="striped",
        )
    )
    )