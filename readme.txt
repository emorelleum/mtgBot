github URL: https://github.com/emorelleum/mtgBot

By: Jerome Mueller (Emorelleum)

MTG courtesy linker: (EmorBot)

	This bot searches marked posts and comments for names of Magic: The Gathering® cards, and posts image links to the cards. The reason for this bot is that everywhere that there are discussions about MTG, people are expected to provide links to the cards so that people can easily look up the cards pertinent to the discussion. These are generally referred to as "courtesy Links". This bot differs from a similar reddit bot in that it searches the entire comment for cards, rather than just text placed within "[[" and "]]", which can potentially make the text messy, and also requires knowledge of the punctuation of the card, which can be difficult to remember.
	The bot works by searching for comments containing MTG_LINK (case sensitive, those characters in that order, may be surrounded by other characters and may appear at any point), then extracting from that comment single words, duplets of words, triples of words, and so on up to 6 words. It then compares each of the words/combination of words with a JSON database of magic cards (also stripping punctuation from the database entries). Using the data in the database, it then assembles a link to a website hosting the card image using data in the database.

Features: Search for all cards without having to specify them completely! This bot can find cards even if the punctuation is not correct, which is a pain for some cards (e.g.  Abu Ja'far). Finally, the saves its info in persistant storage, so if it errors, there is a good chance it can be restarted without fear of it double posting a lot. The bot makes its rounds around the subreddit approximately every 2 minutes.

Other behavior: Since the bot does dumb text search, it will link to cards that coincidentally appeared in the comment for its English use (did you know that who, what, where, when, and why are all MTG cards [sorta speaking]). Some links are recognized as MTG products, but not technically cards (e.g. tokens) due to what is present in the database I am using. Finally, there are rare instances in which a card's name completely contains another card's name (e.g. "Release" and "Release the Ants"). The bot will link both cards in these cases.

Some sample inputs/outputs - All card names in the replies are clickable links

Post/Comment: Hello there, may I trade your conflux for my loxodon Warhammer

Reply: [none, MTG_LINK not included]


Comment: MTG_LINK urzas science Fair project

Reply: Courtesy Links:
Urza's Science Fair Project


Post: MTG_LINK So the other day my opponent was bearing down on me with baneslayer angel, and all I had to block with was a storm crow, so I used flash to play my elesh norn grand cenobite and blocked the baneslayer angel, and my storm crow survived and killed the angel to boot. It was awesome smashing the walletslayer to smithereens with my storm crow, even if flash and elesh norn are also on the expensive side. I then proceeded to beat my opponent over the head with my storm crow, which was a 23 turn clock. My opponent quickly conceded.

Reply: Courtesy Links for the post:
Down
Turn
Flash
Day
Storm Crow
Baneslayer Angel
Elesh Norn, Grand Cenobite

For testing further input, you can visit http://gatherer.wizards.com/ to see a full card database, and link to whatever you can find. Alternatively, it is fun to type in random sentences with MTG_LINK in the comment and just see if any of the words match actual cards.


Sources: Much of the framework logic was gleaned from the praw tutorial linked in the 470Z subreddit. For JSON, I looked heavily at examples given in the docs.python.org JSON section. The card database (not included in the repository because if size) was obtained from mtgjson.com. The card images are hosted by mtgimage.com. 
