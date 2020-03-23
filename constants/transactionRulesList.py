#import all the business rules for transactions
from businessRules.transaction.checkAccountInitialized import checkCardActiveStatus
from businessRules.transaction.checkAvailableLimit import checkAccountBalance
from businessRules.transaction.checkHighFrequency import checkTimeWindow
from businessRules.transaction.checkSimilarTransaction import checkDoubledTransaction

#below list contains of all the business rules in seequential order which we need to validate
transactionRuleFlow = []

#add all required rules are appended insequential order and any rule which is not requied can ignore by not appending
transactionRuleFlow.append(checkCardActiveStatus)
transactionRuleFlow.append(checkAccountBalance)
transactionRuleFlow.append(checkTimeWindow)
transactionRuleFlow.append(checkDoubledTransaction)