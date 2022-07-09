#!/usr/bin/python3
cont = 1
loop = 0
while (cont):
    if loop == 0:
        answer = input("Do you want to play a game? (yes/no)").lower().strip()
    else:
        answer = input("Do you want to play again? (yes/no)")
    if answer == "yes":
        loop += 1
        answer = input("You are being chased by the FBI for no apparent reason. You run down the sidewalk with the FBI right on your tail, when you reach an intersection. Would you like to go LEFT or RIGHT?").lower().strip()
        if answer == "left":

            answer = input("You run down the sidewalk and reach a dead end. Would you like to CLIMB the wall in front of you or try to foolishly FIGHT the FBI?").lower().strip()
        
            if answer == "climb":
            
                answer = input("Great, you made it away safely! But once you scale the walls up to the building tops, you realize that the FBI is probably much stronger than you and follows you up to the rooftops. Now you have a choice between jumping to the glorious dream hotel on your RIGHT, or jumping to the safer car park area on your LEFT?").lower().strip()
        
                if answer == "right":
                    print("Sorry, you were hallucinating with all the adrenaline in your body. You calmly fall to your death as the FBI wonders what you were on.")
        
                elif answer == "left":
               
                    answer = input("You safely make it to the car park place and seem to lose the FBI, when you spot an FBI car unit rushing towards you. You can either try and break into another CAR, or you can get down and HIDE for your dear life.").lower().strip()
        
                    if answer == "car":
                        print("You try to break into a car and... fail. The FBI sniper shoots you from their car and then flexes on his fellow FBI agents that he could shoot a moving target from a moving standpoint. In other words, you died.")
            
                    elif answer == "hide":
                
                        answer = input("You hide and the FBI passes you... but once you get out of hiding immediately someone spots you and yells to the FBI to come and take you. Now you can either try and STOP the person yelling or just RUN.").lower().strip()
            
                        if answer == "stop":
                            print("i guess you can say you were too late to stop him... so yeah. game over.")
                                   
                        elif answer == "run":
                            print("you successfully run away from the FBI. Now your options to get home present themselves.")
                        
                            answer = input("You can try and RENT a car at the local center a few minutes way, or you can just WALK home.")
                        
                                   
                        else:
                            print("You did nothing and the FBI ran over you. Game over.")
                                   
                    else:
                        print("The FBI calmly ran over you.")
                                   
                                   
                else:
                    print("The FBI calmly pushed you off the building as you just stood there.")
                
                
            elif answer == "fight":
                print("that was probably not a good idea, because the FBI just easily tased you as you ran towards them and took you to your stay at jail that was for at least a couple hundred years.")
        
        
            else:
                print("Invalid choice, you just stood there like an idiot as the FBI punched you to death.")
        
        
        
        elif answer == "right":
            print("Great choice! Except... not a great choice. It turns out it was a dead end and the FBI caught up to you and killed you on the spot.")
    
    
    
        else:
            print("Invalid choice, you ran straight into a wall in front of you, the FBI caught up to you, and you were never seen again.")
    else:
        print("That's too bad!")
        cont = 0
