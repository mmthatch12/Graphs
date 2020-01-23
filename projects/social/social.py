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
        for user in range(1, num_users+1):
            self.add_user(self.last_id)

        # Create friendships
        friend_combos = []
        for user in range(1, num_users+1):
            for friend in range(1, num_users+1):
                if user != friend:
                    friend_combos.append((user, friend))

        random.shuffle(friend_combos)

        total_friends = avg_friendships*num_users // 2

        for i in range(total_friends):
            self.add_friendship(friend_combos[i][0], friend_combos[i][1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # do a BFT, but store the paths as we go

        # create an empty queue
        que = Queue()
        # add a path to the starting node to the queue
        que.enqueue([user_id])
        # while the queue is not empty
        while que.size() > 0:
            # dequeue the first Path from the queue
            new_path = que.dequeue()
            vert = new_path[-1]
            # check if it's been visited
            # if not, mark it as visited
            if vert not in visited:
                # when unvisited node reached, add the path to the visited dict
                visited[vert] = new_path
                # add a path to each neighbor to the back of the queue
                for friend in self.friendships[vert]:
                    path_copy = new_path.copy()
                    path_copy.append(friend)
                    que.enqueue(path_copy)
        # when unvisited node reached add the path to visited dict
        # return visited dictionary
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths()
    print(connections)
