"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Julia Ludwig (jal545) and Jackson Stone (jls596)
Date:   9/30/20
"""
import introcs

def exchange(old, new, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency from
    to the currency to. The value returned represents the amount in
    currency to.

    The value returned has type float.

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string for a valid currency code

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    json=currency_response(old,new,amt)
    dst=get_dst(json)
    new_amt=before_space(dst)
    #print('New_amt is '+new_amt)
    return float(new_amt)



def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    space=s.find(' ')
    return s[:space]

def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    space=s.find(' ')
    return s[space+1:]

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    right_of_quotation = s.find('"')
    left_of_quotation = s.find('"',right_of_quotation+1)
    values_between_quotations = s[right_of_quotation+1:left_of_quotation]
    return values_between_quotations

def get_src(json):
    """
    Returns the src value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "src". For example, if the JSON is

    '{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query䠀
    """
    src=json.find('"src"')
    return first_inside_quotes(json[src+5:])

def get_dst(json):
    """
    Returns the dst value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "dst". For example, if the JSON is

    '{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    dst=json.find('"dst"')
    return first_inside_quotes(json[dst+5:])

def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "valid". For example,
    if the JSON is

    '{ "src":"", "dst":"", "valid":false, "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    err=json.find('"err"')
    err_statement=first_inside_quotes(json[err+5:])
    return not(err_statement=='')

def currency_response(old, new, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "src":"<old-amt>", "dst":"<new-amt>", "valid":true, "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "valid" will be followed by the value false (and "err" will have
    an error message).

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string with no spaces or non-letters

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    u='http://cs1110.cs.cornell.edu/2020fa/a1?from='+old+'&to='+new+'&amt='+str(amt)
    json=introcs.urlread(u)
    return json

def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    return not has_error(currency_response(code,code,0.0))
