import jsonschema
from flask import Response
from flask import Flask, request
from flask_jsonschema_validator import JSONSchemaValidator

app = Flask(__name__)
JSONSchemaValidator( app = app, root = "../requests" )

@app.route("/account", methods=["POST"])
@app.validate( 'createAccount', 'createrequest' )
def hello():
    print(request.json)
    return "request came successfully"

@app.route("/transaction",methods=["POST"])
@app.validate('makeTransaction','transactionrequest')
def vv():
    print(request.json)
    return "transact request"

@app.errorhandler( jsonschema.ValidationError )
def onValidationError( e ):
  return Response( "There was a validation error: " + str( e ), 400 )

app.run(debug=True)