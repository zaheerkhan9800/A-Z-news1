# DjangoEast

This website is developed based on `Django2.1` and `Python3.6`, the front-end style is driven by `Bootstrap`, supports responsive layout, and supports multiple terminal displays.

[![Build Status](https://travis-ci.org/mxdshr/DjangoEast.svg?branch=master)](https://travis-ci.org/mxdshr/DjangoEast) ![GitHub release](https ://img.shields.io/github/release/mxdshr/DjangoEast.svg) [![Requirements Status](https://requires.io/github/mxdshr/DjangoEast/requirements.svg?branch=master)]( https://requires.io/github/mxdshr/DjangoEast/requirements/?branch=master) ![GitHub](https://img.shields.io/github/license/mxdshr/DjangoEast.svg)

## 1. Main functions
-Support guest message function
-Support login and registration function
-Articles can be displayed in various forms such as date, category, label, etc.
-The use of xadmin on the background of the website makes up for the shortcomings of the original background
-Multi-level comments are supported at the bottom of the article, and the comment box supports rich text and `Markdown`
-Article writing support `Markdown` editor, article page display support code highlighting
-Support the reminder function of the logged-in user's message, new articles will be notified immediately
-Support to add book list and shadow list function, suitable for friends who like to read books and movies
-Supports site-wide keyword search, the search scope is article mark, content, and search result keyword highlighting
-Stay tuned for more features...

## 2. Local installation
### 2.1 Download website to local
```bash
git clone https://github.com/mxdshr/DjangoEast.git
```
### 2.2 Installation and Operating Environment
```bash
pip install -r requirements.txt
```
### 2.3 Modify the configuration file
Open the `django/settins/local.py` file, find the following code, and fill in the database information
```python
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'Database name',
        'USER':'Database account name',
        'PASSWORD':'Database account password',
        'PORT':'3306',
        'HOST':'localhost',
    }
}
```
### 2.4 Database migration
Terminal execution in the root directory of the website
```bash
python manage.py makemigrations
python manage.py migrate
```
### 2.5 Run the test
Terminal execution in the root directory of the website
```bash
python manage.py runserver 127.0.0.1:8000
```
## 3. Online deployment
Please refer to: [(super detailed) Django online deployment tutorial: Tencent Cloud + Ubuntu + Django + Uwsgi] (https://www.eastnotes.com/post/29)

## 4. Question exchange
I built a Django website exchange group, this group mainly discusses issues related to Django website. If you encounter any problems while learning `Django` or using `DjangoEast`, you can communicate in the group, and I will give you an answer. I will also share materials about Django learning in the group from time to time, including e-books, video tutorials, etc.

If you want to learn how to build a site with Django, you can add me on WeChat: `reborn0502`, note `Django`, I will pull you into the group.
## 4. Changelog

##second edition
### V2.1

-Articles can be placed in the recycle bin or draft box, and the articles will not be displayed on the front end
-Article categories and tags are arranged in reverse order according to the number of articles contained, and the display number is limited, and more hyperlinks are added to view more
-Optimize menu bar function, you can choose to show and hide menu items in the background
-Add my talk function, can post ideas in the background
-Optimize the display effect of archive pages, articles are folded and displayed by month

### V2.0
2019.5.7, the second version, a lot of new functions have been added, the front-end style has been greatly revised, and the functions have been gradually improved, as follows:
-Add my book list, my movie list function, benefits for book lovers and movie lovers-Supports login and registration functions, and can comment on articles after registration
-Added article comment function, comment box supports rich text, driven by `Ckeditor` editor, comment area supports secondary display
-New website message function is an extension of article comment
-The front end uses the `Bootstrap` framework instead of adjusting the CSS style to nausea and vomiting
-Login users can view the notification message notifications in the navigation bar, driven by `django-notifications-hq`
-The background supports website information settings, including title, keywords, description, etc.

##First edition
### V1.0
On 2019.3.7, the personal blog website developed by `Django2.0` and `Python3.6` went online for the first time, and was deployed on Tencent Cloud Server using `Nginx+Gunicorn`. The functions are still simple, as follows:
-The front-end template imitates the `Next` theme, and the background management is replaced by `Xadmin`
-Support article display by category, label, date
-Supports site-wide article search, which is jointly driven by the three libraries `Whoosh+Haystack+Jieba`, and the search content is limited to article title and article content
-The article addition and display also support `Markdown` syntax, which is jointly driven by `Markdown+Mdeditor` 2 libraries
-The code blocks in the article content support `syntax highlighting`, driven by the `Pygments` library