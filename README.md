## Welcome to Wikimedia Commons Helper Tools

The Wikimedia Commons Helper Tools are a set of `pywikibot`-based notebooks that can be used to automate (to some extent) the upload of images from third-party sites to Wikimedia Commons. Appropriate license templates are assigned, usually including a template to ask for verification as well. There are currently five (set of) tools that enable upload of images to Wikimedia Commons:
1. `gencat_upload`: From the press release of the Generalitat of Catalonia.
2. `moncloa_upload`: From the photo galleries of La Moncloa, the Ministry of Presidency of the Government of Spain.
3. `moncloa_fototeca_upload`: From the photo library (*fototeca*) of La Moncloa, the Ministry of Presidency of the Government of Spain.
4. `eldiario.es_upload`: From [eldiario.es](http://www.eldiario.es/), a Spanish newspaper that publishes its contents under a CC-BY-SA license.
5. `diariomadrid`: From the press releases of [diario.madrid.es](http://diario.madrid.es/), the news room of the City of Madridy, which publishes its contents under a CC license as well.

### Installation
**Python version**. `pywikibot` can be used with both Python 2.7 or Python 3.*. However, my personal advice is to use 3.*. There is a main rationale for that: text management. Using Python 2.7 translates into an endless fight with encoding issues. It's possible to make it work (I did it) but it can become a nightmare. If possible use Python 3.6 or later.

**Execution modes**: The Wikimedia Commons Helper Tools run as Jupyter notebooks. You can run them in two main ways: in your our machine, using your Python deployment; or through [PAWS](https://wikitech.wikimedia.org/wiki/PAWS). It is a Jypiter notebook environment provided by the Wikimedia Foundation and tailored to enable easy-to-use access to the Wikimedia projects (for instance, you don't need to worry about `pywikibot` installation; it's already provided!!!).

#### Stand-alone installation
Provided that you've already installed and configured Python 3.6, you need to follow the following steps:

1. First of all, the `pywikibot` library must be installed. Clone the pywikibot repo (see [MediaWiki](https://www.mediawiki.org/wiki/Manual:Pywikibot/Gerrit#For_users)), as only official distribution does not include the upload bots.
```bash
git clone --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git
```

2. Navigate to the `core` folder and clone this repo as a submodule of `pywikibot` (newer versions of Git clone the repo as well; in older versions you will need to clone it explicitly):
```bash
git submodule add https://github.com/miguel-angel-monjas/wmcommons-helpers.git
```
3. This step is not totally required, but recommended: create a Python 3.6 environment, for instance, `wmtools`. You can do it from the command line or using environments such as the Anaconda Navigator.

4. Navigate to the `wmcommons-helpers` folder (it should be a child of `core`) and activate the virtual environment you created previously. Run:
```bash
source activate wmtools
```

5. Install the following packages:
5.1. [`Mako`](http://www.makotemplates.org/): All the pages are created using this template library.
5.2. [`requests`](http://docs.python-requests.org/en/master/): For HTTP request management.
5.3. [`http_request_randomizer`](https://pypi.python.org/pypi/http-request-randomizer): This package is needed to get an anonymous access to La Moncloa site. It seems as if it has some protection about automated crawling and plain access through `requests`, regardless of the used headers, does not work. This package is not part of the Anaconda distribution.
5.4. [`Pillow`](https://pillow.readthedocs.io/en/latest/): For image handling. This package is not part of the Anaconda distribution.

The simplest way is to take advantage of the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

Otherwise you can install them in an individual way:
```bash
pip install Mako
pip install requests
pip install http_request_randomizer
pip install pillow
```

6. Create a `user-config.py` file in the `wmcommons-helpers` folder, with the following content (`Dummy` is used as username in the example below; write down yours or your bot's instead):
```python
# -*- coding: utf-8  -*-

family = 'commons'
mylang = 'commons'

usernames['commons']['commons'] = 'Dummy'
```

7. Run Jupyter:
```bash
jupyter notebook
```

8. Once the notebook server opens in your browser, pick up the notebook you want to use. Edit it to include the address of the page where the images are and the categories you want to assign and run all the cells.

#### PAWS installation
As mentioned above, `pywikibot` is available without any further task to execute and the only additional work you need to carry out is cloning the repo and installing the additional packages (authentication is done through OAuth):
1. Access to [PAWS](https://paws.wmflabs.org/). You'll be asked to get authenticated. Use your credentials.
2. Create a bash notebook. Run the following commands:
```bash
git clone https://github.com/miguel-angel-monjas/wmcommons-helpers.git
cd wmcommons-helpers
pip install -r requirements.txt
```
3. Go back to the home and access the `wmcommons-helpers` folder. You'll see the list of available notebooks. Choose one, edit it to include the address of the page where the images are and the categories you want to assign and run all the cells.

### Use
If you're using the PAWS option, you are not even required to know Python. All the notebooks require some customization (for instance, the URL of the page where the images you want to upload are), but no actual Python knowledge is needed. Next, I'll explain what you need to do to upload images to Wikimedia Commons.

#### `gencat_upload`
`gencat_upload` has been designed to enable automatic uploads from the Generalitat of Catalonia press releases (notes de premsa). There are four pieces of code you need to update:

1. The address of the page (mind that it must be under the `premsa.gencat.cat` hostname). Below you can see an example (simple quotes are used to include the address, which must start with the protocol, `http`):
```python
url = 'http://premsa.gencat.cat/pres_fsvp/AppJava/notapremsavw/304364/ca/bioinformatic-roderic-guigo-guanya-premi-nacional-recerca-2017.do'
```
2. The Commons categories you wish to assign to the uploaded images:
```python
categories = ['December 2017 in Catalonia',
             'Roderic Guigóz']
```

#### `moncloa_upload`

#### `moncloa_fototeca_upload`

#### `eldiario.es_upload`
`eldiario.es_upload` enables upload from [eldiario.es](http://www.eldiario.es/) articles. According to its [license](http://www.eldiario.es/licencia/), eldiario.es materials are published under a CC-BY-SA-3.0 license. Mind that a careful analysis has to be carried out before uploading material from eldiario.es as many times is shows as own material media by news agencies. At the moment, the following eldiario.es photographers are identified and considered as valid sources: *Marta Jara*, *[Robert Bonet](http://www.eldiario.es/autores/robert_bonet/)*, *[Sandra Lázaro](http://www.eldiario.es/autores/sandra_lazaro_-fotos/)*, *[Juan Manzanara](http://www.eldiario.es/autores/juan_manzanara/)*, *[Sònia Calvó](http://www.eldiario.es/autores/sonia_calvo/)*, *[Carlos Hernández](http://www.eldiario.es/autores/carlos_hernandez/)*, and *[Enric Català](http://www.eldiario.es/autores/enric_catala_-fotos/)*. It is important to note than the notebook retrieves the higher existing resolution images, by analyzing the image file name and changing the last characters to `_1` (i.e., the highest resolution version of `diputado-PSOE-Eduardo-Madina_EDIIMA20161107_0795_20.jpg` is `diputado-PSOE-Eduardo-Madina_EDIIMA20161107_0795_1.jpg`). Such higher resolution version is accepted in Wikimedia Commons (see [here](https://commons.wikimedia.org/wiki/Commons:Deletion_requests/Files_uploaded_by_KOKUYO#Files_uploaded_by_KOKUYO_(talk_%C2%B7_contribs)_4).

There are several pieces of code you need to update:

1. The address of the page. Below you can see an example (simple quotes are used to include the address, which must start with the protocol, `http`):
```python
url = 'http://www.eldiario.es/politica/democracia-crisis-instituciones_0_234126756.html'
```
2. The Commons categories you wish to assign to the uploaded images (only the name, get rid of the `Category:` prefix):
```python
categories = ['Ignacio Sánchez-Cuenca', '2014 in Spain']
```
3. The author, if you don't want the notebook to extract it:
```python
author = ''
```
4. Any additional category you might to include, for instace, related to you as uploader:
```python
upload_categories = ['Files uploaded by Supercommonsuploader']
```
5. The images in the page you don't want to upload (not valid photography, lower resolution...). The photograph series in the page starts in `0`. That is, if you want to exclude the second and the third images, include `1` and `2`:
```python
excluded = [1, 2]
```

#### `diario.madrid`
