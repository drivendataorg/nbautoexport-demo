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
        "Frodo",
        "Gandalf",
        "Aragorn",
        "Legolas",
        "Gimli",
    ],
    steps = [
        "go_to_gondor",
        "walk_into_mordor",
        "go_to_mount_doom",
        "cast_ring_back_into_the_fiery_chasm_from_whence_it_came"
    ]
)


workflow.count_participants()




