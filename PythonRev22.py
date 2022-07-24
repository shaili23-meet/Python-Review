def create_youtube_video(title, description):
	youtubeDict = {"title":title, "description":description, "likes":0, "dislike":0, "comments":{}}
	return youtubeDict


def like(youtubeDict):
	if "likes" in youtubeDict:
		youtubeDict["likes"] += 1
	return youtubeDict


def dislike(youtubeDict):
	if "dislike" in youtubeDict:
		youtubeDict["dislike"] += 1
	return youtubeDict


def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo


ytDict = create_youtube_video("Brooklyn99 best cold opens", "best tv show ever")
for i in range (495):
	ytDict= like(ytDict)
ytDict = dislike(ytDict)
ytDict = add_comment(ytDict, "shaiTheBest", "b99 is the best show ever")
print(ytDict)