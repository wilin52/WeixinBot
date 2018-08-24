import random

def autoReply(word):
	if replySame(word):
		return word
	else:
		return replyEmoji()


def replySame(word):
	
	if ("你好" in word) or ("hello" in word) or ("沙雕" in word) or ("傻逼" in word):
		return True
	else:
		return False

def replyEmoji():
	r = random.randint(1,7)
	if r == 1:
		return "[微笑]"
	elif r == 2:
		return "[笑哭]"
	elif r == 3:
		return "[皱眉]"
	elif r == 4:
		return "[奸笑]"
	elif r == 5:
		return "[机智]"
	elif r == 6:
		return "[捂脸]"
	else:
		return "我还没训练好，其他的都不知道怎么回答"
