## Welcome to Wikimedia Commons Helpers Tools

### Installation
* Clone the pywikibot repo (see [MediaWiki](https://www.mediawiki.org/wiki/Manual:Pywikibot/Gerrit#For_users)).
```bash
git clone --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git
```

* Navigate to the `core` folder and clone this repo as a submodule:
```bash
git submodule add https://github.com/miguel-angel-monjas/wmcommons-helpers.git
```

* From the Anaconda Navigator, create a Python 3.6 environment (for instance, `wmtools`).

* From the Anaconda Navigator, install the following packages:
** `mako`
** `requests`

* Navigate to the `wmcommons-helpers` folder (it should be a child of `core`) and activate the virtual environment you created previously. Run:
```bash
source activate wmtools
```

* From the command line, install some additional packages not supported by Anaconda, `http_request_randomizer`, `pillow`:
```bash
pip install http_request_randomizer
pip install pillow
```

* Create `user-config.py` with the following content (`Dummy` is used as username in the example):
```python
# -*- coding: utf-8  -*-

family = 'commons'
mylang = 'commons'

usernames['commons']['commons'] = 'Dummy'
```

* Run your notebooks:
```bash
jupyter notebook
```