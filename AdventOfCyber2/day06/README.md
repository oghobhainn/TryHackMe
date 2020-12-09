# Day06 - Be Careful With What You Wish on a Christmas Night

## XSS

XSS aka *Cross Site Scripting* is a web vuln that allows an attacker to compromise the interactions that users have with a vulnerable application. XSS allows the attacker to masquerade as a victim user, and carry out any actions that the user is able to perform.

### Stored XSS

example : a malicious JavaScript is submitted and later on stored directly on the website.

![malicious-comment]

The `evilcode()` is gonna get executed each time a user sees this comment. We could do the same with an image: the malicious JS would be hidden behing, and get executed each time someone clicks on it or the image is viewed. example : `<img src = 'LINK' onmouseover="alert('xss')">` (here the `alert('xss')` is the malware, executed when the user's mouse goes over it).

### Reflected XSS

Reflected is another type of XSS that is carried out directly in the HTTP request. Could be a malicious JS in the link of a search field. The code is not stored on the server directly, meaning that a target user should compromise himself by clicking on the link. example : `<https://somewebsite.com/titlepage?id=> <script> evilcode() </script>>`.

### How to detect XSS ?

Through the use of HTML tags; if we change the html code and there is a difference (color, text size,...), there's a XSS vulnerability ! But finding them manually can be challenging, so we can use __OWASP ZAP__, an open-source web application security scanner.

![owasp]()
![automated-scan]()
