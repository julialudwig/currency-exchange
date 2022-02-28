"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Julia Ludwig (jal545) and Jackson Stone (jls596)
Date:   9/30/20
"""

import introcs
import a1

#testing something
def testA():
    """
    Test procedure for Part A

    First tests a1.after_space and then tests a1.before_space

    Parameters: none
    Preconditons: none
    """
    print("Testing after_space")

    #Testing for one space between words:
    introcs.assert_equals('Ludwig',a1.after_space('Julia Ludwig'))

    #Testing for a string starting with a space:
    introcs.assert_equals('Julia',a1.after_space(' Julia'))

    #Testing for a string ending in a space:
    introcs.assert_equals('',a1.after_space('Julia '))

    #Testing for multiple spaces between characters:
    introcs.assert_equals('is a rower.',a1.after_space('Jackson is a rower.'))

    #Testing for two spaces in row
    introcs.assert_equals(' there',a1.after_space('Hello  there'))

    print('Testing before_space')

    #Testing for one space between words:
    introcs.assert_equals('Julia',a1.before_space('Julia Ludwig'))

    #Testing for a string starting with a space:
    introcs.assert_equals('',a1.before_space(' Julia'))

    #Testing for a string ending in a space:
    introcs.assert_equals('Julia',a1.before_space('Julia '))

    #Testing for multiple spaces between characters:
    introcs.assert_equals('Jackson',a1.before_space('Jackson is a rower.'))

    #Testing for two spaces in row
    introcs.assert_equals('Hello',a1.before_space('Hello  there'))


#testing something
def testB():
    """
    Test procedure for Part B

    Tests a1.first_inside_quotes(s) then a1.get_src(json)
    then a1.get_dst(json) then a1.has_error(json)
    """
    print('Testing a1.first_inside_quotes')

    #Tests for one set of double quotes:
    introcs.assert_equals('B C',a1.first_inside_quotes('A "B C" D'))

    #Tests for two sets of double quotes:
    introcs.assert_equals('B C',a1.first_inside_quotes('A "B C" D "E F" G'))

    #Tests for single quotes inside double first_inside_quotes
    introcs.assert_equals('',a1.first_inside_quotes('"''"'))

    #Tests for \' inside of quotes
    introcs.assert_equals("He said, 'hello'", a1.first_inside_quotes('She said, '+\
    '"He said, \'hello\'"'))

    #Tests for \" inside of quotes
    introcs.assert_equals('Hello', a1.first_inside_quotes('\"Hello\"'))

    print('Testing a1.get_src(json)')

    #Tests for a valid JSON
    introcs.assert_equals('5 United States Dollars',a1.get_src('{ "src":"5 '+\
    'United States Dollars", "dst":"4.21305 Euros", "valid":true, "err":"" }'))

    #Tests for an invalid JSON
    introcs.assert_equals('',a1.get_src('{ "src":"", "dst":"", "valid":false,'+\
    ' "err":"Currency amount is invalid." }'))

    print('Testing a1.get_dst(json)')

    #Tests for a valid JSON
    introcs.assert_equals('4.21305 Euros',a1.get_dst('{ "src":"5 United States '+\
    'Dollars", "dst":"4.21305 Euros", "valid":true, "err":"" }'))

    #Tests for an invalid JSON
    introcs.assert_equals('',a1.get_dst('{ "src":"", "dst":"", "valid":'+\
    'false, "err":"Currency amount is invalid." }'))

    print('Testing for a1.has_error(json)')

    #Tests for no error
    introcs.assert_equals(False,a1.has_error('{ "src":"5 United States'+\
    ' Dollars", "dst":"4.21305 Euros", "valid":true, "err":"" }'))

    #Tests for an invalid from currency
    introcs.assert_equals(True,a1.has_error('{ "src":"", "dst":"", "valid":'+\
    'false, "err":"Source currency code is invalid." }'))

    #Tests for invalid to currency
    introcs.assert_equals(True,a1.has_error('{ "src":"", "dst":"", '+\
    '"valid":false, "err":"Exchange currency code is invalid." }'))

    #Tests for invalid amount
    introcs.assert_equals(True,a1.has_error('{ "src":"", "dst":"", '+\
    '"valid":false, "err":"Currency amount is invalid." }'))

#testing something
def testC():
    """
    Test procedure for Part C

    Tests a1.currency_response(old,new,amt)
    """
    print('Testing a1.currency_response(old,new,amt)')

    #Testing for positive amt
    introcs.assert_equals('{ "src":"2.5 United States Dollars", "dst":'+\
    '"64.375 Cuban Pesos", "valid":true, "err":"" }' ,a1.currency_response('USD',
    'CUP',2.5))

    #Testing for invalid old
    introcs.assert_equals('{ "src":"", "dst":"", "valid":false, "err":'+\
    '"Source currency code is invalid." }' ,a1.currency_response('hey','CUP',2.5))

    #Testing for invalid new
    introcs.assert_equals('{ "src":"", "dst":"", "valid":false, "err":'+\
    '"Exchange currency code is invalid." }' ,a1.currency_response('USD','hey',2.5))

    #Testing for amt=0.0
    introcs.assert_equals('{ "src":"0 United States Dollars", "dst":"0 '+\
    'Euros", "valid":true, "err":"" }' ,a1.currency_response('USD','EUR',0.0))

    #Testing for negative amount
    introcs.assert_equals('{ "src":"-5.5 Australian Dollars", '+\
    '"dst":"-423.98816558498 Japanese Yen", "valid":true, "err":"" }' ,
    a1.currency_response('AUD','JPY',-5.5))

    #Testing for old=new
    introcs.assert_equals('{ "src":"2.5 United States Dollars", "dst":'+\
    '"2.5 United States Dollars", "valid":true, "err":"" }' ,
    a1.currency_response('USD','USD',2.5))

    #Testing for more than one place before and after decimal
    introcs.assert_equals('{ "src":"44.44 Swedish Kronor", "dst":'+\
    '"372.49095275253 Indian Rupees", "valid":true, "err":"" }' ,
    a1.currency_response('SEK','INR',44.44))

#testing something
def testD():
    """
    Test procedure for Part D

    Tests a1.is_currency(code) then a1.exchange(old,new,amt)
    """
    print('Testing a1.is_currency(old,new,amt)')

    #Testing for valid currency code
    introcs.assert_equals(True,a1.is_currency('USD'))

    #Testing for second currency code
    introcs.assert_equals(True,a1.is_currency('AUD'))

    #Testing for lowercase currency code
    introcs.assert_equals(False,a1.is_currency('aud'))

    #Testing for invalid currency code
    introcs.assert_equals(False,a1.is_currency('jackson'))

    #Testing for capitals and lowercase within currency code
    introcs.assert_equals(False,a1.is_currency('UsD'))

    #Testing for empty currency code
    introcs.assert_equals(False,a1.is_currency(''))

    print('Testing a1.exchange(old,new,amt)')

    #Testing for positive values
    introcs.assert_floats_equal(14.8582587,a1.exchange('USD','AUD',10.9))

    #Testing for negative values
    introcs.assert_floats_equal(-14.8582587,a1.exchange('USD','AUD',-10.9))

    #Testing for amt=0
    introcs.assert_floats_equal(0.0,a1.exchange('HUF','IDR',0.0))

    #Testing for amt with two decimal points
    introcs.assert_floats_equal(5872.3577621357,a1.exchange('IMP','IQD',3.79))

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
