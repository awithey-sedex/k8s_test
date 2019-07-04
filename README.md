This is a light-weight micro service demo.

There is a "front-end" servive, called "is-prime-frontend" and a backend service: "is-prime-backend".

The is-prime-frontend provides three endpoints:
	/ - provides simple usage information
	/_number_ says whether the supplied integer is a prime number
	/list/_start_/_count_ says for each number in the list, whether (or not) they are prime
		<count> is the length if the list. If it is not supplied, the default is 20.	
