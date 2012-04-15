Custom themes for Make Tyler Weird
----------------------------------

You'll need Vagrant to get this working easily:

http://vagrantup.com/docs/getting-started/index.html

You'll also need fabric in order to use the dev tools:

    sudo easy_install fabric

To get a development environment running do the following:

    git clone git@github.com:hacktyler/maketylerweird.git
    cd maketylerweird
    vagrant box add maketylerweird http://media.hacktyler.com/vagrant/maketylerweird.box
    vagrant init maketyleweird
    vagrant up

To see your new dev server, visit:

    http://localhost:4567

When you make a change to the theme, you'll need to run:

    fab reload
