import simplegui
import random

# Global variables
regions = ["Region A", "Region B", "Region C", "Region D", "Region E"]
equality_scores = {region: 50 for region in regions}  # Starting equality levels
resources = 100  # Player's initial resource pool
log = []  # Game log for events and decisions

# Trash collection variables
player_pos = [400, 200]  # Initial position of the player
player_size = 20  # Size of the player character
trash_positions = []  # List of trash positions
trash_size = 10  # Size of trash items
score = 0  # Player's score

# Helper functions
def log_event(event):
    """Adds an event to the game log."""
    log.insert(0, event)
    if len(log) > 10:  # Limit log size
        log.pop()

def spawn_trash():
    """Spawns a trash item at a random position."""
    x = random.randint(0, 780)
    y = random.randint(0, 380)
    trash_positions.append([x, y])

def check_collision():
    """Checks if the player collects trash."""
    global score, resources
    for trash in trash_positions[:]:
        if (abs(player_pos[0] - trash[0]) < (player_size + trash_size) / 2 and
            abs(player_pos[1] - trash[1]) < (player_size + trash_size) / 2):
            trash_positions.remove(trash)
            score += 1
            resources += 5  # Reward resources for collecting trash
            log_event("Collected trash! Gained 5 resources.")
            spawn_trash()  # Replace the collected trash with a new one

# Event handlers for resource allocation
def allocate_resources(region):
    global resources
    if resources >= 10:
        equality_scores[region] += random.randint(5, 15)
        resources -= 10
        log_event(f"Allocated 10 resources to {region}. Equality increased!")
    else:
        log_event("Not enough resources to allocate!")

def random_event():
    global resources
    region = random.choice(regions)
    event_type = random.choice(["bonus", "penalty"])
    
    if event_type == "bonus":
        bonus = random.randint(5, 20)
        equality_scores[region] += bonus
        log_event(f"Good news! {region} gained {bonus} equality points.")
    else:
        penalty = random.randint(5, 20)
        equality_scores[region] -= penalty
        log_event(f"Challenge! {region} lost {penalty} equality points.")
    
    # Random resource gain
    if random.random() < 0.3:
        gain = random.randint(5, 15)
        resources += gain
        log_event(f"Resource gain! You found {gain} extra resources.")

def check_win():
    """Checks if the player has won the game."""
    if all(score >= 80 for score in equality_scores.values()):
        log_event("Victory! All regions have achieved harmony and equality.")
    elif any(score <= 0 for score in equality_scores.values()):
        log_event("Game Over! One region fell into chaos.")

def restart_game():
    global equality_scores, resources, log, score, trash_positions
    equality_scores = {region: 50 for region in regions}
    resources = 100
    log = []
    score = 0
    trash_positions = []
    for _ in range(5):  # Spawn initial trash
        spawn_trash()
    log_event("Game restarted! Let's bring harmony again.")

# Event handlers for player movement
def keydown(key):
    """Handles player movement."""
    if key == simplegui.KEY_MAP['left']:
        player_pos[0] -= 10
    elif key == simplegui.KEY_MAP['right']:
        player_pos[0] += 10
    elif key == simplegui.KEY_MAP['up']:
        player_pos[1] -= 10
    elif key == simplegui.KEY_MAP['down']:
        player_pos[1] += 10

# Drawing handler
def draw(canvas):
    global resources

    # Draw title and resources
    canvas.draw_text("Peaceformers: The Quest for Equality", (50, 30), 24, "White")
    canvas.draw_text(f"Resources: {resources}", (50, 60), 20, "Yellow")
    canvas.draw_text(f"Score: {score}", (650, 30), 20, "Yellow")

    # Draw regions and their equality scores
    for i, region in enumerate(regions):
        y = 100 + i * 50
        canvas.draw_text(f"{region}: {equality_scores[region]}", (50, y), 20, "Cyan")

    # Draw player
    canvas.draw_circle(player_pos, player_size / 2, 2, "White", "Blue")

    # Draw trash
    for trash in trash_positions:
        canvas.draw_circle(trash, trash_size / 2, 2, "Gray", "Green")

    # Draw log
    canvas.draw_text("Event Log:", (400, 60), 20, "Green")
    for i, event in enumerate(log[:5]):  # Show last 5 events
        y = 100 + i * 20
        canvas.draw_text(event, (400, y), 16, "White")

    # Check collision and win/lose conditions
    check_collision()
    check_win()

# Create frame
frame = simplegui.create_frame("Peaceformers", 800, 400)

# Register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.add_button("Allocate to Region A", lambda: allocate_resources("Region A"), 150)
frame.add_button("Allocate to Region B", lambda: allocate_resources("Region B"), 150)
frame.add_button("Allocate to Region C", lambda: allocate_resources("Region C"), 150)
frame.add_button("Allocate to Region D", lambda: allocate_resources("Region D"), 150)
frame.add_button("Allocate to Region E", lambda: allocate_resources("Region E"), 150)
frame.add_button("Trigger Random Event", random_event, 150)
frame.add_button("Restart Game", restart_game, 150)

# Start game
restart_game()
frame.start()

