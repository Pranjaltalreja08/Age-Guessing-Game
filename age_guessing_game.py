import random
def new_game(secret_age):
  if secret_age is None:
    secret_age=random.randint(18,30)
  try:
    user_guess=int(input("Enter your guess:"))
  except:
    print("Enter valid guess")
    return new_game(secret_age)

  if(user_guess==secret_age):
    print("congrations,correct guess")
    value=(input("press 0 to exit and any key to play again"))
    if value=='0':
     return
    else:
      new_game(None)
  elif(user_guess < secret_age):
     print("guess too low")
     new_game(secret_age)
  else:
     print("guess too high")
     new_game(secret_age)


if __name__=="__main__":
  new_game(None)

