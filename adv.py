from room import Room
from player import Player
from world import World

from collections import deque
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#################################################################################################################################################################
def traverse_rooms(player, world):
    visited_rooms = set()
    traversal_graph = {}
    prev_room_id = None
    # possible_direction = ['n', 's', 'e', 'w']

    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)
    print('player current', player.current_room)
        
#################################################################################################################################################################
  
    
    def get_opposite_direction(prev_direction):
        if prev_direction == 'n':
            return 's'
        if prev_direction == 's':
            return 'n'
        if prev_direction == 'w':
            return 'e'
        if prev_direction == 'e':
            return 'w'
    
    def update_graph(player, traversal_path):
        nonlocal prev_room_id 
        visited_rooms.add(player.current_room)
        current_exits = player.current_room.get_exits()
        
        if len(traversal_path) > 0:
            prev_direction = traversal_path[-1]

        

        #updats current room on graph
        for current_exit in current_exits:
            if player.current_room.id not in traversal_graph:
                traversal_graph[player.current_room.id] = {current_exit: '?'}
            else: 
                if current_exit in traversal_graph[player.current_room.id]:
                    continue
                else: 
                    traversal_graph[player.current_room.id][current_exit] = '?'
        
        # Updates previous and current rooms on graph
        if prev_room_id != None:
            opposite_of_prev_direction = get_opposite_direction(prev_direction)
            if traversal_graph[prev_room_id][prev_direction] == '?':
                traversal_graph[prev_room_id][prev_direction] = player.current_room.id
            if traversal_graph[player.current_room.id][opposite_of_prev_direction] == '?':
               traversal_graph[player.current_room.id][opposite_of_prev_direction] = prev_room_id
        
        prev_room_id = player.current_room.id

    def bfs(player, starting_room_id):
        visited = set()
        queue = deque()
        queue.append([starting_room_id])
        while len(queue) > 0:
            currentPath = queue.popleft()
            currentNode = currentPath[-1]
            if '?' in traversal_graph[currentNode].values():
                return currentPath
            if currentNode not in visited:
                visited.add(currentNode)
                print(currentNode)
                for neighbor in traversal_graph[currentNode].values():
                    newPath = list(currentPath)
                    newPath.append(neighbor)
                    queue.append(newPath)
#########################################################################################################################################

    update_graph(player, traversal_path)
    print(traversal_graph)
    while '?' in traversal_graph[player.current_room.id].values():
        possible_directions = [direction for direction in traversal_graph[player.current_room.id].keys() if traversal_graph[player.current_room.id][direction] == '?' ]
        random_direction = random.choice(possible_directions)
        new_direction = random_direction
        traversal_path.append(new_direction)
        player.travel(new_direction)
        update_graph(player, traversal_path)
        print(traversal_graph)
        if '?' not in traversal_graph[player.current_room.id].values():
            print(bfs(player, player.current_room.id))

    """ 
    visited_rooms = set()
    traversal_graph = {}
    prev_room_id = None
    

    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)


    update_graph(player, traversal_path)
    print(traversal_graph)
     """
    
    """ 
    while '?' in traversal_graph[player.current_room.id].values():
        possible_directions = [direction for direction in traversal_graph[player.current_room.id].keys() if traversal_graph[player.current_room.id][direction] == '?' ]
        random_direction = random.choice(possible_directions)
        new_direction = random_direction
        traversal_path.append(new_direction)
        player.travel(new_direction)
        update_graph(player, traversal_path)
        print(traversal_graph) 
        """

   

    """ 
    def recursive_dft_helper(direction, graph):
        player.travel(direction)
        traversal_path.append(direction)
        visited_rooms.add(player.current_room)
        update_graph(player, traversal_path)
        helper_exits = player.current_room.get_exits()
        print(traversal_graph)

        while '?' in traversal_graph[player.current_room.id].values():
            possible_directions = [direction for direction in traversal_graph[player.current_room.id].keys() if traversal_graph[player.current_room.id][direction] == '?' ]
            random_direction = random.choice(possible_directions)
            recursive_dft_helper( random_direction, traversal_graph) """

    """ 
    possible_directions_helper = [new_direction for new_direction in helper_exits if traversal_graph[player.current_room.id][new_direction] == '?' ]
    if len(possible_directions_helper) != 0:
        for possible_direction_helper in possible_directions_helper:
            recursive_dft_helper(possible_direction_helper, traversal_graph)
    else:
        return 
    """


    """ while '?' in traversal_graph[player.current_room.id].values():
        possible_directions = [new_direction for new_direction in player.current_room.get_exits() if traversal_graph[player.current_room.id][new_direction] == '?' ]
        random_direction = random.choice(possible_directions)
        recursive_dft_helper( random_direction, traversal_graph) 
    """
        
traverse_rooms(player, world)
    
"""     update_graph(player, traversal_path)

    new_direction = 'n'
    traversal_path.append(new_direction)
    player.travel(new_direction)
    update_graph(player, traversal_path)

    new_direction = 'n'
    traversal_path.append(new_direction)
    player.travel(new_direction)
    update_graph(player, traversal_path)
    print(traversal_graph)

    new_direction = 's'
    traversal_path.append(new_direction)
    player.travel(new_direction)
    update_graph(player, traversal_path)
    print(traversal_graph)

    new_direction = 's'
    traversal_path.append(new_direction)
    player.travel(new_direction)
    update_graph(player, traversal_path)
    print(traversal_graph)

    new_direction = 'n'
    traversal_path.append(new_direction)
    player.travel(new_direction)
    update_graph(player, traversal_path)
    print(traversal_graph)   """



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
""" player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.") """
