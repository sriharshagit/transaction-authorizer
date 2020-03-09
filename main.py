import jsonschema
from flask import Response
from flask import Flask, request
from flask_jsonschema_validator import JSONSchemaValidator
from controller.createAccount import accountCreate
from controller.transactionAuthorization import makeTrasact

app = Flask(__name__)
JSONSchemaValidator( app = app, root = "requests" )

@app.route("/account", methods=["POST"])
@app.validate( 'createAccount', 'createrequest' )
def crea():
    a = accountCreate(request.json)
    return a

@app.route("/transaction",methods=["POST"])
@app.validate('makeTransaction','transactionrequest')
def trans():
    b = makeTrasact(request.json)
    return b

@app.errorhandler( jsonschema.ValidationError )
def onValidationError( e ):
  return Response( "There was a validation error: " + str( e ), 400 )

#app.run(debug=True)
app.run(host="0.0.0.0", port=8080, debug=True)