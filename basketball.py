from basketball_info import game_dictionary

# This method returns the team's status
def home_or_away(team_name):
  return game_dictionary[team_name]['status']


# Write a new method that returns a team's colors
def team_colors(team_name):
  color_one = game_dictionary[team_name]['team_colors'][0]
  color_two = game_dictionary[team_name]['team_colors'][1]
  return color_one + " and " + color_two


#Write a method that returns a string listing every player and their respective points
def player_points(team_name):
  list = ""
  list_length=0

  for x in range (0, len(game_dictionary[team_name]['players'])):
    list = list + game_dictionary[team_name]['players'][x]['name'] + " - " + str(game_dictionary[team_name]['players'][x]['points']) + " pts, "

  list_length=len(list)
  return list[:(list_length-2)] + "."


#This method should return all of the statistics for a player, given that players team and name
def player_stats(team, player_name):

  x =0
  list = ""
  list_length=0
  final_list=""

  for x in range (0,len(game_dictionary[team]['players'])):
    if player_name == (game_dictionary[team]['players'][x]['name']):
      for type, stat in (game_dictionary[team]['players'][x]).iteritems():
        list = list + "{}: {}\n".format(type.capitalize(), stat)
      print list

  list_length = len(list)
  final_list = list[:(list_length-1)]

  return final_list

# Return a player's shoe size.
def shoe_size(team, player_name):
  x = 0

  for x in range (0,len(game_dictionary[team]['players'])):
    if player_name == (game_dictionary[team]['players'][x]['name']):
      return game_dictionary[team]['players'][x]['shoe']


# Find the player on the team with the biggest shoe size and return their steals for the game
def big_shoe_stealer(team):
  player_list = []

  for x in range (0,len(game_dictionary[team]['players'])):
    player_list.append(game_dictionary[team]['players'][x]['shoe'])
  max_shoe = max(player_list)

  for x in range (0,len(game_dictionary[team]['players'])):
    if max_shoe == (game_dictionary[team]['players'][x]['shoe']):
      return game_dictionary[team]['players'][x]['steals']

