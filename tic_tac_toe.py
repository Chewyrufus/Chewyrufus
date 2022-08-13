def tic_tac_toe():
    
    #first - to set the start variables and import required modules
    
    cont = 'Y'
    active = [1,2,3,4,5,6,7,8,9]
    turn = 'X'
    
    import time
    from IPython.display import clear_output

    # Now to define all the functions
    
    def print_board(active):
        clear_output()
        print('   |   |   ')
        print(' {} | {} | {} '.format(active[6],active[7],active[8]))
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' {} | {} | {} '.format(active[3],active[4],active[5]))
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' {} | {} | {} '.format(active[0],active[1],active[2]))
        print('   |   |   ')
        
        
    
    def pick_player():
        player_1 = ':D'
        player_2 = 'D;'
        while player_1 not in ['X','O']:
               
            player_1 = input('Which side do you want to play, player 1? X or O: ').upper()
        
            if player_1 not in ['X','O']:
            
                print ("You must select 'X' or 'O', you selected {}".format(player_1))
            
                time.sleep(1)
                  
        return player_1
    
    def turn_counter(turn):
        if turn == 'X':
            return 'O'
        if turn == 'O':
            return 'X'
        
        
    def position_req(active,turn):
    
    
        remaining = [i for i in active if i not in ('X','O')]
        print(remaining)
        time.sleep(2)
    
    
        position = 12
    
        while position not in active:
            position = input('Player {}: Please enter which square you would like to place your counter in : '.format(turn))
        
            if not position.isdigit():
                print('You must select a number ')
            
            
                continue
            
        
            if int(position) not in active:
                print('You must select from one of the remaining places on the board {}'.format(remaining))
                time.sleep(2)
                
            else:
                position = int(position)
                active[position-1] = turn
                return active    
    
    def check_win(active,turn):
        if (active[0]==active[1]==active[2] 
        or active[3]==active[4]==active[5] 
        or active[6]==active[7]==active[8]
        or active[0]==active[3]==active[6] 
        or active[1]==active[4]==active[7] 
        or active[2]==active[5]==active[8] 
        or active[0]==active[4]==active[8] 
        or active[2]==active[4]==active[6]):
            print('{} has won the game!'.format(turn))
            return 'win'
        else:
            count=0
            for item in active:
                if type(item) == int:
                    count+=1
            if count == 0:
                print('This is a draw!')
                return 'win'
            if count >=1:
                return 'no_win'
                
        
        
        
    def restart_game():
        restart = 'X'
        while restart not in ['Y','N']:
            restart = input('Do you want to continue? (Y/N) :').upper()
            if restart not in ['Y','N']:
                print("You must select from 'Y' or 'N'")
                time.sleep(1)
                continue
            else:
                return restart
            
            
    # now to sequence the game
    
    while cont =='Y':
        active = [1,2,3,4,5,6,7,8,9]
        pick = 'B'
        win = 'no_win'
        while win == 'no_win':
            if pick not in ['X','O']:
                pick = pick_player()
            else:
        
                print_board(active)
        
                turn = turn_counter(turn)
        
                active = position_req(active,turn)
        
                print_board(active)
        
                win = check_win(active,turn)
        
        cont = restart_game()
