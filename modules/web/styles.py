import sass

prefix = 'pywebio-scope-'

style = """
  .pywebio {{
    padding: 0;
    margin: 0;
  }}
  .footer {{
    display: none;
  }}
  #{prefix}top {{
    display:flex;
    height: 50px;
    line-height: 50px;
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
  #{prefix}log_bar {{
    flex: 1;
    padding: 20px;
    background-color: #f7f7f7;
    height: calc(100vh - 61px);
    margin: 10px 10px 0 10px;
  }}
""".format(prefix=prefix)
style = sass.compile(string=style)
print('res:', style)
