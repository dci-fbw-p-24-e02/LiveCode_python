# Task 1

def make_bold(func):
    """Wrap the text output with a <strong> tag."""
    def inner():
        return "<strong>" + func() + "</strong>"
    return inner


@make_bold
def get_html_greeting():
    """Return a greeting in HTML format."""
    return f"Hello, World!"


# print(get_html_greeting())


# Task 2

def make_bold(func):
    """Wrap the text output with a <strong> tag."""
    def inner(*args, **kwargs):
        return "<strong>" + func(*args, **kwargs) + "</strong>"
    return inner

@make_bold
def get_custom_html_greeting(first, last):
    """Return a custom greeting in HTML format."""
    return f"Hello, {first} {last}!"


# print(get_custom_html_greeting("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))
# print(get_html_greeting())


# Task 3

def make_italics(func):
    """Wrap the text in an <em> tag."""
    def inner(*args, **kwargs):
        return "<em>" + func(*args, **kwargs) + "</em>"
    return inner

def make_paragraph(func):
    """Wrap the text in a <p> tag."""
    def inner(*args, **kwargs):
        return "<p>" + func(*args, **kwargs) + "</p>"
    return inner

@make_bold
def get_full_name(first, last):
    """Return the full name of a person."""
    return f"{first} {last}"

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    """Return a custom greeting in HTML format."""
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"


# print(get_custom_html_greeting("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))


# Task 4

def wrap_with(tag="div"):
    """Wrap the text in an HTML tag."""
    def decorator(func):
        def inner(*args, **kwargs):
            return f"<{tag}>" + func(*args, **kwargs) + f"</{tag}>"
        return inner
    return decorator


@wrap_with(tag="strong")
def get_full_name(first, last):
    """Return the full name of a person."""
    return f"{first} {last}"


@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    """Return a custom greeting in HTML format."""
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
