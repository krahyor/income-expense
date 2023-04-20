import pynecone as pc


def signin():
    return pc.vstack(
        pc.image(src_set = "/r202.png",width="100px",height="auto"),
        pc.text("Signin", font_size="5em"),
        pc.input(placeholder="Username",width="300px"),
        pc.input(placeholder="Password",width="300px",type_="Password"),
        pc.button("signin",bg="lightblue",size="sm"),
    )