import pynecone as pc
import requests
import json

def Cash_in_Wallet():

    api_response = requests.get("http://localhost:8080/cash")
    data = api_response.text
    parse_json = json.loads(data)
    print(parse_json["data"])


    return pc.vstack(
        pc.text("Cash in Wallet"),
        pc.table_container(
        pc.table(
            headers=["Date", "Num", "Description","Transfer","R","Receive","Spend","Balance"],
            rows=[
                (parse_json["data"], parse_json["Num"], parse_json["Description"],parse_json["Transfer"],parse_json["R"],parse_json["Receive"],parse_json["Spend"],parse_json["Receive"]),
                (parse_json["data"], parse_json["Num"], parse_json["Description"],parse_json["Transfer"],parse_json["R"],parse_json["Receive"],parse_json["Spend"],parse_json["Receive"]),

            ],
            variant="striped",
        ),
    )
    )