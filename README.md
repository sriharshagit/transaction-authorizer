# transaction-authorizer

This project is hosted at aws and api links are and use post method
for account creation http://ec2-52-66-188-226.ap-south-1.compute.amazonaws.com/account 
for trasaction its http://ec2-52-66-188-226.ap-south-1.compute.amazonaws.com/transaction

my assumptions of this case studies are:-
due to network delay there may be delayed requests, so if a transaction which has timestamp of 10:00:05 seconds arrives first to the server and due to network delay a transaction of timestamp 10:00:00 may arrive to server after above transaction. but we have already commited the first request so for second request we check if this fits in 2 mins interval period if it fits we commit the transaction else we return exception of high frequency.

to run this project make sure python 3 is the environment and install flask, flask-jsonschema-validator and python-dateutil dependencies
and run main.py file

