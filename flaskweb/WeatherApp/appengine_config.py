from google.appengine.ext import vendor
# Add any libraries installed in the "lib" folder.
# vendor.add('lib')
vendor.add(Flask)
vendor.add(click)
vendor.add(gunicorn)
vendor.add(itsdangerous)
vendor.add(Jinja2)
vendor.add(MarkupSafe)
vendor.add(pytz)
vendor.add(requests)
vendor.add(Werkzeug)
