import sass

prefix = 'pywebio-scope-'

style = """
  #{prefix}top {{
    display:flex;
  }}
  #{prefix}state  {{
    flex: 1;
    * {{
      display:inline-block;
    }}
  }}
  #{prefix}title {{
    flex: 3;
  }}
  #{prefix}content {{
    display: flex;
  }}
  #{prefix}menu_bar {{
    margin-left: 20px;
  }}

""".format(prefix=prefix)
style = sass.compile(string=style)
print('res:', style)
