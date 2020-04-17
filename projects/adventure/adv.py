from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Useful commands:
    # player.current_room.id
    # player.current_room.get_exits()
    # player.travel(direction)

# 1. Travel in random direction
# 2. Add rooms as you go if they have not been visited
# 3. Convert question marks to room id's
# 4. If you reach a dead end, backtrack to last question mark
# 5. Go back to step 1

class Navigation:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id):
        get_exits = player.current_room.get_exits()

        exits = {}

        for direction in get_exits:
            self.rooms[room_id] = exits
            self.rooms[room_id][direction] = "?"

    def set_direction(self, random_direction):
        opposite_direction = None

        if random_direction == "n":
            opposite_direction = "s"
        elif random_direction == "s":
            opposite_direction = "n"
        elif random_direction == "w":
            opposite_direction = "e"
        elif random_direction == "e":
            opposite_direction = "w"

        return opposite_direction


    def bfs(self, starting_room, search):
        pass

    def traverse_map(self, room_id):
        room_id = player.current_room.id
        curr_id = None
        question_mark_arr = []

        # Adds room if not in dictionary
        if room_id not in self.rooms.keys():
            self.add_room(room_id)
        
        while '?' in self.rooms[room_id].values():
            for key, value in self.rooms[room_id].items():
                if value == "?":
                    question_mark_arr.append(key)

            random_direction = random.choice(question_mark_arr)

            opposite_direction = self.set_direction(random_direction)

            prev_room_id = player.current_room.id

            player.travel(random_direction)
            traversal_path.append(random_direction)

            curr_id = player.current_room.id

            question_mark_arr = []

            if self.rooms[prev_room_id][random_direction] == "?" or self.rooms[curr_id][opposite_direction] == "?":
                self.rooms[prev_room_id][random_direction] = curr_id
                self.rooms[curr_id][opposite_direction] = prev_room_id
            
            if len(self.rooms) == 500:
                break

            while '?' not in self.rooms[curr_id].values():
                print("Deadend")

            
        

navigate = Navigation()

navigate.traverse_map(player.current_room.id)

# TRAVERSAL TEST
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
