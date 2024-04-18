import sass

p = prefix = 'pywebio-scope-'

style = """
  .pywebio {{
    padding: 0;
    margin: 0;
  }}
  .footer {{
    display: none;
  }}
  #{p}top {{
    display:flex;
    height: 50px;
    line-height: 50px;
  }}
  #{p}state  {{
    flex: 1;
    * {{
      display:inline-block;
    }}
  }}
  #{p}title {{
    flex: 3;
  }}
  #{p}main {{
    display: flex;
  }}
  #{p}module_bar {{
    width: 80px;
  }}
  #{p}navigation_bar {{
    width: 110px;
    margin: 0 10px;
  }}
  #{p}content {{
    flex: 1;
    margin: 0 20px;
    padding: 10px;
    text-align: center;
    display: flex;
  }}
  #{p}menu_bar {{
    width: 800px;
  }}
  #{p}log_bar {{
    background-color: #f7f7f7;
  }}
  #{p}img_show {{
    flex:1;
    padding: 10px;
    text-align: center;
      img {{
        margin: 5px;
        width: 100%;
      }}
  }}



  .btn-primary {{
    color: #000;
    background-color: #fff;
    border: None;
  }}
  details {{
    border: none;
  }}
""".format(p=p)
style = sass.compile(string=style)
