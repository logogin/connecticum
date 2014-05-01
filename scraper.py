# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
import scraperwiki
import requests
import lxml.html

def parse_exhibitor(link):
    html = requests.get(link).content
    dom = lxml.html.fromstring(html)
    for li in dom.cssselect('[class*=marker-]'):
        if 'Berlin' in li.text_content():
            return True
    return False

html = requests.get("http://www.connecticum.de/Jobmessen/Recruiting-Karrieremesse-2014").content
dom = lxml.html.fromstring(html)

for entry in dom.cssselect('[id*=anker_exhibitor_detail_] a'):
    #print entry.get('title')
    #print entry.get('href')
    link = entry.get('href')
    if parse_exhibitor(link):
        print link
    #post = {
    #    'title': entry.cssselect('.entry-title')[0].text_content(),
    #    'author': entry.cssselect('.the-meta a')[0].text_content(),
    #    'url': entry.cssselect('a')[0].get('href'),
    #    'comments': int( entry.cssselect('.comment-number')[0].text_content() )
    #}
    #print entry
