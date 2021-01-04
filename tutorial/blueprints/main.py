from flask import Blueprint
from flask_restplus import Api
from tutorial.namespaces.namespacesA import api as ns1
from tutorial.namespaces.namespacesB import api as ns2


blueprint = Blueprint('main', __name__)


main = Api(blueprint)

main.add_namespace(ns1)
main.add_namespace(ns2)