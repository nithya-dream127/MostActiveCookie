# Most Active Cookie

Code written to find the most active cookie in a given log file and on a specific date. The cookie with most occurences on the given date must be returned to the user. 

## Code

The repository is made of 3 files:

- FindMostActiveCookie.py: Contains the source code with logic to find the most active cookie present in the cookie_log.csv file. Returns list of cookies that were active for most times in a given date taken from the CLI. 
- cookie_log.csv: Stores the name of the cookies and their respective occurrences through different dates and time. This file acts as a data input to help user achieve his requirement.
- FindMostActiveCookieTest.py: Python unit test cases written for different scenarios to test the relevancy of the logic present in FindMostActiveCookie.py

## Usage

```python
python .\FindMostActiveCookie.py -f .\cookie_log.csv -d 2018-12-09
# returns "AtY0laUfhglK3lC7"

python -m unittest FindMostActiveCookieTest.py
# returns ".....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK"
```# MostActiveCookie
