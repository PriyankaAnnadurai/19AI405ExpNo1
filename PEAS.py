import random
class VacuumCleanerAgent:
    def __init__(self): # Initialize the agent's state (location and dirt status)
        self.location = "A"  # Initial location (can be "A" or "B")
        self.dirt_status = {"A": True, "B": True}  # Initial dirt status (False means no dirt)
        self.performance=0
    def move_left(self): # Move the agent to the left if possible
        if self.location == "B":
            self.location = "A"
    def move_right(self): # Move the agent to the right if possible
        if self.location == "A":
            self.location = "B"
    def suck_dirt(self): # Suck dirt in the current location if there is dirt
        if self.dirt_status[self.location]:
            self.dirt_status[self.location] = False
            print(f"Sucked dirt in location {self.location}")
    def do_nothing(self): # Do nothing
        pass
    def perform_action(self, action): # Perform the specified action
        if action == "left":
            self.performance=self.performance-1
            self.move_left()
        elif action == "right":
            self.performance=self.performance-1
            self.move_right()
        elif action == "suck":
            self.performance=self.performance+10
            self.suck_dirt()
        elif action == "nothing":
            self.do_nothing()
        else:
            print("Invalid action")
    def print_status(self): # Print the current status of the agent
        print(f"Location: {self.location}, Dirt Status: {self.dirt_status}, ",end="")
        print(f"Perfomance Measure: {self.performance}")
# Example usage:
agent = VacuumCleanerAgent()
# Move the agent, suck dirt, and do nothing
agent.perform_action("left")
agent.print_status()
agent.perform_action("suck")
agent.print_status()
agent.perform_action("right")
agent.print_status()
agent.perform_action("suck")
agent.print_status()
agent.perform_action("nothing")
agent.print_status()
