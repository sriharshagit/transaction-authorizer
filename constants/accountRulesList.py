#import all the business rules for creation of account here
from businessRules.account.isAccountCreated import checkAccountStatus

#below list contains of all the rules in seequential order which we need to check
accountCreationRuleFlow = []

#add all the business rules in sequential order to check one by one
accountCreationRuleFlow.append(checkAccountStatus)