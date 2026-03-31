# pheromone_table.py

from config import DECAY_FACTOR

class PheromoneTable:

    def __init__(self):

        self.table = {}

    def reinforce(self, peer, value):

        self.table[peer] = self.table.get(peer, 0) + value


    def decay(self):

        for peer in self.table:

            self.table[peer] *= DECAY_FACTOR


    def get_best_candidates(self, threshold):

        return [

            peer

            for peer, pher in self.table.items()

            if pher >= threshold

        ]


    def show_table(self):

        print("\nPheromone levels:")

        for peer, value in self.table.items():

            print(f"path {peer} -> {value:.3f}")