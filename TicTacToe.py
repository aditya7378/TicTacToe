board =['', '', '', '', '', '', '', '', '', '']
     def display_board (board):print ('\n' * 10)
  print ('   |     |')
  print ('' + board[1] + '   | ' + board[2] + '    | ' + board[3])
  print ('   |     |')
  print ('-------------')
  print ('   |     |')
  print ('' + board[4] + '   |  ' + board[5] + '   | ' + board[6])
  print ('   |     |')
  print ('-------------')
  print ('   |     |')
  print ('' + board[7] + '   | ' + board[8] + '    | ' + board[9])
  print ('   |     |')
#################################
     def player_input ():mark = '' while mark
!='x' and mark != 'o':
  mark = input ('Player 1 please choose X or O :') player1 = mark if player1
  == 'x':
    player2 = 'o'
    else
  :
    player2 = 'x' return (player1, player2)
######################################
     def player_choice (board):position = 0 while position
not in[1, 2, 3, 4, 5, 6, 7, 8, 9]:
     position = int (input ('Please enter from 1-9')) return position
#######################################
  def
place_marker (board, p1, position1):
  board[position1] = p1
######################################
def win_check (board, mark):
return ((board[1] == mark and board[2] == mark and board[3] == mark) or
	(board[4] == mark and board[5] == mark and board[6] == mark) or
	(board[7] == mark and board[8] == mark and board[9] == mark) or
	(board[1] == mark and board[4] == mark and board[7] == mark) or
	(board[2] == mark and board[5] == mark and board[8] == mark) or
	(board[3] == mark and board[6] == mark and board[9] == mark) or
	(board[1] == mark and board[5] == mark and board[9] == mark) or
	(board[3] == mark and board[5] == mark and board[7] == mark))
##########################################
     def
     space_check (board, position):
  return
  board[position] == ''
#FUNCTION TO CHECK THE FULL BOARD  CHECK
def full_board_check (board):
for i
in range (1, 10):
  if space_check
  (board, i):
    return False
    else
  :
    return True count = 1 p1, p2 = player_input ()while True
    :
#display_board(board)
#p1,p2=player_input()
      print (p1) print (p2) if count
      %2 != 0:
	print ('player 1 will play')
	  display_board (board)
	  count += 1
	  position1 = player_choice (board)
	  place_marker (board, p1, position1)
	  display_board (board) if win_check
	(board, p1):
	  display_board (board) print ('player 1 has won') break
#else	/* : */
#if full_board_check(board):
#display_board(board)
#print('game tie..!!!1')
#break
#else	/* : */
#a=p2
	    else
	:
	  print ('player 2 will play')
	    display_board (board)
	    count += 1
	    position1 = player_choice (board)
	    place_marker (board, p2, position1)
	    display_board (board) if win_check
	  (board, p2):
	    display_board (board) print ('player 2 has won') break
#else	/* : */
#if full_board_check(board):
#display_board(board)
#print('game tie..!!!1')
#break
#else	/* : */
#
