import aminofix as amino
import pyfiglet, concurrent.futures
from colorama import init, Fore, Back, Style
init()
print(Fore.BLACK + Style.BRIGHT)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminofxllowfxck", font="drpepper"))
client = amino.Client()
client.login(email=input("Email >>"), password=input("Password >>"))
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_Id = clients.comId[int(input("Select the community >> ")) - 1]
sub_client = amino.SubClient(comId=com_Id, profile=client.profile)
print(
    """[1] Follow All Users
[2] Unfollow All Users
[3] Delete All Followers
[4] Invite Followers To Chat"""
)
select = input("Select >> ")


def follow_all_users():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(100, 2000, 250):
            online_users = sub_client.get_online_users(start=i, size=100)
            recent_users = sub_client.get_all_users(type="recent", start=i, size=100)
            all_users = [*online_users.profile.userId, *recent_users.profile.userId]
            if all_users:
                for user_Id in all_users:
                    print(f"Followed to {user_Id}")
                    _ = [executor.submit(sub_client.follow, user_Id)]
            else:
                follow_all_users()
            print("Following...")


def unfollow_all_users():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100, 2000, 250):
            followed_users = sub_client.get_user_following(
                userId=sub_client.profile.userId, start=i, size=100
            )
            for nickname, user_Id in zip(
                followed_users.nickname, followed_users.userId
            ):
                print(f"Unfollowed {nickname}")
                _ = [executor.submit(sub_client.unfollow, user_Id)]
        print("Unfollowed All Users...")


def delete_all_followers():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100, 2000, 250):
            followers = sub_client.get_user_followers(
                userId=sub_client.profile.userId, start=i, size=100
            )
            for nickname, user_Id in zip(followers.nickname, followers.userId):
                print(f"Deleted {nickname} From Followers")
                _ = [executor.submit(sub_client.block, user_Id)]
                _ = [executor.submit(sub_client.unblock, user_Id)]
        print("Deleted all followers")


def invite_followers_to_chat():
    chats = sub_client.get_chat_threads(size=1000)
    for z, title in enumerate(chats.title, 1):
        print(f"{z}.{title}")
    chat_Id = chats.chatId[int(input("Select the chat >> ")) - 1]
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100, 2000, 250):
            user_followers = sub_client.get_user_followers(
                userId=sub_client.profile.userId, start=i, size=100
            )
            for nickname, user_Id in zip(followers.nickname, followers.userId):
                print(f"Invited {nickname}...")
                _ = [executor.submit(sub_client.invite_to_chat, user_Id, chat_Id)]
        print("Invited Followers")


if select == "1":
    follow_all_users()

elif select == "2":
    unfollow_all_users()

elif select == "3":
    delete_all_followers()

elif select == "4":
    invite_followers_to_chat()
