XDebugTraceTree
===============

This simple script adds trees to [XDebug](https://xdebug.org/) traces.

Example input (taken from [here](http://a32.me/2013/05/discover-php-bottlenecks-with-xdebug-or-why-my-site-is-so-slow/):

```
TRACE START [2012-09-25 11:19:54]
    0.0005     645152  +645152   -> {main}() /var/www/test.php:0
    0.0007     649296    +4144     -> require(/var/www/config.inc) /var/www/test.php:4
    0.0007     649504     +208       -> define('HOST', '10.1.1.1') /var/www/config.inc:3
    0.0008     649536      +32       -> define('NAME', 'db') /var/www/config.inc:4
    0.0008     649568      +32       -> define('USER', 'u0') /var/www/config.inc:5
    0.0008     649600      +32       -> define('PASS', 'ps') /var/www/config.inc:6
    0.0012     695728   +46128     -> require(/var/www/class/db.php) /var/www/test.php:5
    0.0013     694736     -992     -> show_num($i = 1) /var/www/test.php:8
    0.0013     694736       +0       -> show_odd($i = 1) /var/www/test.php:21
    0.0013     694864     +128     -> show_num($i = 2) /var/www/test.php:8
    0.0013     694864       +0       -> show_even($i = 2) /var/www/test.php:21
    0.0014     694960      +96         -> sleep(1) /var/www/test.php:30
    1.0033     694864      -96     -> show_num($i = 3) /var/www/test.php:8
    1.0034     694864       +0       -> show_odd($i = 3) /var/www/test.php:21
    1.0034     694864       +0     -> show_num($i = 4) /var/www/test.php:8
    1.0034     694864       +0       -> show_even($i = 4) /var/www/test.php:21
    1.0035     694960      +96         -> sleep(1) /var/www/test.php:30
    2.0047     694864      -96     -> show_num($i = 5) /var/www/test.php:8
    2.0048     694864       +0       -> show_odd($i = 5) /var/www/test.php:21
    2.0048     695224     +360     -> alloc_array($size = 1024) /var/www/test.php:13
    2.0057     843024  +147800     -> DB::Get($type = 'mysql', $host = '10.1.1.1', $user = 'u0', $pass = 'ps', $db = 'db') /var/www/test.php:15
    2.0057     843664     +640       -> absDB->__construct($host = '10.1.1.1', $user = 'u0', $pass = 'ps', $db = 'db') /var/www/class/db.php:10
    2.0058     843664       +0         -> DB->__construct($host = '10.1.1.1', $user = 'u0', $pass = 'ps', $db = 'db') /var/www/class/db.php:36
    2.0058     844000     +336           -> DB->build() /var/www/class/db.php:19
    2.0058     844016      +16     -> absDB->connect() /var/www/test.php:16
    2.0058     844368     +352       -> mysqli_connect('10.1.1.1', 'u0', 'ps', 'db') /var/www/class/db.php:47
   11.0164       8432
TRACE END   [2012-09-25 11:20:05]

```

Output:

```
TRACE START [2012-09-25 11:19:54]
    0.0005     645152  +645152   └> {main}() /var/www/test.php:0
    0.0007     649296    +4144     └> require(/var/www/config.inc) /var/www/test.php:4
    0.0007     649504     +208     │ └> define('HOST', '10.1.1.1') /var/www/config.inc:3
    0.0008     649536      +32     │ └> define('NAME', 'db') /var/www/config.inc:4
    0.0008     649568      +32     │ └> define('USER', 'u0') /var/www/config.inc:5
    0.0008     649600      +32     │ └> define('PASS', 'ps') /var/www/config.inc:6
    0.0012     695728   +46128     └> require(/var/www/class/db.php) /var/www/test.php:5
    0.0013     694736     -992     └> show_num($i = 1) /var/www/test.php:8
    0.0013     694736       +0     │ └> show_odd($i = 1) /var/www/test.php:21
    0.0013     694864     +128     └> show_num($i = 2) /var/www/test.php:8
    0.0013     694864       +0     │ └> show_even($i = 2) /var/www/test.php:21
    0.0014     694960      +96     │   └> sleep(1) /var/www/test.php:30
    1.0033     694864      -96     └> show_num($i = 3) /var/www/test.php:8
    1.0034     694864       +0     │ └> show_odd($i = 3) /var/www/test.php:21
    1.0034     694864       +0     └> show_num($i = 4) /var/www/test.php:8
    1.0034     694864       +0     │ └> show_even($i = 4) /var/www/test.php:21
    1.0035     694960      +96     │   └> sleep(1) /var/www/test.php:30
    2.0047     694864      -96     └> show_num($i = 5) /var/www/test.php:8
    2.0048     694864       +0     │ └> show_odd($i = 5) /var/www/test.php:21
    2.0048     695224     +360     └> alloc_array($size = 1024) /var/www/test.php:13
    2.0057     843024  +147800     └> DB::Get($type = 'mysql', $host = '10.1.1.1', $user = 'u0', $pass = 'ps', $db = 'db') /var/www/test.php:15
    2.0057     843664     +640     │ └> absDB->__construct($host = '10.1.1.1', $user = 'u0', $pass = 'ps', $db = 'db') /var/www/class/db.php:10
    2.0058     843664       +0     │   └> DB->__construct($host = '10.1.1.1', $user = 'u0', $pass = 'ps', $db = 'db') /var/www/class/db.php:36
    2.0058     844000     +336     │     └> DB->build() /var/www/class/db.php:19
    2.0058     844016      +16     └> absDB->connect() /var/www/test.php:16
    2.0058     844368     +352       └> mysqli_connect('10.1.1.1', 'u0', 'ps', 'db') /var/www/class/db.php:47
   11.0164       8432
TRACE END   [2012-09-25 11:20:05]

```
