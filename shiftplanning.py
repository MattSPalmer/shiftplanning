#!/usr/bin/python

import json
import urllib
import urllib2

response_codes = {
    '-3': "Flagged API Key - Pemanently Banned",
    '-2': "Flagged API Key - Too Many invalid access attempts - contact us",
    '-1': "Flagged API Key - Temporarily Disabled - contact us",
    '1' : "Success -",
    '2' : "Invalid API key - App must be granted a valid key by ShiftPlanning",
    '3' : "Invalid token key - Please re-authenticate",
    '4' : "Invalid Method - No Method with that name exists in our API",
    '5' : "Invalid Module - No Module with that name exists in our API",
    '6' : "Invalid Action - No Action with that name exists in our API",
    '7' : "Authentication Failed - You do not have permissions to access the service",
    '8' : "Missing parameters - Your request is missing a required parameter",
    '9' : "Invalid parameters - Your request has an invalid parameter type",
    '10' :"Extra parameters - Your request has an extra/unallowed parameter type",
    '12' :"Create Failed - Your CREATE request failed",
    '13' :"Update Failed - Your UPDATE request failed",
    '14' :"Delete Failed - Your DELETE request failed",
    '20' :"Incorrect Permissions - You don't have the proper permissions to access this",
    '90' :"Suspended API key - Access for your account has been suspended, please contact ShiftPlanning",
    '91' :"Throttle exceeded - You have exceeded the max allowed requests. Try again later.",
    '98' :"Bad API Paramaters - Invalid POST request. See Manual.",
    '99' :"Service Offline - This service is temporarily offline. Try again later."
}

internal_errors = {
    '1':"The requested API method was not found in this SDK.",
    '2':"The ShiftPlanning API is not responding.",
    '3':"You must use the login method before accessing other modules of this API.",
    '4':"A session has not yet been established.",
    '5':"You must specify your Developer Key when using this SDK.",
    '6':"The ShiftPlanning SDK needs the CURL PHP extension.",
    '7':"The ShiftPlanning SDK needs the JSON PHP extension.",
    '8':"File doesn't exist.",
    '9':"Could not find the correct mime for the file supplied.",
}

class ShiftPlanning():
    def __init__(self, key, user, pwd):
        self.api_endpoint = "http://www.shiftplanning.com/api/"
        self.output_type = "json"
        self.request = None
        self.token = None
        self.response = None
        self.response_data = None
        self.callback = None
        self.username = user
        self.password = pwd
        try:
            self.key = key
        except:
            raise Exception(internal_errors['5'])
        pass
