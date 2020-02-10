#!/usr/local/bin/python3

# Implement a healthcheck method which will take an array of endpoints of
# the form host:port and run a test of each one returning a dictionary
# with each endpoint and either True or False depending on whether the
# endpoint is healthy
#
# for the purposes of this task, it is assumed that only http will be used
# and not https
# Further assume that each endpoint has a /status path which returns the
# health of the endpoint
# 
# An endpoint is assumed healthy if the call to /status returns with
# precisely a 200 status AND that status returns witin 0.5 seconds.
#
# You are only permitted to use the following libraries:
# asyncio
# aiohttp


