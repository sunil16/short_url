# Short Url Service

  - submit long url
  - wait for result
  - get short url

### Tech

Short url service uses a number of open source projects to work properly:

* [Python] - Python is an interpreted, high-level, general-purpose programming language.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps.
* [jQuery] - jQuery is a fast, small, and feature-rich JavaScript library.

And of course Short url service itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Find Lat and Lng requires [Flask](https://flask.palletsprojects.com/en/1.1.x/) v1.1.1+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd short_url
$ pip install -r requirements.txt
$ python3 app.py

```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://127.0.0.1:5000/
```

### API Endpoints

#### Uploads

* **/** (home page and post long url)
* **/<short_url>** (redirect original url)
* **/search** (search urls by title)


License
----

MIT


**Free Software

   [dill]: <https://github.com/sunil16/short_url.git>
   [git-repo-url]: <https://github.com/sunil16/short_url.git>
   [Python]: <https://www.python.org/>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
