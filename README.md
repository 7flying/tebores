Tebores
=======

Tebores is a Tech Book Recommendation System.

It consists of a web-scrapper that obtains the latest books published at
it-ebooks and freecomputerbooks and tweets them
in [@tebores_](https://twitter.com/tebores_).

It has a db to record what it has scrapped.

# How to make your own

To authenticate you can use a username-password pair, or the Twitter API keys.

First, fill in ```config.py```'s variables.

```
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
    
After setting up the login you can launch the bot:
```
python daemon.py 
```

You can specify the number of seconds that Tebores will wait between the
tweets.
```
# Wait 5 mins between tweets.
python daemon.py 300
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

# Future

- Model the followers' tastes and recommend them books.

# Note

I do pay for books and you should do so.
