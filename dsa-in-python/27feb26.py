# name = "python"
# if name == "html" or "java":
#     print("login successful")
# else:
#     print("authentication failed")
    
   
# ## rock paper scissor game
# import random
# def get_choices():
#     players_choice = input("enter a choice rock, paper, scissor: ")
#     options = ["rock", "paper", "scissor"]
#     computers_choice  = random.choice(options)
#     choices = {"player":players_choice, "computer":computers_choice}
#     return choices
# def check_win(player, computer):
#     print(f" you choose {player} and the computer choose {computer}")
#     if player == computer:
#         return "It's a tie!"
#     elif player == "rock":
#         if computer == "scissor":
#             return "Rock smashes the scissor You Win !! "
#         else:
#             return "paper covers the rock You lose!!"
    
#     elif player == "paper":
#         if computer == "scissor":
#             return "paper covers rock You Win !! "
#         else:
#             return "scissor cut paper You lose!!"
#     elif player == "scissor":
#         if computer == "paper":
#             return "Rock smashes the scissor You Win !! "
#         else:
#             return "paper covers the rock You lose!!"
    
# check_win("rock", "paper")

# # def greeting():
# #     return "Hi"

# # response = greeting()
# # print(response)


#reverse an array
i = list(map(int, input("enter an array:")))
left = 0
right = len(i)-1
while left < right:
    i[left], i[right] = i[right], i[left]
    left += 1
    right -= 1
    
print(i)
