#!/usr/bin/python
# -*- coding: UTF-8 -*-
from newspaper import Article
"""
Thuộc tính article, thông dụng: *

__class__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
__weakref__
additional_data
article_html
authors
build
build_resource_path
canonical_link *
clean_doc
clean_top_node
config
doc
download
download_exception_msg
download_state
extractor
fetch_images
get_parse_candidate
get_resource_path
has_top_image
html *
images * 
imgs *
is_media_news
is_parsed *
is_valid_body
is_valid_url
keywords
link_hash
meta_data *
meta_description *
meta_favicon
meta_img *
meta_keywords * 
meta_lang
movies
nlp
parse
publish_date
release_resources
set_article_html
set_authors
set_canonical_link
set_html
set_imgs
set_keywords
set_meta_data
set_meta_description
set_meta_favicon
set_meta_img
set_meta_keywords
set_meta_language
set_movies
set_reddit_top_img
set_summary
set_tags
set_text
set_title
set_top_img
set_top_img_no_check
source_url *
summary
tags
text *
throw_if_not_downloaded_verbose
throw_if_not_parsed_verbose
title *
top_image *
top_img *
top_node
url *
"""
url = 'https://vnexpress.net/12-000-nguoi-do-ve-cua-lo-4092705.html'
article = Article(url)
article.download()
article.parse()
# Xong rồi đấy, giờ lấy data thôi
#command = list(dir(article))
att = ["title","meta_description","canonical_link","images","imgs","meta_favicon","meta_img","url","top_image","top_img","source_url","meta_keywords"]

for i in att:
    print("[+] ",i," : ",getattr(article,i))
    print('-'*60)

print("Tiêu đề \n",article.title)
print("-------Nội dung-------\n",article.title)
content = article.text.split("\n")
for x in content:
    print(x)
print("-------Hết nội dung----\n")


