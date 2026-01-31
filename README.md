# FocusRead RSVP - Pro

A high-speed reading application using Rapid Serial Visual Presentation (RSVP) technique to help you read faster with better comprehension.

## What is RSVP?

Rapid Serial Visual Presentation (RSVP) is a method of displaying text one word at a time in a fixed location. This approach:

- **Eliminates eye movement** - Your eyes stay fixed in one place, reducing fatigue
- **Increases reading speed** - By removing the time spent scanning across lines
- **Improves focus** - Each word demands your full attention
- **Enhances comprehension** - With proper pacing, comprehension can actually improve

## Features

### Core Reading Experience

- **Vowel-Sync ORP (Optimal Recognition Point)**: Words are displayed with the optimal recognition point (usually the first vowel near the center) highlighted in red, with the prefix and suffix in gray. This helps your eyes focus on the most informative part of each word.

- **Dynamic Word Highlighting**: As you read, the current word is highlighted in the text input area, allowing you to track your position and pause if you lose focus.

- **Adjustable Speed**: Control reading speed from 100 to 1200 words per minute (WPM) with a simple slider.

### Intelligent Pacing

FocusRead automatically adjusts reading speed based on content:

- **End-sentence pauses** (. ! ?) - Automatically slows down at the end of sentences for better comprehension
- **Mid-sentence pauses** (, ; :) - Brief pauses for natural rhythm
- **Long word slowdown** - Longer words (>6 and >9 characters) are displayed slightly longer to ensure readability

### Advanced Settings

Expand the "Advanced Settings" menu to customize pacing behavior:

- **End Sentence Multiplier** (1.0-5.0x): Control how much to slow down at sentence endings (default: 2.5x)
- **Mid Sentence Multiplier** (1.0-3.0x): Adjust pause length for commas, semicolons, and colons (default: 1.5x)
- **Long Word Multiplier (>9 chars)** (1.0-3.0x): Set slowdown factor for very long words (default: 1.4x)
- **Medium Word Multiplier (>6 chars)** (1.0-2.0x): Set slowdown factor for moderately long words (default: 1.1x)

### Progress Tracking

- Visual progress bar shows how far you are through the text
- Percentage indicator updates in real-time

## How to Use

1. **Paste Text**: Copy any text into the text input area at the top
2. **Adjust Speed**: Use the WPM slider to set your desired reading speed
   - Start with 200-300 WPM if you're new to RSVP
   - Gradually increase as you get comfortable
3. **Start Reading**: Click the "START READING" button
4. **Follow Along**: Watch the word display and track progress in the text area
5. **Pause/Resume**: Click "PAUSE" to take a break, then "RESUME" to continue
6. **Reset**: Click "RESET" to clear all progress and start over

### Tips for Success

- **Start slow**: Begin at 200-250 WPM and gradually increase
- **Take breaks**: If you feel overwhelmed, pause and review the text
- **Adjust settings**: Use the Advanced Settings menu to find what works best for you
- **Practice regularly**: RSVP is a skill that improves with practice

## Building from Source

To compile the executable yourself:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "FocusRead" rsvp.py
```

The executable will be created in the `dist/` directory.

## Requirements

- Python 3.x
- tkinter (included with Python)
- PyInstaller (for building the executable)

## License

This project is open source and available for personal and commercial use.
