import pynecone as pc 
 
def Saving_Account():
    return pc.vstack(
        pc.text("Saveing Account"),
        pc.table_container(
        pc.table(
            headers=["Date", "Num", "Description","Transfer","R","Deposit","Withdrawal","Balance"],
            rows=[
                ("12/04/2566", 1, "ค่าบัตร","Car","n",0,1500,-1500),
            ],
            variant="striped",
        )
    )
)