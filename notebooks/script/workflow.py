#!/usr/bin/env python
# coding: utf-8

class Workflow:
    def __init__(self, participants, steps):
        self.participants = participants
        self.steps = steps
        
    def count_participants(self):
        return len(self.participants)


workflow = Workflow(
    participants = [
        "Boromir",
    ],
    steps = [
        "go_to_gondor",
        "use_the_ring",
    ]
)

