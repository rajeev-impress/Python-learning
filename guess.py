
word = "google"
guess = ""
count = 1
while guess != word and count <=3 :
    guess = input("enter the guess in small case: ")
    count +=1
        
if guess == word and count <=3:
    print(f'Your WIN with in {count} attempts of max 3');  

else:
    print("YOU LOOSE")
