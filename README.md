django-boilerplate -- a standard layout for Django apps
===============================================================================

## Description

django-boilerplate is an attempt to set up an convention for Django app layouts,
to assist in writing utilites to deploy such applications. A bit of convention
can go a long way, if one method is not better than another.

## Acknowledgements

The folks at Mozilla working on the [next version of AMO](https://github.com/jbalogh/zamboni)
were the primary inspiration for this layout.

## Directory Structure

    django-boilerplate/
    ....apps/
        ....foo/
            ....templates/
            ....templates/foo/
            ....templates/foo/foo.html
            ....models.py
            ....views.py
            ....forms.py
    ....lib/
    ....logconfig/
    ....media/
        ....css/
            ....vendor/
        ....js/
            ....vendor/
        ....images/
    ....requirements/
        ....common.txt
        ....dev.txt
        ....production.txt
    ....templates/
    ....vendor/
    ....environment.py
    ....fabfile.py
    ....manage.py
    ....settings.py


### apps

Everything in this directory is added to the PYTHONPATH when the
`environment.py` file is imported.

### lib

Python packages and modules that aren't true Django 'apps' - i.e. they don't
have their own models, views or forms. These are just regular Python classes and
methods, and they don't go in the `INSTALLED_APPS` list of your project's
settings file. 

Everything in this directory is added to the PYTHONPATH when the
`environment.py` file is imported.

### logconfig

An extended version of the
[log_settings](https://github.com/jbalogh/zamboni/blob/master/log_settings.py)
module from Mozilla's [zamboni](https://github.com/jbalogh/zamboni).

This package includes an `initialize_logging` method meant to be called from the
project's `settings.py` that sets Python's logging system. The default for
server deployments is to log to syslog, and the default for solo development is
simply to log to the console. 

### media

Just an arbitrary convention - a subfolder each for CSS, Javascript and images.
3rd-party files (e.g. the 960.gs CSS files or jQuery) go in a `vendor/`
subfolder to keep your own code separate.

### requirements

pip requirements files, optionally one for each app environment. The
`common.txt` is installed in every case.

Our Fabfile (see below) is set up to install the project's dependencies from
these files. It's an attempt to standardize the location for dependencies like
Rails' `Gemfile`. We specificially avoid also listing the dependencies in the
README of the project, since a list there isn't actually checked programatically
or ever installed, so it tends to quickly become out of date.

### templates

Project-wide templates (i.e. those not belonging to any specific app in the
`apps/` folder). The boilerplate includes a `base.html` template that defines
these blocks:

#### <head>

`title`
Text for the browser title bar. You can set a default here and append/prepend to
it in sub-templates using `{{ super }}`.

`site_css`

Primary CSS files for the site. By defaut, includes `media/css/reset.css` and
`media/css/base.css`. 

`css`

Optional page-specific CSS - empty by default. Use this block if a page needs an extra CSS file
or two, but doesn't want to wipe out the files already linked via the `site_css`
block.

`extra_head`

Any extra content for betwee the `<head>` tags.

#### <body>

`header`

Top of the body, inside a `div` with the ID `header`.

`content`

After the `header`, inside a `div` with the ID `content`.

`footer`

After `content`, inside a `div` with the ID `footer`.

`site_js`

After all body content, includes site-wide Javascript files. By default,
includes `media/js/application.js` and jQuery. In deployed environments, links
to a copy of jQuery on Google's CDN. If running in solo development mode, links
to a local copy of jQuery from the `media/` directory - becuase the best way to
fight snakes on a plane is with jQuery on a plane.

`js`

Just like the `css` block, use the `js` block for page-specific Javascript files
when you don't want to wipe out the site-wide defaults in `site_js`.

### vendor

Python package dependencies installed as git submodules. pip's support for git
repositories is somewhat unreliable, and if the specific package is your own
code it can be a bit easier to debug if it's all in one place (and not off in a
virtualenv). 

At Bueda we collect general webapp helpers and views in the separate package
`comrade` and share it among all of our applications. It is included here as an
example of a Python package as a git submodule.

Any directory in `vendor/` is added to the `PYTHONPATH` by `environment.py`.

### Files

#### environment.py

Modifies the PYTHONPATH to allow importing from the `apps/`, `lib/` and
`vendor/` directories. This module is imported at the top of `settings.py` to
make sure it runs for both local development (using Django's built-in server)
and in production (run through mod-wsgi, gunicorn, etc.).

#### fabfile.py

We use Fabric to deploy to remote servers in development, staging and production
environments. The boilerplate Fabfile is quite thin, as most of the commands are
imported from [buedafab](https://github.com/bueda/ops), a collection of our
Fabric utilites.

#### manage.py

The standard Django `manage.py`.

#### settings.py

Many good default settings for Django applciations - check the file for more
detailed documentation.
