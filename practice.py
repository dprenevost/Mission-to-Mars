{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a958a4e2-70b7-42b2-80ab-78d295a22da0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "01641d8c-83d1-418b-a428-cc76b8fbb0c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 96.0.4664\n",
      "Get LATEST chromedriver version for 96.0.4664 google-chrome\n",
      "Driver [C:\\Users\\dpren\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "# Set up Splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "63efdc37-660d-4017-b79f-7540478762bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Quotes to Scrape site\n",
    "url = 'http://quotes.toscrape.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2182aaf9-4827-49a3-a674-6b2c3dae198b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the HTML\n",
    "html = browser.html\n",
    "html_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "910f4f8d-5ae2-4949-8462-1c2bd930f91f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Top Ten tags'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Scrape the Title\n",
    "title = html_soup.find('h2').text\n",
    "title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2bf49fe5-ec12-459c-9338-67bfe5f03492",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "love\n",
      "inspirational\n",
      "life\n",
      "humor\n",
      "books\n",
      "reading\n",
      "friendship\n",
      "friends\n",
      "truth\n",
      "simile\n"
     ]
    }
   ],
   "source": [
    "# Scrape the top ten tags\n",
    "tag_box = html_soup.find('div', class_='tags-box')\n",
    "# tag_box\n",
    "tags = tag_box.find_all('a', class_='tag')\n",
    "\n",
    "for tag in tags:\n",
    "    word = tag.text\n",
    "    print(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3cd06a71-a37d-47f4-b7bb-8a319b9871f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'http://quotes.toscrape.com/'\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e9e278e1-d730-4a08-8989-ec0fc759bc07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "page: 1 ----------\n",
      "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”\n",
      "page: 1 ----------\n",
      "“It is our choices, Harry, that show what we truly are, far more than our abilities.”\n",
      "page: 1 ----------\n",
      "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”\n",
      "page: 1 ----------\n",
      "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”\n",
      "page: 1 ----------\n",
      "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”\n",
      "page: 1 ----------\n",
      "“Try not to become a man of success. Rather become a man of value.”\n",
      "page: 1 ----------\n",
      "“It is better to be hated for what you are than to be loved for what you are not.”\n",
      "page: 1 ----------\n",
      "“I have not failed. I've just found 10,000 ways that won't work.”\n",
      "page: 1 ----------\n",
      "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”\n",
      "page: 1 ----------\n",
      "“A day without sunshine is like, you know, night.”\n",
      "page: 2 ----------\n",
      "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”\n",
      "page: 2 ----------\n",
      "“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”\n",
      "page: 2 ----------\n",
      "“If you can't explain it to a six year old, you don't understand it yourself.”\n",
      "page: 2 ----------\n",
      "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”\n",
      "page: 2 ----------\n",
      "“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”\n",
      "page: 2 ----------\n",
      "“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”\n",
      "page: 2 ----------\n",
      "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”\n",
      "page: 2 ----------\n",
      "“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”\n",
      "page: 2 ----------\n",
      "“Good friends, good books, and a sleepy conscience: this is the ideal life.”\n",
      "page: 2 ----------\n",
      "“Life is what happens to us while we are making other plans.”\n",
      "page: 3 ----------\n",
      "“I love you without knowing how, or when, or from where. I love you simply, without problems or pride: I love you in this way because I do not know any other way of loving but this, in which there is no I or you, so intimate that your hand upon my chest is my hand, so intimate that when I fall asleep your eyes close.”\n",
      "page: 3 ----------\n",
      "“For every minute you are angry you lose sixty seconds of happiness.”\n",
      "page: 3 ----------\n",
      "“If you judge people, you have no time to love them.”\n",
      "page: 3 ----------\n",
      "“Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.”\n",
      "page: 3 ----------\n",
      "“Beauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.”\n",
      "page: 3 ----------\n",
      "“Today you are You, that is truer than true. There is no one alive who is Youer than You.”\n",
      "page: 3 ----------\n",
      "“If you want your children to be intelligent, read them fairy tales. If you want them to be more intelligent, read them more fairy tales.”\n",
      "page: 3 ----------\n",
      "“It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all - in which case, you fail by default.”\n",
      "page: 3 ----------\n",
      "“Logic will get you from A to Z; imagination will get you everywhere.”\n",
      "page: 3 ----------\n",
      "“One good thing about music, when it hits you, you feel no pain.”\n",
      "page: 4 ----------\n",
      "“The more that you read, the more things you will know. The more that you learn, the more places you'll go.”\n",
      "page: 4 ----------\n",
      "“Of course it is happening inside your head, Harry, but why on earth should that mean that it is not real?”\n",
      "page: 4 ----------\n",
      "“The truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.”\n",
      "page: 4 ----------\n",
      "“Not all of us can do great things. But we can do small things with great love.”\n",
      "page: 4 ----------\n",
      "“To the well-organized mind, death is but the next great adventure.”\n",
      "page: 4 ----------\n",
      "“All you need is love. But a little chocolate now and then doesn't hurt.”\n",
      "page: 4 ----------\n",
      "“We read to know we're not alone.”\n",
      "page: 4 ----------\n",
      "“Any fool can know. The point is to understand.”\n",
      "page: 4 ----------\n",
      "“I have always imagined that Paradise will be a kind of library.”\n",
      "page: 4 ----------\n",
      "“It is never too late to be what you might have been.”\n",
      "page: 5 ----------\n",
      "“A reader lives a thousand lives before he dies, said Jojen. The man who never reads lives only one.”\n",
      "page: 5 ----------\n",
      "“You can never get a cup of tea large enough or a book long enough to suit me.”\n",
      "page: 5 ----------\n",
      "“You believe lies so you eventually learn to trust no one but yourself.”\n",
      "page: 5 ----------\n",
      "“If you can make a woman laugh, you can make her do anything.”\n",
      "page: 5 ----------\n",
      "“Life is like riding a bicycle. To keep your balance, you must keep moving.”\n",
      "page: 5 ----------\n",
      "“The real lover is the man who can thrill you by kissing your forehead or smiling into your eyes or just staring into space.”\n",
      "page: 5 ----------\n",
      "“A wise girl kisses but doesn't love, listens but doesn't believe, and leaves before she is left.”\n",
      "page: 5 ----------\n",
      "“Only in the darkness can you see the stars.”\n",
      "page: 5 ----------\n",
      "“It matters not what someone is born, but what they grow to be.”\n",
      "page: 5 ----------\n",
      "“Love does not begin and end the way we seem to think it does. Love is a battle, love is a war; love is a growing up.”\n"
     ]
    }
   ],
   "source": [
    "for x in range(1, 6):\n",
    "   html = browser.html\n",
    "   quote_soup = soup(html, 'html.parser')\n",
    "   quotes = quote_soup.find_all('span', class_='text')\n",
    "   for quote in quotes:\n",
    "      print('page:', x, '----------')\n",
    "      print(quote.text)\n",
    "   browser.links.find_by_partial_text('Next').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7260a20d-ce96-4431-bd49-f81cf981ed9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "34984bf2",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 96.0.4664\n",
      "Get LATEST chromedriver version for 96.0.4664 google-chrome\n",
      "Driver [C:\\Users\\dpren\\.wdm\\drivers\\chromedriver\\win32\\96.0.4664.45\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4775187b-630f-482b-8d18-0548f424e655",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ecd14741",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "27e151c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'7 Things to Know About the Mars 2020 Perseverance Rover Mission'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "29cfc2c9-4d95-4257-9327-c08f7aa707e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's next rover to the Red Planet is slated to launch no earlier than July 30. These highlights will get you up to speed on the ambitious mission.\""
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a97d5a28-f96d-4458-b769-56d105115f22",
   "metadata": {},
   "source": [
    "### Featured Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c586d134-1cac-4e98-9e1e-3bcb6fa6fec5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "90b818e8-adad-447b-8313-dd7a98af7767",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8f8ad0c4-49f3-4e78-9a73-5d71645ea92b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8a8c4667-c6f8-4df8-953b-e124068682a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars3.jpg'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "fe637609-a8df-46c6-af0b-a202ebb86f66",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars3.jpg'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "673fc088-89eb-4876-962e-0ea4c6ae4fd4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "64381385-a3ff-47a2-a990-047b71226469",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fe85469a",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a4afae9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
