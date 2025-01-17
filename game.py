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
starlings = 0  # Player's starlings (score)

# Inventory (including wood and water)
inventory = {"wood": 0, "water": 0}  # Player's inventory
max_inventory = 80  # Max inventory capacity

# Game state
game_over = False
win = False
player_velocity = [0, 0]  # Velocity for smooth movement
instructions_visible = False  # Track if instructions page is visible

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
    """Checks if the player collects trash, wood, or water."""
    global starlings, resources, inventory
    for trash in trash_positions[:]:
        if (abs(player_pos[0] - trash[0]) < (player_size + trash_size) / 2 and
            abs(player_pos[1] - trash[1]) < (player_size + trash_size) / 2):
            trash_positions.remove(trash)
            starlings += 5
            resources += 5  # Reward resources for collecting trash
            log_event("Collected trash! Gained 5 starlings and 5 resources.")
            spawn_trash()  # Replace the collected trash with a new one

            # Collect wood and water if inventory is not full
            if inventory["wood"] + inventory["water"] < max_inventory:
                wood_or_water = random.choice(["wood", "water"])
                if inventory[wood_or_water] < max_inventory // 2:
                    inventory[wood_or_water] += 1
                    log_event(f"Collected {wood_or_water}!")

def allocate_resources(region):
    global resources
    if not game_over:
        if resources >= 10:
            equality_scores[region] += random.randint(5, 15)
            resources -= 10
            log_event(f"Allocated 10 resources to {region}. Equality increased!")
        else:
            log_event("Not enough resources to allocate!")

def random_event():
    global resources
    if not game_over:
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
    """Checks if the player has won or lost the game."""
    global game_over, win
    if all(score >= 80 for score in equality_scores.values()):
        game_over = True
        win = True
    elif any(score <= 0 for score in equality_scores.values()):
        game_over = True
        win = False

def restart_game():
    global equality_scores, resources, log, starlings, trash_positions, game_over, win, inventory, instructions_visible
    equality_scores = {region: 50 for region in regions}
    resources = 100
    log = []
    starlings = 0
    trash_positions = []
    inventory = {"wood": 0, "water": 0}  # Reset inventory
    game_over = False
    win = False
    instructions_visible = False  # Ensure instructions are hidden when restarting
    for _ in range(5):  # Spawn initial trash
        spawn_trash()
    log_event("Game restarted! Let's bring harmony again.")

def check_edges():
    """Subtracts starlings if the player touches the screen edges."""
    global starlings
    if player_pos[0] <= 0 or player_pos[0] >= 800 or player_pos[1] <= 0 or player_pos[1] >= 400:
        starlings = max(0, starlings - 2)
        log_event("Touched the edge! Lost 2 starlings.")

# Event handlers for player movement
def keydown(key):
    """Handles key press for player movement."""
    if not game_over:
        if key == simplegui.KEY_MAP['left']:
            player_velocity[0] = -5
        elif key == simplegui.KEY_MAP['right']:
            player_velocity[0] = 5
        elif key == simplegui.KEY_MAP['up']:
            player_velocity[1] = -5
        elif key == simplegui.KEY_MAP['down']:
            player_velocity[1] = 5

def keyup(key):
    """Stops movement when the key is released."""
    if not game_over:
        if key in (simplegui.KEY_MAP['left'], simplegui.KEY_MAP['right']):
            player_velocity[0] = 0
        elif key in (simplegui.KEY_MAP['up'], simplegui.KEY_MAP['down']):
            player_velocity[1] = 0

# Background drawing function
def draw_background(canvas):
    # Soft gradient background (top to bottom)
    canvas.draw_polygon([(0, 0), (800, 0), (800, 200), (0, 200)], 1, "Black", "#5f6a6a")
    canvas.draw_polygon([(0, 200), (800, 200), (800, 400), (0, 400)], 1, "Black", "#3b4c48")

    # Geometric shapes for a professional, abstract look
    canvas.draw_polygon([(50, 100), (150, 50), (250, 100), (150, 150)], 1, "White", "#2b5a6f")
    canvas.draw_polygon([(600, 50), (750, 100), (750, 200), (600, 150)], 1, "White", "#387493")
    canvas.draw_polygon([(300, 250), (400, 300), (500, 250), (400, 200)], 1, "White", "#456c6f")
    canvas.draw_line((0, 100), (800, 100), 2, "white")
    canvas.draw_line((0, 300), (800, 300), 2, "white")

# Draw the game screen with background and content
def draw(canvas):
    global resources, instructions_visible

    draw_background(canvas)  # Call background drawing function

    if instructions_visible:
        # Draw instructions page
        canvas.draw_text("Instructions:", (50, 50), 24, "White")
        canvas.draw_text("1. Collect trash to earn resources and starlings.", (50, 100), 20, "White")
        canvas.draw_text("2. Allocate resources to different regions.", (50, 150), 20, "White")
        canvas.draw_text("3. Manage your resources wisely!", (50, 200), 20, "White")
        canvas.draw_text("4. Collect wood and water to keep them in your inventory", (50, 250), 20, "White")
        canvas.draw_text("5. Victory after collecting 30 starlings!", (50, 300), 20, "White")
        canvas.draw_text("Press Restart Game to play the game!", (50, 350), 20, "White")
    else:
        if game_over:
            canvas.draw_polygon([(0, 0), (800, 0), (800, 400), (0, 400)], 1, "Black", "Black")
            if win:
                canvas.draw_text("Congratulations! You won!", (200, 200), 36, "Green")
            else:
                canvas.draw_text("You lost! Try again.", (250, 200), 36, "Red")
        else:
            # Draw title and resources
            canvas.draw_text("Peaceformers: The Quest for Equality", (50, 30), 24, "White")
            canvas.draw_text(f"Resources: {resources}", (50, 60), 20, "Yellow")
            canvas.draw_text(f"Starlings: {starlings}", (650, 30), 20, "Yellow")

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

            # Draw inventory
            canvas.draw_text(f"Wood: {inventory['wood']}", (650, 60), 20, "White")
            canvas.draw_text(f"Water: {inventory['water']}", (650, 90), 20, "White")

            # Check collision, edges, and win/lose conditions
            check_collision()
            check_edges()
            check_win()

            # Update player position
            player_pos[0] += player_velocity[0]
            player_pos[1] += player_velocity[1]

# Inventory toggle
def toggle_inventory():
    if inventory["wood"] > 0 or inventory["water"] > 0:
        log_event(f"Inventory - Wood: {inventory['wood']}, Water: {inventory['water']}")
    else:
        log_event("Inventory is empty.")

# Function to show instructions
def show_instructions():
    global instructions_visible
    instructions_visible = True
    frame.set_draw_handler(draw)  # Redraw with instructions page visible

# Function to hide instructions
def hide_instructions():
    global instructions_visible
    instructions_visible = False
    frame.set_draw_handler(draw)  # Redraw with game content

# Create main game frame
frame = simplegui.create_frame("Peaceformers", 800, 400)

# Register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Allocate to Region A", lambda: allocate_resources("Region A"), 150)
frame.add_button("Allocate to Region B", lambda: allocate_resources("Region B"), 150)
frame.add_button("Allocate to Region C", lambda: allocate_resources("Region C"), 150)
frame.add_button("Allocate to Region D", lambda: allocate_resources("Region D"), 150)
frame.add_button("Allocate to Region E", lambda: allocate_resources("Region E"), 150)
frame.add_button("Trigger Random Event", random_event, 150)
frame.add_button("Restart Game", restart_game, 150)
frame.add_button("Toggle Inventory", toggle_inventory, 150)
frame.add_button("Instructions", show_instructions, 150)
frame.add_button("Hide Instructions", hide_instructions, 150)

# Start the game with initial trash items
for _ in range(5):
    spawn_trash()

# Start the frame
frame.start()
