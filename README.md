Tebores
=======

Tebores is a Tech Book Recommendation System.

It consists of a web-scrapper that obtains the latest books published at
**it-ebooks** and **freecomputerbooks**, then tweets about them in
[@tebores_](https://twitter.com/tebores_).

If you follow the bot and favourite some of the tweets Tebores will start
recommending similar books (-> doing this last part).

# How to roll your own

## Timetable and frequency

You can modify the tweet and scrap (data recollection) times on ```config.py```:

```python
# Bot timetable
TIMETABLE_SCRA = {
    # Scraping hours (data recollection) from-to 24h format.
    'FROM' : '11:45',
    'TO' : '22:00'
    }
TIMETABLE_TWI = {
    # Tweeting hours from-to 24h format.
    'FROM' : '12:00',
    'TO' : '22:00'
    }
```
as well as the scrap and tweet frequency on the above intervals:
```python
# Scraping frequency, seconds
S_FREQ = 300
# Tweeting frequency, seconds
TW_FREQ = 180

```

## Authentication

To authenticate you can use a username-password pair, or the Twitter API keys.

First, fill in ```config.py```'s variables.

```python
# Name of the database -> put the one you like
DB_NAME = 'tebores_db.sqlite'
# Bot type: DesktopBot or TwitterAPIBot -> choose one
BOT_TYPE = 'TwitterAPIBot'
```

* API keys
  1. Create a Twitter account.
  2. Create a Twitter app with read-write permissions.
  3. The keys are stored as environment variables in your machine.
  You have to setup: ```TWI_CO_KEY```: consumer key,
  ```TWI_CO_SECRET```: consumer secret,
  ```TWI_AC_TOKEN```: access token, ```TWI_AC_SECRET```: access secret.
  
* Username-password pair
  1. Create a Twitter account.
  2. Put your credentials on ```tebores/files/auth.py```:
    ```python
    user = "your_twitter_account_without_@"
    
    password = "the_password"
    ```

## Start!

After setting up the login you can launch the bot:
```
python daemon.py 
```

But better with:
```bash
nohup python daemon.py &
```

If your machine has more important things to do, schedule the process priority:
```bash
nohup nice python daemon.py &
```

# Enhance

You can add more book websites to Tebores changing the following files.

1. For each new book website create a new class at ```bookcrawler.py``` which
inherits ```BookCrawler```.

2. Add the class name on ```BookCrawler.factory```. For instance, if the new
class is ```CoolNewPageCrawler```:
  ```python
  @staticmethod
  def factory(name):
      if name == 'ITebooksCrawler':
          return ITebooksCrawler()
      elif name == 'FreeCBCrawler':
          return FreeCBCrawler()
      elif name == 'CoolNewPageCrawler':
          return CoolNewPageCrawler()
      else:
          throw error
  ```
3. Fill in the abstract method ```get_books``` of ```BookCrawler``` doing your
magic, it must return a dictionary with ```book-url:book-name```.
  ```python
  class CoolNewPageCrawler(BookCrawler):
	  def __init__(self, url=your_url):
		  BookCrawler.__init__(self, url)

	  def get_books(self):
		  book_dict = {}
		  # Your magic goes here.
		  return book_dict
  ```

# Headless Firefox-Selenium

If you don't want to use the Twitter API and Selenium opening the browser seems
annoying, setup a headless version of Firefox-Selenium. We are going to use
[Xvfb](http://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml),
a virtual framebuffer X server.

Install Xvfb and its dependencies:

```bash
sudo apt-get -y --force-yes install xvfb x11-xkb-utils xfonts-100dpi \
xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps
```

Start Xvfb and setup the ```DISPLAY``` environment variable:

```bash
Xvfb :99 -screen 0 1280x1024x16 &
export DISPLAY=:99
```

Alternatively you can use it as service, see:
[xvfb script](https://github.com/7flying/tebores/blob/master/tebores/xvfb).

# Future

- Model the followers' tastes and recommend them books.

# Note

I do pay for books and you should do so.
