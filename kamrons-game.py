#!/usr/bin/python3
def get_answer(prompt):
    return input(prompt + " ").strip().lower()

cont = 1
loop = 0
while (cont):
    if loop == 0:
        answer = get_answer("Do you want to play a game? (yes/no)")
        #answer = input("Do you want to play a game? (yes/no)").lower().strip()
    else:
        answer = get_answer("Do you want to play again? (yes/no)")
    if answer == "yes":
        loop += 1
        answer = get_answer("You are being chased by the FBI for no apparent reason. You run down the sidewalk with the FBI right on your tail, when you reach an intersection. Would you like to go LEFT or RIGHT?")
        if answer == "left":

            answer = get_answer("You run down the sidewalk and reach a dead end. Would you like to CLIMB the wall in front of you or try to foolishly FIGHT the FBI?")
        
            if answer == "climb":
            
                answer = get_answer("Great, you made it away safely! But once you scale the walls up to the building tops, you realize that the FBI is probably much stronger than you and follows you up to the rooftops. Now you have a choice between jumping to the glorious dream hotel on your RIGHT, or jumping to the safer car park area on your LEFT?")
        
                if answer == "right":
                    print("Sorry, you were hallucinating with all the adrenaline in your body. You calmly fall to your death as the FBI wonders what you were on.")
        
                elif answer == "left":
               
                    answer = get_answer("You safely make it to the car park place and seem to lose the FBI, when you spot an FBI car unit rushing towards you. You can either try and break into another CAR, or you can get down and HIDE for your dear life.")
        
                    if answer == "car":
                        print("You try to break into a car and... fail. The FBI sniper shoots you from their car and then flexes on his fellow FBI agents that he could shoot a moving target from a moving standpoint. In other words, you died.")
            
                    elif answer == "hide":
                
                        answer = get_answer("You hide and the FBI passes you... but once you get out of hiding immediately someone spots you and yells to the FBI to come and take you. Now you can either try and STOP the person yelling or just RUN.")
            
                        if answer == "stop":
                            print("i guess you can say you were too late to stop him... so yeah. game over.")
                                   
                        elif answer == "run":
                            print("you successfully run away from the FBI. Now your options to get home present themselves.")
                        
                            answer = get_answer("You can try and RENT a car at the local center a few minutes way, or you can just WALK home.")
                            
                            if answer == "rent":
                                print("You successfully rent a car but realize you don't know how to drive a car. You die in an epic movie-scene car crash.")
                                
                            if answer == "walk":
                                print("You walk home before stopping at a go-kart rent place. You rent one and get on your way to your home.")
                                answer = get_answer("You get stopped by the FBI on the way there and threaten to kill you. You can now either make a RUN for it, or try to TALK with them.")
                                
                                if answer == "run":
                                    print("you weren't fast enough.")
                                
                                if answer == "talk":
                                    print("You manage to get some information out of them.")
                                    print("The story goes that your mother is secretly a bank robber. She got caught, and says that she gave you all the money.")
                                    answer = get_answer("You say that it's not true, but when you say that, the FBI automatically assume that you are lying and threaten to kill you, again. Now your options are to try and RUN, beg for MERCY, or try to convince them with PROOF.")
                                    
                                    if answer == "run":
                                        print("you weren't fast enough.")
                                        
                                    if answer == "mercy":
                                        print("You beg for mercy a lot. And when I mean a lot, I mean A LOT. The FBI finally accepts, but when they ask you a question, you fall down in exhaustion. Now the FBI thinks you are faking and threatens to kill you. Your choices now are to offer them PROOF, or to RUN.")
                                        
                                        if answer == "proof":
                                            print("You offer them your address to investigate for the stolen money. They let you into their vehicle when you realize that... they aren't going to the right place! You tell them the address again, the driver nods, but doesn't change directions. Then it hits you: These people aren't the real FBI! You panic in your brain but stay completely still. At any moment they could kill you and no one would ever know! You manage to calm yourself and figure out two options: try and ESCAPE or PLAY along.")
                                            
                                            if answer == "escape":
                                                print("you weren't fast enough.")
                                                
                                            if answer == "play":
                                                answer = get_answer("You play along for a little while until the so called 'FBI' stopped at an abandoned warehouse and said 'wait here'. Now you have another choice: to try and make a RUN for it here or to FIND out exactly what is up here.")
                                                if answer == "find":
                                                    answer = get_answer("You managed to get no information whatsoever out, but once you entered the warehouse, you saw that it was a meeting room for illegal shipping services. You can now either try and CALL the cops or PLAY along even more.")
                                                    
                                                    if answer == "play":
                                                        print("You play along even more before finally finding an opportunity to make a dash for it without them noticing. Right as they were out of sight and you were in their van alone, you break out immediatley and make a run for it. The fake FBI don't notice, so you think you are clear. You run before finally setlling down somewhere safe where the fake FBI won't find you. You tried calling the police, but there was no signal. You checked for nearby signals, and you found one. You luckily managed to connect to it, but unluckily it was only 10 minutes of free wifi. You quickly called 911, telling them your location and details, and you managed to arrest the fake FBI agents. The police awarded you with a ride home and the rest is history.")
                                                        print("I would like to thank you for playing, because this is one of the winning endings of this game. Thank you, and simply putting it, THE END.")
                                                    
                                                    if answer == "call":
                                                        print("You manage to excuse yourself to a port-o-potty and call the cops. Then you realize the flaw in your plan - the signal. Apparently the fake FBI drove so far that even the cellular signal couldn't reach. Now you were left with no hopes. You searched and searched for a way, but without internet, it was useless. You thought that you should probably get out now, but after one last search, a second too much was wasted, and the fake FBI began to speculate that maybe you weren't actually going to the bathroom, because normally even a number-two doesn't take 20 minutes. The FBI banged on the door and took the door down, faster than you could put your phone away and act like you were going to the bathroom. The FBI had found out what you were doing, and shot you on the spot. At least they have to clean up another port-o-potty with a corpse in it, I guess.")
                                                        
                                                    else:
                                                        ("Looks like you were confused. You just sat there in the truck for the rest of eternity, until the fake FBI just got tired of you and used you as fire fuel.")
                                                        
                                            
                                        if answer == "run":
                                            print("You weren't fast enough, duh.")
                                    
                                    if answer == "proof":
                                        print("You manage to show them proof that the bank robber is not you mother with a picture of your mother. They agree that it was not your mother and ask you if you would like to join their investigation.")
                                        answer = get_answer("Now your decision: if you want to JOIN their investigation or just go HOME after this long day being hunted by the FBI.")
                                        if answer == "home":
                                            print("It looks like this crazy adventure is coming to an end. It is now evening at your house and you look out the window, stare into space, and pass out before your head hits the pillow.")
                                            print("THE END")
                                        
                                        if answer == "join":
                                            print("You decide to join them on their investigation. You offer them your address to investigate for the stolen money. They let you into their vehicle when you realize that... they aren't going to the right place! You tell them the address again, the driver nods, but doesn't change directions. Then it hits you: These people aren't the real FBI! You panic in your brain but stay completely still. At any moment they could kill you and no one would ever know! You manage to calm yourself and think that maybe if you excuse yourself, you can call the cops and they will handle it! So you do just that.")
                                            print("You excuse yourself to the bathroom at a resturant and manage to call the cops. The cops come and recognize that the FBI agents don't have proper badges. The fake FBI agents are now in prison! And thanks to you. The cops reward you with... a ride home. An actual one. So you live happily ever after and this adventure became only a story that you tell at parties.")
                                            print("We regret to inform you that this story has come to a close, but if you would like to play again and discover all the endings and funny passages, go ahead and type 'yes' down below. Now without further ado, I'm just going to say, THE END, and thank you for playing.")
                                        
                                    else:
                                        print("Looks like you were confused. You stood there like a dummy until nightfall when the FBI left, and then you just stood there for the rest of your life, slowly rotting to a crisp of ash.") 
                                        
                                else:
                                     print("Looks like you were confused. You spoke nothing or did nothing and the FBI just assumed you guilty and killed you, case closed.")
                                        
                            else:
                                print("Looks like you were confused. You did nothing for the rest of your life and died of either starvation of old age. I wouldn't know.")
                                        
                        else:
                            print("Looks like you were confused. You did nothing and the FBI ran over you. Game over.")
                                   
                    else:
                        print("Looks like you were confused. The FBI calmly ran over you.")
                                   
                                   
                else:
                    print("Looks like you were confused. The FBI calmly pushed you off the building as you just stood there.")
                
                
            elif answer == "fight":
                print("that was probably not a good idea, because the FBI just easily tased you as you ran towards them and took you to your stay at jail that was for at least a couple hundred years.")
        
        
            else:
                print("Looks like you were confused. you just stood there like an idiot as the FBI punched you to death.")
        
        
        
        elif answer == "right":
            print("Great choice! Except... not a great choice. It turns out it was a dead end and the FBI caught up to you and killed you on the spot.")
    
        else:
            print("Looks like you were confused. you ran straight into a wall in front of you, the FBI caught up to you, and you were never seen again.")
    else:
        if loop == 0:
            print("Okay, maybe next time!")
        else:
            print("Okay, maybe next time!")
            print("GAME OVER")
        cont = 0
