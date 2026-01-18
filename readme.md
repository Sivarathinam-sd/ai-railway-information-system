# AI Railway Information System
<p align="center">
  <img width="100%" height="1024" alt="AI Railway System" src="https://github.com/user-attachments/assets/8e5a0dda-decc-4976-98f0-9b6d69d357bc" />
</p>
The AI Railway Information System leverages an intelligent conversational interface, allowing users to query the following:

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
