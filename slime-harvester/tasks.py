from invoke.tasks import task


@task
def start(ctx):

    ctx.run("python src/index.py")


@task
def test(ctx):
    ctx.run("pytest src/tests")


@task
def coverage_report(ctx):
    ctx.run("coverage run -m pytest src/tests")
    ctx.run("coverage report -m")
    ctx.run("coverage html")

@task(name="coverage")
def coverage_alias(ctx):
    coverage_report(ctx)


@task
def lint(ctx):
    ctx.run("pylint src --init-hook=\"import sys; sys.path.insert(0, 'src')\"")