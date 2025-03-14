AUTHOR = 'Jamie Smith'
SITENAME = 'Code Delicious'
TAGLINE = 'An Open-Source Plant Based Cookbook'
SITEURL = "https://multiplemonomials.github.io/Code-Delicious"

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Image Process plugin settings
# Documented here: https://github.com/pelican-plugins/image-process
IMAGE_PROCESS = {
    "article-image": {
        "type": "image",
        "ops": ["scale_in 600 600 True"],
    },
}

THEME = "pelican-svbhack"