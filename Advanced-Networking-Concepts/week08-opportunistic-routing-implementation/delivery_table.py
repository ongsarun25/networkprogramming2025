# delivery_table.py

import random
import time

class DeliveryTable:
    """
    Maintains probability of successful delivery through each peer.
    """

    def __init__(self):
        self.table = {}
        self.last_update = {}

    def update_probability(self, peer, prob):
        self.table[peer] = prob
        self.last_update[peer] = time.time()

    def get_probability(self, peer):
        return self.table.get(peer, 0.0)

    def get_best_candidates(self, threshold):
        return [
            peer
            for peer, prob in self.table.items()
            if prob >= threshold
        ]

    def simulate_dynamic_update(self):
        """
        randomly adjust probabilities
        simulates node encounters
        """
        for peer in self.table:

            change = random.uniform(-0.1, 0.1)

            new_prob = self.table[peer] + change

            # clamp 0-1
            new_prob = max(0.0, min(1.0, new_prob))

            self.table[peer] = new_prob

    def show_table(self):
        print("\nDelivery probabilities:")
        for peer, prob in self.table.items():
            print(f"peer {peer} -> {prob:.2f}")