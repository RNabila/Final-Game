# Peacefomers: Collect Resources and Distribute!
In this strategy-based game, the player must collect as many resources and distribute them in order to raise equality levels of 5 different regions. They must collect trash, and keep track of how many wood and water they have in their inventory. Equality for all regions and prudent resource management are the keys to vicotry!

## Objective

The goal of the game is to collect starlings and resources while improving the equality levels of different regions. Players must allocate resources, collect trash, and manage their inventory to bring harmony to all regions. The game ends when:

**Win Condition:** All regions reach an equality/resources score of 80 or more.

**Lose Condition:** Any region's equality/resources score drops to 0.(It is hard to lose, it would have to be a random event.)

## Features of the Game

- **Regions:** Region A, Region B, Region C, Region D, and Region E are the five regions in the game. The initial equality score for each region is 50. Distributing resources is necessary to raise their equality ratings.
  
- **Resources:** The player has one hundred resources at the beginning. Trash collection might boost the amount of resources that are allocated to different locations.
  
- **Trash:** Items in the trash show up on the screen at random. They provide resources and starlings (scoring) to the player when they are gathered.
  
- **Starlings:** Starlings are used to track the player's score. The player receives starlings for gathering rubbish. To win, the player requires thirty starlings.
  
- **Inventory:** Water and wood, which are kept in the inventory, are available for the player to gather. Eighty is the maximum inventory capacity.
  
- **Random Events:** Random events can affect regions positively or negatively, influencing equality scores.

### Key Features

- **Trash Collection:** Collect trash items on the screen to gain starlings and resources.
  
- **Resource Distribution/Allocation:** Use resources to increase equality in regions. The player can choose which region to allocate resources to by clicking the respective buttons.
  
- **Inventory Management:** Collect wood and water to manage resources in your inventory.
  
- **Random Events:** Random events affect the equality levels of regions, either giving a bonus or a penalty, and sometimes providing additional resources.
  
- **Game Over Conditions:** The game ends when either the player wins or loses. The game can be restarted at any time.

### GUI Functionality

#### Display

For a contemporary, abstract atmosphere, the game uses geometric shapes over a smooth gradient background. Important details are displayed on the screen:

- **Title:** "Peaceformers: The Quest for Equality"  
- **Resources:** Displays the pool of available resources on the side of the screen  
- **Starlings:** Shows the score as of right now on the top of the screen.  
- **Region Equality Scores:** Provides each region's current equality score on the left side of the screen.  
- **Player:** A circle represents the player's character on the screen that can be moved around using up/down/left/right keys.  
- **Trash:** Items in the trash are shown as circles strewn all over the screen.  
- **Log:** Shows the previous five game events.  
- **Inventory:** Displays how much water and wood the player currently has.

### Controls

- **Keyboard:** Use the arrow keys (left, right, up, down) to move the player character on the screen.
  
- **Buttons:**
  - **Allocate to Region A, B, C, D, E:** Allocate 10 resources to the selected region.
  - **Trigger Random Event:** Random events will impact the game (e.g., bonus or penalty to a region’s equality score).
  - **Restart Game:** Resets the game to its initial state.
  - **Toggle Inventory:** Displays the player's inventory (wood and water).
  - **Instructions:** Shows the game instructions.
  - **Hide Instructions:** Hides the game instructions.

### Random Events

Random events can be triggered at intervals during gameplay:

- **Bonus:** A region gains additional equality points.  
- **Penalty:** A region loses equality points.  
- **Resource Gain:** The player gains extra resources.

### Code Structure

#### Global Variables

- **regions:** A list of the game's regions.
- **equality_scores:** A dictionary that holds each region's equality score.
- **resources:** The player's resources are tracked by a global variable.
- **log:** A list used for recording game happenings.
- **player_pos, player_size:** The player character's location and dimensions.
- **trash_positions:** The locations of the trash items on the screen are listed.
- **inventory:** A dictionary that holds the player's water and wood supplies.
- **game_over, win:** Boolean indicators that indicate whether the game is won or over.
- **player_velocity:** The player character's speed for fluid motion.
- **instructions_visible:** A Boolean flag that indicates whether the game's instructions are visible or not.

#### Helper Functions

- **log_event(event):** Adds an event to the game log.  
- **spawn_trash():** Spawns a trash item at a random position on the screen.  
- **check_collision():** Checks if the player collects any trash and updates the player's resources and starlings.  
- **allocate_resources(region):** Allocates 10 resources to a selected region and increases its equality score.  
- **random_event():** Generates random events (bonus, penalty, or resource gain).  
- **check_win():** Checks whether the player has won or lost the game.  
- **restart_game():** Restarts the game to its initial state.

#### Key Handlers

- **keydown(key):** Handles key presses for player movement (up, down, left, right).  
- **keyup(key):** Stops the player from moving when the key is released.

#### Drawing Functions

- **draw_background(canvas):** Draws the background with soft gradients and geometric shapes for a modern and sophisticated look.  
- **draw(canvas):** The main function that draws the game elements, including the background, player, trash, resources, inventory, and event log.

#### Instructions and Inventory

- **toggle_inventory():** Toggles the visibility of the player's inventory.  
- **show_instructions():** Displays the game instructions.  
- **hide_instructions():** Hides the game instructions.
