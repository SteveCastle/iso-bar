# isobar

Isobar is a django seed project with ansible instrumentation for starting
a generalized business application.

## Features
1. Redis caching.
2. Data based auth system.
3. Front end agnostic REST endpoints provided by Django Rest Framework.
4. CMS by Django CMS.
5. Django storages for CDN static files.
6. Nose with coverage test runner.

## Installation

1. Clone the isobar repository.
2. Open a terminal in the isobar directory.
3. Run `vagrant up`.
4. Vagrant will create a vm and install ansible to complete the build process.
5. Inside your virtual machine change directory to /vagrant/deployment.
6. Run `ansible-playbook -s -k -u vagrant provision.yml`
7. Congratulations you have a working django isobar project.

## Usage

1. The project is installed to /var/projects/isobar/code/isobar
2. From the project directory you can `python manage.py createsuperuser`
3. To run your app `python manage.py runserver 0.0.0.0:8080`
4. To login to the admin screen in your browser go to localhost:8080/admin
5. Now write some urls, views, and templates. It's that easy ya dingus.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license
