import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)
      
        # Create friendships
        friendships = []
      
        for user in range(1, self.last_id):
            for friend in range(user + 1, self.last_id + 1):
                friendships.append((user, friend))
        
        random.shuffle(friendships)

        total_friendships = num_users * avg_friendships
        pairs_needed = total_friendships // 2
        random_friendships = friendships[:pairs_needed]

        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = Queue()

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        queue.enqueue([user_id])

        while queue.size() > 0:
            curr_path = queue.dequeue()
            curr_node = curr_path[-1]

            if curr_node not in visited.keys(): 
                visited[curr_node] = curr_path
                edges = self.friendships[curr_node]
            
                for edge in edges:
                    path_copy = list(curr_path)
                    path_copy.append(edge)
                    queue.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
