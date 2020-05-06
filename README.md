# Lunatech Group's website

This site is the portal to all our websites, it's the highest point in the hierarchy of entry points to Lunatech. It contains links to the local websites, our [blog][blog] and [life][life] sites. Dynamic content is displayed: our latest tech blog article and latest event article.

## Design decisions

Python with Flask is used to manage  dynamic content while keeping the application to a minimum. Templating and serving static files are also well supported. The [Requests][requests] library is used for API calls.

## How to run it locally

1. Install `python3` and follow the steps from the [Flask installation documentation][flask] until you have a running virtual environment. 
2. Install the requirements: `pip install -r requirements.txt`.
3. Run the application: `python application.py` and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).




[blog]: https://blog.lunatech.com
[life]: https://life.lunatech.com
[requests]: https://requests.readthedocs.io/en/master/
[flask]: https://flask.palletsprojects.com/en/1.1.x/installation/#activate-the-environment
