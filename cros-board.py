import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
from datetime import datetime
from time import sleep
from progress.bar import Bar


while True:

    now = datetime.now()
    d1 = now.strftime("%b %d %Y %H:%M:%S")
    print (d1)

    data = pd.read_csv('https://chromiumdash.appspot.com/cros/download_serving_builds_csv?deviceCategory=ChromeOS')
    df=data[data["eol"]==False]
    df =df[["board/model","cr_stable"]]
    df=df.reset_index(drop=True)


    omaha=pd.read_csv('https://omahaproxy.appspot.com/all')
    omaha=omaha[omaha["os"]=="cros"]
    stable=omaha[omaha["channel"]=="stable"]
    stable=stable["current_version"]
    stable=stable.reset_index(drop=True)

    df.loc[df.cr_stable != str(stable[0]), "cr_stable"] = Fore.RED+df.loc[df.cr_stable != str(stable[0]), "cr_stable"]+Fore.GREEN
    df.loc[df.cr_stable == str(stable[0]), "cr_stable"] = Fore.GREEN+df.loc[df.cr_stable == str(stable[0]), "cr_stable"]+Fore.GREEN
    print (df)
    print (Style.RESET_ALL)

    with Bar('Processing...') as bar:
        for i in range(100):
            sleep(1)
            bar.next()
