import random

class MovieRemote:
    """Simulates a simple movie remote control."""
    def mute(self):
        print("Muting video.")

    def fast_forward(self, seconds):
        print(f"Fast-forwarding video by {seconds} seconds.")

    def skip(self, seconds):
        print(f"Skipping {seconds} seconds.")

    def status(self):
        print("Displaying video status.")

class MovieRemoteAI:
    """AI-enhanced remote that learns user preferences."""
    def __init__(self, remote):
        self.remote = remote
        self.action_log = []

    def log_action(self, action, *args):
        self.action_log.append((action, args))
        print(f"Action logged: {action} with arguments {args}")

    def learn_preferences(self):
        """Determine the most commonly used action."""
        if not self.action_log:
            return None
        actions = [log[0] for log in self.action_log]
        return max(set(actions), key=actions.count)

    def mute(self):
        self.remote.mute()
        self.log_action('mute')

    def fast_forward(self, seconds):
        self.remote.fast_forward(seconds)
        self.log_action('fast_forward', seconds)

    def skip(self, seconds):
        self.remote.skip(seconds)
        self.log_action('skip', seconds)

    def status(self):
        self.remote.status()
        self.log_action('status')

    def perform_preferred_action(self):
        """Perform the action the user does most often."""
        preferred_action = self.learn_preferences()
        if preferred_action:
            print(f"Performing preferred action: {preferred_action}")
            if preferred_action == 'mute':
                self.mute()
            elif preferred_action == 'fast_forward':
                self.fast_forward(random.randint(1, 600))  # Random fast forward
            elif preferred_action == 'skip':
                self.skip(random.randint(1, 600))  # Random skip
            elif preferred_action == 'status':
                self.status()
        else:
            print("No preferred action learned yet.")

# Example Usage
remote = MovieRemote()
ai_remote = MovieRemoteAI(remote)

ai_remote.status()
ai_remote.mute()
ai_remote.fast_forward(300)
ai_remote.skip(600)
ai_remote.status()

# Perform the preferred action based on the logged actions
ai_remote.perform_preferred_action()
import random