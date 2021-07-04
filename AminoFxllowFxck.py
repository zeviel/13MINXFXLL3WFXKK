import amino
import pyfiglet
import concurrent.futures
import stdiomask
from colorama import init, Fore, Back, Style
init()
print(Fore.BLACK + Style.BRIGHT)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminofxllowfxck", font="drpepper"))
print("Version = 2.1")
client = amino.Client()
email = input("Email/Почта >> ")
password = stdiomask.getpass("Password/Пароль >> ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
	print((f"{x}.{name}"))
communityid = clients.comId[int(input("Выберите сообщество/Select the community >> "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
print("""[1] Follow Users
[2] Unfollow All Users
[3] Delete All Followers
[4] Invite Followers To Chat""")
followfxckselect = input("Type Number/Введите цифру >> ")

def followusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
		for i in range(0, 20000, 2000):
			onlineusers = sub_client.get_online_users(start=i, size=100)
			recentusers = sub_client.get_all_users(type="recent", start=i, size=100)
			bannedusers = sub_client.get_all_users(type="banned", start=i, size=100)
			users = [*onlineusers.profile.userId, *recentusers.profile.userId, *bannedusers.profile.userId]
			if users:
				for userId in users:
					print(f"Followed to {userId}")
					_ = [executor.submit(sub_client.follow, userId)]
			else:
				followusers()
			print("Following")

def unfollowallusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		for i in range(0, 20000, 2000):
			followed = sub_client.get_user_following(userId=sub_client.profile.userId, start=i, size=100)
			if followed:
				for nickname, userId in zip(followed.nickname, followed.userId):
					print(f"Unfollowed {nickname}")
					_ = [executor.submit(sub_client.unfollow, userId)]
			print("Unfollowed all users")
			
def deleteallfollowers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		for i in range(0, 20000, 2000):
			followers = sub_client.get_user_followers(userId=sub_client.profile.userId, start=i, size=100)
			if followers:
				for nickname, userId in zip(followers.nickname, followers.userId):
					print(f"Deleted from followers {nickname}")
					_ = [executor.submit(sub_client.block, userId)]
					_ = [executor.submit(sub_client.unblock, userId)]
			print("Deleted all followers")
			
def invitefollowerstochat():
	chats = sub_client.get_chat_threads(size=1000)
	for z, title in enumerate(chats.title, 1):
		print(f"{z}.{title}")
	chatx = chats.chatId[int(input("Выберите чат/Select the chat >> "))-1]
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		for i in range(0, 20000, 2000):
			followers = sub_client.get_user_followers(userId=sub_client.profile.userId, start=i, size=100)
			if followers:
				for nickname, userId in zip(followers.nickname, followers.userId):
					print(f"Invited To Chat {nickname}")
					_ = [executor.submit(sub_client.invite_to_chat, userId, chatx)]
			print("Invited Followers")
				
if followfxckselect == "1":
	followusers()
	
elif followfxckselect == "2":
	unfollowallusers()
	
elif followfxckselect == "3":
	deleteallfollowers()
	
elif followfxckselect == "4":
	invitefollowerstochat()
