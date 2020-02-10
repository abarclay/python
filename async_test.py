#!/usr/local/bin/python3

import asyncio
import random

async def testing(myint):
	await asyncio.sleep(random.random()*10)
	print('yay! ' + str(myint))

async def healthcheck(endpoint):
	try:
		await asyncio.wait_for(testing(endpoint), timeout=15)
	except asyncio.TimeoutError:
		print('hcresult fail!')
		return(False)
	print("hcresult good!")
	return(True)

async def foo(myint):
	result=await asyncio.run(healthcheck(myint))
	return(result)

 
# main
for i in range(5):
	asyncio.run(foo(i))
	x = foo(i)
	print(x)
