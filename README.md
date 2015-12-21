Try this on http://uniwhere.xyz

Steps to get this running - I hope: 

- clean ubuntu server (14.04) with ssh keys set up
- create a user on the server
- edit `config/uniwherebot.conf` and `fabfile.py` to update the user
- edit `fabfile.py` with the server's ip
- `cd` (locally) to `bot_app/`, run `git init` and `git remote add production root@<your_ip_or_domain>:/home/git/uniwherebot.git`
- run `fab create`. This will set up everything. it may go wrong. check your `config/` files and so on, pay attention to errors as they may help you.
- ssh into your server, `cd` to `bot_app` and `cp settings.ini.sample settings.ini`, then edit `settings.ini`.
- add a cronjob with `cd /path/to/bot_app/ && python updatedb.py` in order to update your local db from http://unipd.xyz.
- to test it out (be careful, also the tests may have errors), `cd test/`, `cp text_settings.ini.sample text_settings.ini` and edit `test_settings.ini`. Then you can run `python pytest.py` to run a elementary test, or you can fake some message POSTing with `python fake_message.py`.
