from yrconfigparser import MyConfigParser
import os
import sys
import praw
from datetime import datetime
import pickle



      
  
cfg_file=MyConfigParser()
path_to_cfg = os.path.abspath(os.path.dirname(sys.argv[0]))
path_to_cfg = os.path.join(path_to_cfg, 'banconfig.cfg')
cfg_file.read(path_to_cfg)

r = praw.Reddit(user_agent=cfg_file.get('reddit', 'user_agent'))
print 'Logging in as '+ cfg_file.get('reddit', 'username')
r.login(cfg_file.get('reddit', 'username'),
            cfg_file.get('reddit', 'password'))

bansub=r.get_subreddit(cfg_file.get('reddit','banSubreddit'))
checksub=r.get_subreddit(cfg_file.get('reddit','checkSubreddit'))

checksub_comments=checksub.get_comments(limit=999)
banned=[]
for x in bansub.get_banned():
    banned+=[x]
print(len(banned))
for x in checksub_comments:
    if x.author not in banned:
        try:
            print("Banning "+str(x.author))
            bansub.add_ban(x.author)
            banned+=[x.author]
        except:
            print("Failed Banning "+str(x.author))
            banned+=[x.author]



    
