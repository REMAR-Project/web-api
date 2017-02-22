To get uWSGI to start automatically when the server is booted, copy uwsgi.conf to

    /etc/init

You will also need to edit the config file so that it can find the following:

1. the virtualenv into which uWSGI has been installed
2. the folder containing the vassals for uWSGI to launch

You can now use:

    $ sudo start uwsgi

to start the server, and

    $ sudo stop uwsgi

to stop it. The server will also start & stop things according to the systems run-level as defined in uwsgi.conf

