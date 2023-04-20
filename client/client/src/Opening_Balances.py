import pynecone as pc 

def Opening_Balances():
    return pc.vstack(
        pc.text("Opening Balance")
    )