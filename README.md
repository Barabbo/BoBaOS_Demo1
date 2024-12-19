
# BoBaOS_Demo1... FINALLY!
This Python code show a rotating shaded cube in the terminal. It defines the cube's vertices, edges, and faces, using functions to rotate, project, and draw the vertices on a 2D plane, calculating shading based on light intensity. The main loop rotates the cube, updates the screen every 0.05 seconds. 


# Rotating Shaded Cube

This Python project took me very mount of time to figure how to do this:
displays a rotating shaded cube in the terminal. 


che code took me an infinity.

It defines the vertices, edges, and faces of the cube and uses functions to rotate,
project, and draw the vertices on a 2D plane. The shading is calculated based on light intensity, creating a realistic visual effect.

## Features

- Rotating 3D cube in realtime
- "Raytarcing" shadow effect (buggy)
- Real-time in your terminal
- Adjustable rotation angles
- Loading text animation

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contribution](#contribution)
- [License](#license)
- [Dual Licensing](#dual-licensing)
- [Contact](#contact)

## Installation

To run this project, you need to have Python installed on your machine. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Barabbo/BoBaOS_Demo1.git

-------
Navigate to the project directory:

bash

cd rotating-shaded-cube


(Optional) Create and activate a virtual environment:

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash

pip install -r requirements.txt
Usage
To run the cube animation, execute the following command:

bash

python main.py
You should see a rotating cube with shading effects and a loading text animation in your terminal.

Code Explanation
Vertices, Edges, and Faces
Vertices: The corners of the cube.
Edges: The lines connecting the vertices.
Faces: The surfaces of the cube.

Main Functions:

rotate_vertices(vertices, angle_x, angle_y, angle_z): Rotates the vertices around the x, y, and z axes.
project_vertices(vertices, width, height, scale, distance): Projects the 3D vertices onto a 2D plane.
calculate_normal(face, vertices): Calculates the normal vector of a face.
calculate_light_intensity(normal, light): Calculates the light intensity on a face.
draw_cube(vertices, edges, faces, width, height, light): Draws the cube in the terminal with shading.
this took me alot to figure how shadows and light can affect a surface.

display_screen(screen): Displays the screen buffer in the terminal.
Main Loop
The main loop continuously rotates the cube, projects the vertices, draws the cube, and displays the loading text. The screen is updated every 0.05 seconds, faster than your eye perceptions.

Contribution
Contributions are welcome! If you want to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Dual Licensing
This software is available under a dual licensing model:

Open-source License: MIT License
Commercial License: For commercial use, please contact me here, on github.

Boba Boba!

Nick
