# Python OOP Minesweeper

## Project Overview
This project is a fully functional, classic Minesweeper game built using Python and the Tkinter library. It was developed to demonstrate core Object-Oriented Programming (OOP) concepts, including class design, object interaction, and encapsulation.

## Features & Custom Modifications
In addition to the base game logic from the tutorial, this project includes several custom modifications to improve the user experience:

Interactive Grid: Left-click to reveal a cell, and right-click to place a flag on suspected mines.

Cascading Reveals: Clicking a cell with zero adjacent mines automatically reveals all surrounding safe cells.

Custom Feature - Live Timer: A real-time clock tracks how many minutes and seconds the player takes to complete the board.

Custom Feature - Restart Button: A dedicated GUI button allows players to clear the board, reset the timer, and start a new game without closing the application window.

Custom Feature - Flag Counter: A dynamic label tracks how many mines are left to be flagged.

Win/Loss Detection: The game disables all buttons and triggers a pop-up message box when the player clicks a mine or successfully clears all safe cells.

## Technical Specifications

Language: Python 3

GUI Framework: Tkinter

Grid Size: 6x6 square grid (easily adjustable in the settings).

Difficulty: Set to "Easy Mode," where mines take up 20% of the total cells.

Window Dimensions: 1440 x 720 pixels.

Responsive Layout: Frames and elements are placed using calculated percentage utilities to keep the UI organized.

## OOP Concepts Demonstrated

Classes & Objects: The Cell class is the blueprint for every grid square, managing its own state (e.g., is_mine, is_opened).

Class Attributes: Global game variables, like the list of all cells (Cell.all) and the timer state (Cell.timer_running), are managed at the class level.

Static Methods: Utility functions like randomize_mines() and restart_game() are implemented as static methods since they affect the game globally.

Properties: The @property decorator is used for dynamically calculating a cell's surrounding neighbors and nearby mine count.

## How to Run

Clone the repository.

Ensure you have Python installed on your machine.

Open your terminal in the project directory.

Run the command: python main.py