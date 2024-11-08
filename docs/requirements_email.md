# Requirements Email

Here's the challenge:

*Problem*:

Please design and develop a service that I can query that will yield the difference between 1.) the sum of the squares of the first n natural numbers and 2.) the square of the sum of the same first n natural numbers, where n is guaranteed to be no greater than 100.

Example:

The sum of the squares of the first ten natural numbers is:

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

*Requirements*:

You should use Python3.6+ and Django.

I should be able to install your service by doing: pip install -r requirements.txt. Please include a README with instructions for launching it.

I should be able to query your service at the following (or similar) endpoint:

localhost:8000/difference?number=n where n is any integer greater than 0 and less than or equal to 100.

Your service should emit a JSON object of the following structure:

{
"datetime":current_datetime,
"value":solution,
"number":n,
"occurrences":occurrences // the number of times n has been requested
"last_datetime": datetime_of_last_request
}

For persistence you can use postgres, mysql, memcached,  sqlite3 or redis.

*Optional 1*

Assume this is only the first of many such similar requests. For example, as a team we have decided that users really want to know the answer you may need to develop a service that also asks the following:

Please design and develop a service that I can query that will yield 1.) if a sequence of three natural numbers (a,b and c) are a Pythagorean triplet and 2.) the product of the sequence of these three numbers where abc = n, where c is guaranteed to be no greater than 1000.

Construct your application in such a way that you can easily scale to meet these additional product needs.

*Optional 2*

Use Python3.6 style typehinting

*Optional 3*

Unit tests are appreciated.

*Optional 4*

Front end:

Create a react application (or any other front end framework or just jquery) based on the above backend service that should display a list of the above values in the four columns described above.

Your UI should have a form to enter the number that you wish to query.

*Delivery*:

Please commit your code using either git or mercurial and use either bitbucket, gitlab, github, or a similar service. 

If you run into any issues, please contact Joe directly (cc'd).

Please deliver the result by November 5, 11AM ET.

Thank you!