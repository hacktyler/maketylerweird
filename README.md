Custom themes for Make Tyler Weird
----------------------------------

You'll need Vagrant to get this working easily:

[http://vagrantup.com/docs/getting-started/index.html](http://vagrantup.com/docs/getting-started/index.html)

You'll also need fabric in order to use the dev tools:

    sudo easy_install fabric

To get a development environment running do the following:

    git clone git@github.com:hacktyler/maketylerweird.git
    cd maketylerweird
    vagrant box add maketylerweird http://media.hacktyler.com/vagrant/maketylerweird.box
    vagrant init maketyleweird
    vagrant up

To see your new dev server, visit:

[http://localhost:4567](http://localhost:4567)

Changes to the templates should be picked up immediately, but if you make changes to the static assets you'll need to run:

    fab reload

If you want direct access to the server you can get that too:

    vagrant ssh

To deploy changes to production (assuming you have the ssh key):

    fab deploy

