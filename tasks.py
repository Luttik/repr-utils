from invoke import task


@task(name="make-setup")
def make_setup(c):
    c.run("dephell deps convert")


@task(name="format")
def _format(c):
    c.run("black .")
    c.run("isort -rc .")
