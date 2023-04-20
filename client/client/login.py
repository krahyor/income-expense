import pynecone as pc
import requests
import json

app = pc.App(
    stylesheets=[
        "https://fonts.google.com/share?selection.family=Silkscreen",
    ],
)

def login():
    return pc.vstack(
        pc.text("Hello Again", font_size="5em",font_family="Silkscreen"),
        pc.text("Welcome back to ...", font_size="2em",font_family="Silkscreen",),
        pc.input(placeholder="Username",width="300px",),
        pc.input(placeholder="Password",width="300px",type_="Password"),
        pc.link(
        pc.button("Login",bg="lightblue",size="sm"),href = "/home"
        ),
        pc.link(
            pc.button("Signup",bg="lightblue",size="sm"),href = "/signin"
        )
    )
    