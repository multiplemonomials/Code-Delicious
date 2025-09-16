AUTHOR = 'Jamie Smith'
SITENAME = 'Code Delicious'
TAGLINE = 'An Open-Source Plant Based Cookbook'
SITEURL = "https://multiplemonomials.github.io/Code-Delicious"

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Logo in the theme header
USER_LOGO_URL = "/images/site_logo.png"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Favicon configuration -- see here: https://simulatine.github.io/100DaysOfCode/day-5-configuring-pelican.html
STATIC_PATHS = ['extras']
EXTRA_PATH_METADATA = {
    "extras/favicon.ico": {"path": "favicon.ico"}
}


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