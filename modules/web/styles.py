import sass

p = prefix = 'pywebio-scope-'

style = """
  html, body {{
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
  }}
  .container {{
    margin: 0 !important;
    padding: 0 !important;
  }}
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
    box-shadow: 0 0 8px rgba(0, 0, 0, .2);
  }}
  #{p}state  {{
    flex: 1;
    * {{
      display:inline-block;
    }}
    button {{
      margin-left: 20px;
      border: 1px solid #cdcdcd;
    }}
  }}
  #{p}title {{
    flex: 3;
  }}
  #{p}main {{
    height: calc(100vh - 60px);
    display: flex;
  }}
  #{p}module_bar {{
    padding-top: 5px;
    width: 70px;
    border-right: 1px solid #cdcdcd;
  }}
  #{p}navigation_bar {{
    padding-top: 5px;
    width: 110px;
    margin: 0 10px;
    border-right: 1px solid #cdcdcd;
  }}
  #{p}content {{
    flex: 1;
    margin: 0 20px;
    padding: 10px;
    text-align: center;
    display: flex;
  }}
  #{p}menu_bar {{
    flex:1;
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
