# VettyClient
vetty_client_assessment


# File Reader Flask App

## Overview
This Flask application serves as a simple file reader. It allows users to read the contents of text files stored within the server by specifying the file name and optionally, the range of lines they wish to read.

## Features
- **File Reading**: Read the contents of a file by navigating to the root URL followed by the filename.
- **Line Range Selection**: Specify a range of lines to read from the file using `start` and `end` query parameters.

## Installation

To run this application, you'll need Python and Flask installed on your system.

1. Clone the repository:
https://github.com/GANESH0369/VettyClient.git

2. Create a virtual environment: Navigate to your project directory and run:
python3 -m venv venv

3. Activate the virtual environment(On Windows, run):
\venv\Scripts\activate


4. Navigate to the cloned directory:
cd [vetty_Assesment]

5. Install the required packages:
pip install -r requirements.txt

6. Start the server with the following command:
flask run

7. based on start and end endpoint: 
http://localhost:5000/file3.txt?start=1&end=30
