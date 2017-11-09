"""
The following are the constants needed to run the script
"""
URL_COL    = 9 # column number for URL to filter (starts at 0)
SKIP_FIRST = True # do not attempt to filter header
PARAMETERS = ["lang=fr", "lang=en", "lang=it", "lang=es", "lang=de",
              "mobile=1", "nomobile=1", "nomobile=0", "format=embed",
              "format=reader", "format=noaccess", "format=noaccess"]
              # list of supported/allowed GET paramters
SAFE_PARAM = ["%22", "%27", "\\", "'", "A=0"] # scrap allowed in URL
