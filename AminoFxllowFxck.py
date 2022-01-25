import amino
from pyfiglet import figlet_format
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor
init()
print(f"""{Fore.BLACK + Style.BRIGHT}
Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminofxllowfxck", font="drpepper"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
print(
"""
[1] Follow All Users
[2] Unfollow All Users
[3] Invite Followers To Chat
"""
)
select = int(input("-- Select::: "))


def follow_users():
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100, 2000, 250):
            online_users = sub_client.get_online_users(start=i, size=100)
            recent_users = sub_client.get_all_users(type="recent", start=i, size=100)
            all_users = [*online_users.profile.userId, *recent_users.profile.userId]
            if all_users:
                for user_id in all_users:
                    print(f"-- Followed to::: {user_id}")
                    executor.submit(sub_client.follow, user_id)
            else:
                break

def unfollow_users():
	with ThreadPoolExecutor(max_workers=50) as executor:
		while True:
			following_users_count = sub_clientget_user_info(userId=client.userId).followingCount
			if following_users_count > 0:
				for i in range(0, following_users_count, 100):
					followed_users = sub_clientget_user_following(userId=client.userId, start=i, size=100).userId
					if followed_users:
						for user_id in followed_users:
							print(f"-- Unfollowed from::: {user_id}")
							executor.submit(sub_clientunfollow, [user_id])

def invite_followers_to_chat():
    chats = sub_client.get_chat_threads(size=100)
    for z, title in enumerate(chats.title, 1):
        print(f"{z}.{title}")
    chat_id = chats.chatId[int(input("-- Select the chat::: ")) - 1]
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100, 2500, 1500):
            user_followers = sub_client.get_user_followers(
                userId=sub_client.profile.userId, start=i, size=100
            )
            for nickname, user_id in zip(followers.nickname, followers.userId):
                print(f"-- Invited::: {nickname}|{user_id} to chat"))
                executor.submit(sub_client.invite_to_chat, user_id, chat_Id)
        print("-- Invited all followers...")


if select == 1:
    follow_users()
    
elif select == 2:
    unfollow_users()


elif select == 4:
    invite_followers_to_chat()
