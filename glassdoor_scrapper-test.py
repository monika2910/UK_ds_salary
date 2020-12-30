

import glassdoor_scrapper as gs
import pandas as pd

path = "/Users/vinay/Downloads/scraping-glassdoor-selenium-master"
df = gs.get_jobs('data scientist', 2000, False)


