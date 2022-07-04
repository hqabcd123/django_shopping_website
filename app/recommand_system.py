import sqlite3
import pandas as pd

con = sqlite3.connect('../db.sqlite3')
cursor = con.cursor()