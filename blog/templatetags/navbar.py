import feedparser
from django_yaba.blog.models import *
from django.conf import settings
from django import template

register = template.Library()

def parse_github():
    """ Grab latest commits from GitHub """
    d = feedparser.parse("http://github.com/%s.atom" % settings.GITHUB_USERNAME)
    e = d.entries[:5]
    commit = "<ul>"
    for x in e:
        commit += "<p><li>"
        commit += '<a href="%s">' % x['link']
        commit += x['title_detail']['value']
        commit += "</a>\n@ %s" % x['updated']
        commit += "</li></p>"
    commit += "</ul>"
    return commit

def sitename():
    sitename = settings.BLOG_NAME
    return {'sitename': sitename}

def sidebar():
    categories = Category.objects.all()
    link_list = Links.objects.all()
    commit = parse_github()
    sitename = settings.BLOG_NAME
    return {'link_list': link_list, 'commit': commit, 'sitename': sitename, 'categories': categories}

def main_nav():
    articles = Article.objects.all()
    return {'articles': articles}

register.inclusion_tag('sidebar.html')(sidebar)
register.inclusion_tag('main_nav.html')(main_nav)
register.inclusion_tag('sitename.html')(sitename)