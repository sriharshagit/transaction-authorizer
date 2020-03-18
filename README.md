# transaction-authorizer

This project is hosted at aws and api links are:-

for account creation http://ec2-52-66-188-226.ap-south-1.compute.amazonaws.com/account  method=post

for trasaction its http://ec2-52-66-188-226.ap-south-1.compute.amazonaws.com/transaction method=post

my assumptions of this case studies are:-

all the transaction amounts are positive

due to network delay there may be delayed requests, so if a transaction which has timestamp of 10:00:05 seconds arrives first to the server and due to network delay a transaction of timestamp 10:00:00 may arrive to server after above transaction. but we have already commited the first request so for second request we check if this fits in 2 mins interval period if it fits we commit the transaction else we return exception of high frequency.

to run this project make sure python 3 is the environment and install flask, flask-jsonschema-validator and python-dateutil dependencies
and run main.py file


flow for the project:

api server will start in main.py file and will listen to port 80 

in main.py file exposed to endpoints i.e /account and /transaction and input validation checks for each endpoint is done. input format for each endpoint are in requests folder.

from here control goes to controller folder. for account endpoint the control goes to createAccount.py and for transaction endpoint the control goes to transactionAuthorization.py file in controller folder.

createAccount.py will get array from constants/accountRulesList.py and traverses each rule and calls each rule which returns array. if returned array is empty then we proceed to check other business rule and if returned array has some data(exception) then create account will return response will data. if all business rules returns empty array then commit purpose of api and return success response.

same above follows with transactionAuthorization.py but will get array from constants/transactionRulesList.py

constants folder has 2 files and each file will export endpoint specific business rules which needs to be followed.

constants/accountRulesList.py will export array of business rules which needs to be followed for /account endpoint. accountRulesList.py will pick business rules from businessRules/account and appended in array .

constants/transactionRulesList.py will export array of business rules which needs to be followed for /transaction endpoint. accountRulesList.py will pick business rules from businessRules/transaction and appended in array .

addition or deletion of new business rules which needs to be followed by endpoint can be done by appending or removing business rule from array which is exported by constants folder.

here all the business rules will follow same input and output format. 

input is request object and output is array. array is empty if business rule is followed or array will have exception message in array.

businessRules/account/isAccountCreated.py file will check if account is already created of not, if created this will return expection message in array else will return empty array

businessRules/transaction/checkSccountInitialized.py file will check is active card is true or not, if true will return empty array else will return expection message in array

businessRules/transaction/checkAvailableLimit.py file will check if account holder has sufficient balance for transaction to commit. if has will return empty array else will return exception message in array


businessRules/transaction/checkHighFrequency.py file will check whether given transaction can be performed based on the certain rules associated with timestamp. This check is based upon the business rule stating at most 3 transactions can be performed within 2 minutes of timeframe. Moreover, all the delayed transcation also get accepted if feasible.

    Note: considering 0th based indexing

    Algorithm:
    Append the transaction time to global list

    For first 3 transactions - 
    Accepting all of them without validating against any rule

    For multiple transaction at same timestamp - 
    If already 3 transaction for that particular timestamp exist then it will return violation else it will be treated just like any other transaction.

    For first element -
    If incoming transaction get delays and upon the sorting the list it becomes first element.
    Will check the timestamp difference between element present at 3rd and 0th, if difference is greater than 120 then accpeted otherwise rejected.

    For last element -
    Upon sorting the list, incoming transaction turns out to be last element.
    Will check the timestamp difference between element present at last 3rd and last, if difference is greater than 120 then accpeted otherwise rejected.

    For middle element -
    Upon sorting the list, incoming transaction turns out to be middle element.
    Will check all 4 possible conditions as follows:
    Note: index is index is of the incoming transaction in the list
    1. Difference between element present at (index + 2) and (index - 1), if difference is greater than 120 then will check following possible conditions otherwise rejected.
    2. Difference between element present at (index + 1) and (index - 2), if difference is greater than 120 then will check following possible conditions otherwise rejected.
    3. Difference between element present at (index + 3) and (index), if difference is greater than 120 then will check following possible conditions otherwise rejected.
    4. Difference between element present at (index) and (index - 3), if difference is greater than 120 then accepted otherwise rejected.

    In the final step, for each transaction irrespective of getting accepted or rejected, input transaction time is removed from the global list.

    Parameter:
    request object

    Return:
    Response array containing feasibility of the transaction, if possible then empty array else an array containing particular violation


businessRules/transaction/checkSimilarTransaction.py file will check whether given transaction can be performed based on the similarities between two transactions. The business rule associated with this function states no two similar transaction can be performed within 2 minutes of timeframe. Here, similar transaction refers to transactions having same merchant and same amount.

    Algorithm:

    Traverse the dictionary containing all the previous transaction and get the new list of transaction occurred between timeframe of 2 minutes wrt incoming transaction time.

    Validate all the transactions present in the new list with incoming transaction and if two transactions are found to be similar returns rejected otherwise accecpted.

    Parameter:
    request object

    Return:
    Response array containing feasibility of the transaction, if possible then empty array else an array containing particular violation
