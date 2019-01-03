title['container']
'mp4'


guessit.guessit()


guessit.guessit("my show 101 blah")
MatchesDict([('title', 'my show'), ('season', 1), ('episode', 1), ('episode_title', 'blah'), ('type', 'episode')])


guessit.guessit("my show 101 blah", options={'type': 'episode'})
MatchesDict([('title', 'my show'), ('season', 1), ('episode', 1), ('episode_title', 'blah'), ('type', 'episode')])