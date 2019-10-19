# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
    count = 0
    answer = initialLevelOfDebt*(repaymentPercentage/100)
    while(initialLevelOfDebt>50):
        initialLevelOfDebt = initialLevelOfDebt + initialLevelOfDebt*(interestPercentage/100)
        initialLevelOfDebt = initialLevelOfDebt - 100
        count = count + 1
    answer = answer + count * 100 + initialLevelOfDebt + initialLevelOfDebt*(interestPercentage/100)
    return answer
