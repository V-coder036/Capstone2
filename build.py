from pybuilder.core import use_plugin, init, task

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

@task
def run():
    from sys import path
    path.append("src/main/python")
    from web import app
    app.run(debug=True, host = '0.0.0.0',port=8000)

name = "g"
default_task = ["publish","run"]


@init
def set_properties(project):
    project.set_property("coverage_exceptions", ['web'])
    project.build_depends_on("tensorflow")
    project.build_depends_on("flask")
    project.build_depends_on("selenium")
    project.build_depends_on("pillow")
