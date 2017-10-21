# raspy-sampler

[![Youtube](https://img.youtube.com/vi/bWudBkCdCZA/0.jpg)](https://www.youtube.com/watch?v=bWudBkCdCZA "Youtube")

## Sampler / Sequencer

A very basic sampler / sequencer for the [Raspbperry Pi Piano HAT](https://shop.pimoroni.com/products/piano-hat). This python program reads key input from the Pimoroni Piano Hat on your raspberry pi.

- Piano keys play samples
- Octave keys switch between sound banks
- The instrument key switches recording-mode on or off (and erases the recording when switching off)

## Recording

When recording is ON, the keys you press are remembered for the position that the LED is currently indicating. The corresponding sound 
will be played back when the LED reaches that position again. You can play multiple sounds in the same slot.

### Todo

- Remember the sound bank for each recorded sound, not just the first
- When recording, a sound can unintentionally play twice (once for pressing it, and once for being in the recording)
