from user_interface import inter

x = inter()

if x == 1:
    from add_game import add

elif x == 2:
    from available_games import available

elif x == 3:
    from order_game import order

elif x == 4:
    from games_that_well_appear_soon import soon

elif x == 5:
    from registration import regi

else:
    from user_date import users
