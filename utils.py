import lxml.html

def is_html(html):
    try: 
        return True if lxml.html.fromstring(html).find('.//*') else False
    except:
        return False