# Software-dev2-A1-RefDef


In sprint 1 this repo was proposed https://github.com/RayanT123-jpg/Platformer-game-.git

Platform Game

Introduction:
# Coin Adventure

## Project Overview

Coin Adventure is a 2D platform game developed using Python and Pygame.

The player controls a character that must collect coins, avoid enemies and reach the goal to complete the level.

The project was developed as part of the Software Development 2 module.

## Project Objectives
## Objectives

The objectives of the project are:

- Create a playable platform game.
- Implement player movement.
- Implement jumping and gravity.
- Implement enemy collision.
- Implement coin collection.
- Implement a win condition.
- Apply software development principles.

Scrum Style Stories.

Identify, priorities and explain user and system requirements supported with ‘scrum’
style stories (5%)

User Requirements ;

As a player, I want to move left and right so that I can explore the level. Priority - (High)

As a player, I want to jump so that I can reach platforms and avoid enemies. Priority - (High)

As a player, I want the character to fall when jumping so that the game feels realistic. Priority - (High)

As a player, I want enemies to damage me so that the game provides challenge. Priority - (High)

As a player, I want to collect coins so that I can increase my score. Priority - (Medium)

As a player, I want to reach the goal so that I can complete the level. Priority - (High)

As a player, I want the game to end when I hit an enemy so that failure is recognised. Priority - (Low)

As a player, I want a background image so that the game environment feels immersive. Priority - (Extremely High)

As a player, I want graphics and images so that the game looks interesting. Priority - (High)

As a player, I want simple keyboard controls so that the game is easy to play. Priority - (Low)

System Requirements ;

The system shall allow the player to jump when the spacebar is pressed.

The system shall allow the player to move left and right using keyboard input.

The system shall detect collisions between player and platform.

The system shall detect collision between player and enemy and trigger game over.

The system shall detect when the player collects a coin.

The system shall detect when the player reaches the goal.

The system should detect if the player reaches the end goal


## Game Story

The player controls a hero who must travel through a platform world collecting coins while avoiding enemies. The aim is to safely reach the goal at the end of the level.


Scrum Backlog 
b. Produce a ‘scrum’ style backlog supported with clear, evaluated definitions and tests
for the functions and features necessary to the completion of your project (10%)

Scrum Backlog ;

| ID   | Feature            | Priority | Description                                       | Test Case                            |
| ---- | ------------------ | -------- | ------------------------------------------------- | ------------------------------------ |
| PB1  | Player Movement    | High     | Player moves left and right using keyboard arrows | Press left/right keys → player moves |
| PB2  | Jump System        | High     | Player jumps using spacebar                       | Press space → player jumps           |
| PB3  | Gravity System     | High     | Player falls back down after jumping              | Player jumps → falls down            |
| PB4  | Platform Collision | High     | Player lands on platform without falling through  | Player lands on platform correctly   |
| PB5  | Enemy Movement     | Medium   | Enemy moves back and forth                        | Enemy moves automatically            |
| PB6  | Enemy Collision    | High     | Player loses if touching enemy                    | Touch enemy → Game Over              |
| PB7  | Coin Collection    | Medium   | Player collects coin and increases score          | Touch coin → score increases         |
| PB8  | Background Display | Low      | Background image loads in game                    | Background appears                   |
| PB9  | Goal System        | High     | Player wins when reaching goal                    | Touch goal → Win message             |
| PB10 | Game Window        | High     | Game screen loads correctly                       | Game window opens                    |
| PB11 | Score System       | Medium   | Score increases when coin collected               | Collect coin → score changes         |
| PB12 | Game Loop          | High     | Game continuously updates screen                  | Game runs smoothly                   |
| PB13 | Keyboard Controls  | High     | Game responds to key input                        | Keys move player                     |
| PB14 | Sprite Display     | Medium   | Player and enemy images load                      | Images appear correctly              |

## Characters

### Hero

- Controlled by the player
- Can move and jump
- Collects coins

### Enemy

- Moves automatically

## Environment

The game takes place in a side-scrolling platform world with a sky background, platforms, enemies and collectible coins.


- Causes game over if touched


Acceptance criteria.

## Gameplay

The player uses the keyboard to move through the level, collect coins and avoid enemies. The game ends when the player reaches the goal or collides with an enemy.

## Controls

| Key | Action |
|------|--------|
| Left Arrow | Move Left |
| Right Arrow | Move Right |
| Space | Jump |

## Development Strategy

The project followed an iterative development process.

Sprint 1:
- Research
- Planning
- Requirements
-  Enemy system
- Coin system
- Goal system

Sprint 2:
- Player movement
- Jumping
- Gravity
- - Testing
- Bug fixing
- Documentation

## Tools Used

- Python
- Pygame
- Visual Studio Code
- GitHub
- Windows 11

## Test Plan

| Test ID | Feature | Expected Result |
|----------|----------|----------|
| T1 | Movement | Player moves |
| T2 | Jump | Player jumps |
| T3 | Enemy Collision | Game Over |
| T4 | Coin Collection | Score increases |
| T5 | Goal | Victory |

