# web-security-demos
Some demonstration apps to show simple examples of a range of web security vulnerabilities

## Client-side
* [CSRF (Cross-Site Request Forgery)](/client-side-injection/csrf)
* [XSS (Cross-Site Scripting) (express)](/client-side-injection/xss-express)
* [XSS (Cross-Site Scripting) (flask)\*](/client-side-injection/xss-flask)
* [Response Splitting/CRLF Injection\*\*](/client-side-injection/response_splitting)
* [DOM\_clobbering\*\*](/client-side-injection/dom_clobbering)

\* note: I built the flask version of the XSS challenge because the express one seemed to be a bit broken. For whatever reason, it doesn't seem to actually trigger XSS, despite me rendering it insecurely on the page (using innerHTML)?

\*\* these two demos were used to show off how to bypass some protections that could prevent XSS from appearing (e.g. http-only cookies and sanitization) 

## Server-side
* [Shell Injection](/server-side-injection/shell_injection)
* [SQL Injection](/server-side-injection/sqli)
* [Server-side template injection](/server-side-injection/ssti)
