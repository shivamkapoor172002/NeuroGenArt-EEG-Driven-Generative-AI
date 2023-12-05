# NeuroGenArt-EEG-Driven-Generative-AI (Code will be updated soon) - I'm working on it and will update soon as I continue my research.
This project is a Python application that generates images based on EEG (Electroencephalogram) data and user input. The generated images are created using a pre-trained model from the `diffusers` library, specifically the `AutoPipelineForText2Image` class. The EEG data is processed to extract frequency information, and a custom prompt for image generation is generated based on the user's input percentages for different brain wave frequencies.

## Sample Images

![image](https://github.com/shivamkapoor172002/NeuroGenArt-EEG-Driven-Generative-AI/assets/92868323/3296e37c-52d4-4890-aad3-71cd3dcc6f0b)
![image](https://github.com/shivamkapoor172002/NeuroGenArt-EEG-Driven-Generative-AI/assets/92868323/f930c9fe-fae8-4db3-9deb-bf52b61d60c7)

## Requirements

- Python 3.x
- `torch`, `numpy`, `pandas`, `matplotlib`, `scipy`, `PIL`, and `diffusers` libraries.

## Installation

1. Clone the repository:

   ```bash
   git clone [ https://github.com/your-username/brain-wave-image-generator.git](https://github.com/shivamkapoor172002/NeuroGenArt-EEG-Driven-Generative-AI)
   cd ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the `genrate.py` script:

   ```bash
   python genrate.py
   ```

2. Enter the initial prompt and the path to your EEG data CSV file in the Tkinter window.

3. Click the "Generate Image" button to generate and display an image based on the provided input.

## File Structure
![image](https://github.com/shivamkapoor172002/NeuroGenArt-EEG-Driven-Generative-AI/assets/92868323/bddc9b24-f1d5-4d0f-ae62-968bedb11c0c)

- `genrate.py`: Python script for generating images based on EEG data and user input.
- `plottin.py`: Python script for processing EEG data and computing frequency percentages.
- `requirements.txt`: List of Python dependencies.

## Sample EEG Data

The sample EEG data should be in CSV format with columns `timestamp` and `ch1`. Here's an example:

```csv
timestamp,ch1
1695905995.254,14377.446696453893
1695905995.258,14362.873359069034
1695905995.2619998,14357.55364388867
1695905995.266,14356.525463643726
1695905995.27,14353.55268163117
...
```



Feel free to explore and customize the code according to your needs. If you encounter any issues or have suggestions, please open an issue on this repository.

---
