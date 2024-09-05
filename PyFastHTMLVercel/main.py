from fasthtml.common import *
app, rt = fast_app()

# @rt('/change')
# def get():
#     return P('Nice to be here!')

@rt('/change')
def get():
    return Titled("Change", P('Nice to be here!'), A("Go Back to Home",href = "/"))


# @rt('/')
# def get():
#     return Titled(Div(P('Hello World!'), hx_get = "/change"))

# @rt('/')
# def get():
#     return Titled(Div(P('Hello World!')), P(A("Link", href = "/change")))

# def render_message(entry):
#     return (
#         Article(
#             Header("Name : Sven"),
#             P("Message"),
#             Footer(Small(Em("Posted: now"))),
#         ),
#     )

def render_message(entry):
    return (
        Article(
            Header(f"Name : {entry['name']}"),
            P(entry['message']),
            Footer(Small(Em(f"Posted: {entry['timestamp']}"))),
        ),
    )

def render_message_list():
     messages = [
         {"name": "Peter", "message": "Hi there", "timestamp": "now"},
         {"name": "John", "message": "cool", "timestamp": "yesterday"},
     ]
     return Div(
         *[render_message(entry) for entry in messages],
        )


# def render_message_list():
#     messages = [
#         {"Name":"Peter" }
#     ]

def render_content():
    form = Form(
        Fieldset(
            Input(
                type = "text",
                name = "name",
                placeholder = "Name",
                required = "True",
                maxlength = 15
            ),
            Input(
                type="text",
                name="message",
                placeholder="Message",
                required="True",
                maxlength=50
            ),
            Button("Submit", type="Submit"),
            role = "group",
        )
    )
    return Div(
        P(Em('Write Something Nice!')),
        # P("Our form will be here..."),
        form,
        Div(
            "Made With Heart by ",
            A("Sven", href="https://www.youtube.com/watch?v=_o31SB3NLFk", target = "_blank"),
        ),
        Hr(),
        # P("The Messages will be displayed here...")
        render_message_list()

    )


@rt('/')
def get():
    return Titled(Div(P('Hello World!')), render_content())

serve()