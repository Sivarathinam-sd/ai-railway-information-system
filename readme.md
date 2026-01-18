# AI Railway Information System
The AI Railway Information System leverages an intelligent conversational interface, allowing users to query the following:

<p align="center">
  <img width="100%" height="1024" alt="AI Railway System" src="https://github.com/user-attachments/assets/8e5a0dda-decc-4976-98f0-9b6d69d357bc" />
</p>

* **Trains running from a source (Point A) to a destination (Point B)**  
  Example: `What are the trains running from 'LOKMANYATILAK T - LTT' to 'BHOPAL JN - BPL'?`

* **Whether a train runs on a specific day or get its running days**  
  Example: `Does train number '01123' run on Friday? Can you list its running days?`

* **The list of stops for a given train**  
  Example: `What is the arrival schedule of train '01123' at 'THANE - TNA'?`

* **The schedule timings of a train, optionally at a specific stop**  
  Example: `Can you list all the stops of train '01123'?`

The agent always responds courteously and accurately, in **no more than one sentence**, and is designed **not to hallucinate**.  

All information is retrieved from the official dataset: [Indian Express Dataset](https://www.kaggle.com/datasets/rohan26x/indian-express-train-dataset)

## Installation

1. Clone the repository:<br>
`git clone https://github.com/Sivarathinam-sd/Ai-Railway-Information-System.git`<br>
`cd ai-railway-information-system`

2. Create a virtual environment and activate it:<br>
`python -m venv venv`<br>
`source venv/bin/activate   # On Windows: venv\Scripts\activate`

3. Install dependencies: <br>
`pip install -r requirements.txt`

## Usage
1. Run the main interface: 
`python main.py` <br>
2. Open the URL shown in the terminal and start querying the system.

