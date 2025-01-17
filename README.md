# Final-Game

Certainly! Here's a thorough README for your game:

---

# Peaceformers: The Quest for Equality

## Overview
**Peaceformers: The Quest for Equality** is a strategy-based simulation game where the player must balance resources to improve the equality levels of different regions. The player must collect trash, allocate resources, and manage an inventory of wood and water, all while ensuring their starlings score increases. Victory is achieved by bringing equality to all regions while managing resources wisely. The game provides an interactive GUI to track progress and events, and is controlled using keyboard and in-game buttons.

## Gameplay

### Objective
The goal of the game is to collect starlings and resources while improving the equality levels of different regions. Players must allocate resources, collect trash, and manage their inventory to bring harmony to all regions. The game ends when:
- **Win Condition**: All regions reach an equality score of 80 or more.
- **Lose Condition**: Any region's equality score drops to 0.

### Game Elements
- **Regions**: There are 5 regions in the game (Region A, Region B, Region C, Region D, and Region E). Each region starts with an equality score of 50. You must allocate resources to increase their equality scores.
- **Resources**: The player starts with 100 resources. Resources are used to allocate to regions and can be increased by collecting trash.
- **Trash**: Trash items appear randomly on the screen. When collected, they give the player starlings (score) and resources.
- **Starlings**: The player's score is tracked through starlings. Collecting trash gives the player starlings. The player needs 30 starlings to win.
- **Inventory**: The player can collect wood and water, which are stored in the inventory. The maximum inventory capacity is 80.
- **Random Events**: Random events can affect regions positively or negatively, influencing equality scores.

### Key Features
1. **Trash Collection**: Collect trash items on the screen to gain starlings and resources.
2. **Resource Allocation**: Use resources to increase equality in regions. The player can choose which region to allocate resources to by clicking the respective buttons.
3. **Inventory Management**: Collect wood and water to manage resources in your inventory.
4. **Random Events**: Random events affect the equality levels of regions, either giving a bonus or a penalty, and sometimes providing additional resources.
5. **Game Over Conditions**: The game ends when either the player wins or loses. The game can be restarted at any time.

## GUI Functionality

### Display
The game displays a soft gradient background with geometric shapes for a modern, abstract feel. Key information is shown on the screen:
- **Title**: Displays the game title "Peaceformers: The Quest for Equality".
- **Resources**: Shows the current resource pool.
- **Starlings**: Displays the current score.
- **Region Equality Scores**: Lists the current equality score for each region.
- **Player**: The player's character is shown as a circle on the screen.
- **Trash**: Trash items are represented as circles scattered around the screen.
- **Log**: Displays the last 5 game events in the log.
- **Inventory**: Shows the current amount of wood and water the player has collected.

### Controls
- **Keyboard**: Use the arrow keys (left, right, up, down) to move the player character on the screen.
- **Buttons**:
  - **Allocate to Region A, B, C, D, E**: Allocate 10 resources to the selected region.
  - **Trigger Random Event**: Random events will impact the game (e.g., bonus or penalty to a region’s equality score).
  - **Restart Game**: Resets the game to its initial state.
  - **Toggle Inventory**: Displays the player's inventory (wood and water).
  - **Instructions**: Shows the game instructions.
  - **Hide Instructions**: Hides the game instructions.

### Random Events
Random events can be triggered at intervals during gameplay:
- **Bonus**: A region gains additional equality points.
- **Penalty**: A region loses equality points.
- **Resource Gain**: The player gains extra resources.

## Code Structure

### Global Variables
- `regions`: A list of regions in the game.
- `equality_scores`: A dictionary storing the equality score for each region.
- `resources`: A global variable tracking the player's resources.
- `log`: A list storing game events for logging purposes.
- `player_pos`, `player_size`: The position and size of the player character.
- `trash_positions`: A list of trash item positions on the screen.
- `inventory`: A dictionary storing the player's inventory (wood and water).
- `game_over`, `win`: Boolean flags for checking if the game is over or won.
- `player_velocity`: The velocity of the player character for smooth movement.
- `instructions_visible`: Boolean flag for showing or hiding the game instructions.

### Helper Functions
- **log_event(event)**: Adds an event to the game log.
- **spawn_trash()**: Spawns a trash item at a random position on the screen.
- **check_collision()**: Checks if the player collects any trash and updates the player's resources and starlings.
- **allocate_resources(region)**: Allocates 10 resources to a selected region and increases its equality score.
- **random_event()**: Generates random events (bonus, penalty, or resource gain).
- **check_win()**: Checks whether the player has won or lost the game.
- **restart_game()**: Restarts the game to its initial state.

### Event Handlers
- **keydown(key)**: Handles key presses for player movement (up, down, left, right).
- **keyup(key)**: Stops the player from moving when the key is released.

### Drawing Functions
- **draw_background(canvas)**: Draws the background with soft gradients and geometric shapes for a modern look.
- **draw(canvas)**: The main function that draws the game elements, including the background, player, trash, resources, inventory, and event log.

### Instructions and Inventory
- **toggle_inventory()**: Toggles the visibility of the player's inventory.
- **show_instructions()**: Displays the game instructions.
- **hide_instructions()**: Hides the game instructions.

## Conclusion
This game combines resource management, random events, and strategic decision-making to create an engaging gameplay experience. Players must carefully manage their resources, collect trash to earn starlings, and allocate resources to improve the equality scores of various regions. With a visually appealing GUI and clear, interactive controls, **Peaceformers: The Quest for Equality** offers a fun and challenging gameplay experience.
