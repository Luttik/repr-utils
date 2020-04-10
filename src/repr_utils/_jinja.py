from jinja2 import Environment, Template, PackageLoader


def get_template(file_name: str) -> Template:
    env = Environment(
        loader=PackageLoader("repr_utils", "templates"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env.get_template(file_name)
