Tebores
=======

Tebores is a Tech Book Recommendation System.

It consists of a web-scrapper that obtains the latest books published at it-ebooks and freecomputerbooks and tweets them in [@tebores_](https://twitter.com/tebores_).

It has a db to record what it has scrapped.

#How to use

Currently it tweets via Selenium, I will make use of the Twitter api on the future.

1 - Create a Twitter account.

2 - Create ```tebores/files/sele_auth.py``` and type:
  ```python
  user = "your_twitter_account_without_@"
  password = "the_password"
  ```
3 - Launch the bot:

  ```
  python main.py 
  ```

  You can specify the number of seconds that Tebores will wait between the tweets.

  ```
  # Wait 5 mins between tweets.
  python main.py 300
  ```


#Enhance

At ```bookcrawler.py``` inherit ```BookCrawler``` and define a method called ```get_books``` that does your magic and returns a dict of book_url:book_name.

```python
class YourCrawler(BookCrawler):
	def __init__(self, url=your_url):
		BookCrawler.__init__(self, url)

	def get_books(self):
		book_dict = {}
		# Your magic goes here.
		return book_dict
```

#Future

- Twitter API.
- Model the followers' tastes and recommend them books.

#Note

I do pay for books and you should do so.
