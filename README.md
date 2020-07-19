# Hixe
Server Control

Use this module, if you have server

<img src = 'https://img.shields.io/badge/Server-Control-red' alt='bage4'>
<img src='https://img.shields.io/badge/Made%20by-R5whos-red' alt='bage2'>
<img src='https://img.shields.io/badge/version-1.0-9cf' alt='bage1'>
<img src='https://img.shields.io/badge/write%20on-python3.8-green' alt='bage3'>

# _How to use_

1 - if you want user open main web page:

<code>Hixe.sites(main='index.html')</code>

If user <b>run</b> your web page whis this file, code <b>redirection</b> to file whot you write in <code>main=''</code>
If you dont enter main, code find index.html in directory and <b>redirection</b> to them, but id you dont have index file code run any file in `Hixe.sites('main.html')`

2 - if you want localhost:

<code>Hixe.sites(lchost=8080)</code>

whis func <b>run localhost</b> whis <b>port</b> whot you write in <code>lchost=</code>

# _In soon time_

1 - adding a favicon for multiple sites at once

# _How to add .htaccess_

`Htaccess.settings(page_404 = '404.html', html_show='True', safe='True')`

page_404: 404 error page

html_show: if True in end link of web site was .html

safe: if True - Website protection against script injection else - Website dont protection against script injection
