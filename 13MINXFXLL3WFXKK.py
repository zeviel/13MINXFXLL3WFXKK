import amino
from concurrent.futures import ThreadPoolExecutor
print(f"""\033[38;5;45m
Script by zeviel
Github : https://github.com/zeviel
╋┏┓┏━━━┳━┳━┳━━┳━┳┳┓┏┳━━┳┓┏┳┓┏┳━━━┳┳━┳┳━━┳┓┏┳┳┳┳┓
┏┛┃┃┏━┓┃┃┃┃┣┃┃┫┃┃┣┓┏┫━┳┻┓┏┫┃┃┃┏━┓┃┃┃┃┃━┳┻┓┏┫┏┫┏┛
┗┓┃┗┛┏┛┃┃┃┃┣┃┃┫┃┃┣┛┗┫┏┛┏┛┗┫┗┫┗┫┏┛┃┃┃┃┃┏┛┏┛┗┫┗┫┗┓
╋┃┃┏┓┗┓┣┻━┻┻━━┻┻━┻┛┗┻┛╋┗┛┗┻━┻┳┫┗┓┣━┻━┻┛╋┗┛┗┻┻┻┻┛
┏┛┗┫┗━┛┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┗━┛┃
""")
client = amino.Client()
email = input("[Email]::: ")
password = input("[Password]::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"[{x}][{name}]")
com_id = clients.comId[int(input("[Select the community]::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
print("""
[1][Follow All Users]
[2][Unfollow All Users]
[3][Invite Followers To Chat]
""")
select = int(input("[Select]::: "))

def follow_online_users():
	followed = []
	while True:
		with ThreadPoolExecutor(max_workers=100) as executor:
			try:
				online_users = sub_client.get_online_users(
					start=0, size=100).profile.userId
				recent_users = sub_client.get_all_users(
					type="recent", start=0, size=100).profile.userId
				users = [*online_users, *recent_users]
				for user_id in followed:
					if user_id in users:
						users.remove(user_id)
				for user_id in users:
					followed.append(user_id)
					executor.submit(self.sub_client.follow, [user_id])
				print(f"[Following]...")
			except Exception as e:
				print(e)

def unfollow_from_followed_users():
	while True:
		with ThreadPoolExecutor(max_workers=100) as executor:
			following_count = sub_client.get_user_info(
					userId=sub_client.profile.userId).followingCount
			if following_count > 0:
				followed_users = sub_client.get_user_following(
					userId=sub_client.profile.userId, start=0, size=100).userId
				for user_id in followed_users:
					executor.submit(sub_client.unfollow, user_id)
			print("[Unfollowed from all users]")
	
def invite_followers_to_chat():
	chats = sub_client.get_chat_threads(size=100)
	for z, title in enumerate(chats.title, 1):
		print(f"[{z}][{title}]")
	chat_id = chats.chatId[int(input("[Select the chat]::: ")) - 1]
	while True:
		with ThreadPoolExecutor(max_workers=100) as executor:
			try:
				followers = sub_client.get_user_followers(
					userId=sub_client.profile.userId, start=0, size=100)
				for nickname, user_id in zip(followers.nickname, followers.userId):
					print(f"[Invited]::: [{nickname}][{user_id}]")
					executor.submit(sub_client.invite_to_chat, user_id, chat_id)
			except Exception as e:
				print(e)

if select == 1:
	follow_online_users()
elif select == 2:
	unfollow_from_followed_users()
elif select == 3:
	invite_followers_to_chat()
