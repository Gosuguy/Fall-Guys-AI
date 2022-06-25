<a href="https://youtu.be/Li2C7f61rZs" target="_blank"><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/26d947fb-61f5-4f5a-953f-64f52fb24301/de9f44g-c9659a69-a49b-426b-8bd1-7d2380a6ee51.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI2ZDk0N2ZiLTYxZjUtNGY1YS05NTNmLTY0ZjUyZmIyNDMwMVwvZGU5ZjQ0Zy1jOTY1OWE2OS1hNDliLTQyNmItOGJkMS03ZDIzODBhNmVlNTEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.SjkL3nDFd_Q7VgxI-Ynw19ZZ_tNqxvOhL2U-B0slFOM" title="Clarity Coders YouTube" /></a>
# Python / FastAI CNN - Playing Fall Guys
> This code was used to gather and process data while playing the game Fall Guys.
> The network was then trained using the FastAI Libary. 

## Setup
- I used dual monitors with a game playing at a 1280 x 720 resolution on one screen.
- You can start data collection by running CreateData.py
- Pressing B will start the screen / key grab. These will be stored in lists until the episode is done.
- Once the episode ( Round ) ends pressing h will stop the screen / key grab process and all data will be moved to a numpy array.
- Then I used a script in util folder called CreateImages.py to put then onto a disk drive in folders corresponding to their actions.

## Train
- Use the file called training.py
- Point it at your image directory

## Run Agents
- Trained Agent is TrainedAgent.py
- You will have to load in the pkl created from training.

## Inputs (Observations)
- Uses inputs to the neural network (Observations) of pixes in the game.
- 224 X 224
- Line detection

## Contact!
- Updated code YouTube <a href="https://www.youtube.com/gosugarage" 
- Original code YouTube <a href="https://www.youtube.com/claritycoders" target="_blank">Clarity Coders</a>
