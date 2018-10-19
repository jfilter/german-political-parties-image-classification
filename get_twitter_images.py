import tweets_with_images

parties = [('cdu', 'cdu'), ('csu', 'csu'), ('afd', 'afd'),
           ('dielinke', 'link'), ('die_gruenen', 'grue'), ('fdp', 'fdp')]

for party, folder in parties:
    tweets = tweets_with_images.by_user(party, folder)
    print(tweets)  # tweets with images
