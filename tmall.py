from datetime import date
import sys
import time
start = time.clock()

def add_months(sourcedate, months):
    """A module to add months to a date

    :sourcedate: TODO
    :months: TODO
    :returns: TODO

    """
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1 
    return date(year, month, sourcedate.day)

price = float( sys.argv[1] )
# print "Your price is %f" % price

billingday   = 3
repaymentday = 13
rateperday = 1.0821 / 10000
# print rateperday

today=date.today()

if today.day < billingday :
    # billingmonth = ( today.month + 1 ) % 12
    # if today.month == 12 :
    #     billingyear = today.year + 1
    # else :
    #     billingyear = today.year

    # firstrepaymentdate = date(billingyear, billingmonth, repaymentday)
    firstrepaymentdate = add_months( date(today.year, today.month, repaymentday), 1 )
else :
    # billingmonth = ( today.month +2 ) % 12
    # if today.month >= 11 :
    #     billingyear = today.year + 1
    # else :
    #     billingyear = today.year

    # firstrepaymentdate = date(billingyear, billingmonth, repaymentday)
    firstrepaymentdate = add_months( date(today.year, today.month, repaymentday), 2)

print firstrepaymentdate

secondrepaymentdate = add_months(firstrepaymentdate,1)
thirdrepaymentdate  = add_months(firstrepaymentdate,2)

days1 = firstrepaymentdate - date.today()
days2 = secondrepaymentdate -date.today()
days3 = thirdrepaymentdate - date.today()

# print firstrepaymentdate
# print secondrepaymentdate
# print thirdrepaymentdate

# print "days1 = %d" % days1.days
# print "days2 = %d" % days2.days
# print "days3 = %d" % days3.days


difference = price * ( ( 1 + rateperday ) ** days1.days + ( 1 + rateperday ) ** days2.days + ( 1 + rateperday ) ** days3.days ) - 3 * price
discount = ( price - difference ) / price

print "Your difference is %f" % difference
print "Your discount is %f" % discount

print time.clock() - start
