from diffusers import AutoPipelineForText2Image
import torch
import random
import tkinter as tk
from tkinter import Button, Label, Entry
from PIL import Image, ImageTk
from plottin import compute_frequencies_percentage

# Load sdxl-turbooo
pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float32)


def generate_brain_wave_prompt(initial_prompt, delta_percent, theta_percent, alpha_percent, beta_percent, gamma_percent):
    """
    Generate a brain wave custom prompt string based on user input percentages.
    """
    # Define the adjective lists for each brain wave type
    delta_adjectives = ["Serene", "Sombre", "Ethereal", "Misty", "Gentle", "Luminous", "Dreamlike", "Subdued", "Monochromatic", "Fluid"]
    theta_adjectives = ["Ethereal", "Fluid", "Mystical", "Surreal", "Hazy", "Translucent", "Whimsical", "Melancholic", "Organic", "Soft-focus"]
    alpha_adjectives = ["Tranquil", "Harmonious", "Soft", "Fluid", "Luminous", "Pastel", "Ethereal", "Dreamy", "Meditative", "Subtle"]
    beta_adjectives = ["Vibrant", "Dynamic", "Sharp", "Intense", "Contrasted", "Bold", "Geometric", "Detailed", "Saturated", "Energetic"]
    gamma_adjectives = ["Intricate", "Vivid", "Radiant", "Dynamic", "Sharp", "Synchronized", "Intense", "Pulsating", "Luminous", "Kaleidoscopic"]

    def select_adjectives(adjective_list, percent):
        count = max(1, int(len(adjective_list) * (percent / 100)))
        return random.sample(adjective_list, count)

    # Select adjectives for each brain wave type based on the given percentages
    selected_delta = select_adjectives(delta_adjectives, delta_percent)
    selected_theta = select_adjectives(theta_adjectives, theta_percent)
    selected_alpha = select_adjectives(alpha_adjectives, alpha_percent)
    selected_beta = select_adjectives(beta_adjectives, beta_percent)
    selected_gamma = select_adjectives(gamma_adjectives, gamma_percent)

    # Build the prompt
    prompt = initial_prompt
    prompt += ", ".join(selected_delta)
    prompt += ", ".join(selected_theta)
    prompt += ", ".join(selected_alpha)
    prompt += ", ".join(selected_beta)
    prompt += ", ".join(selected_gamma)

    return prompt

def display_image(window, img_path, img_label_var):
    """
    Display the generated image on the Tkinter window.
    """
    img = Image.open(img_path)
    img_tk = ImageTk.PhotoImage(img)

    if img_label_var:
        img_label_var[0].configure(image=img_tk)
        img_label_var[0].image = img_tk
    else:
        img_label = Label(window, image=img_tk)
        img_label.image = img_tk
        img_label.pack()
        img_label_var.append(img_label)

def generate_image(initial_prompt, img_label_var, delta, theta, alpha, beta, gamma):
    """
    Generate an image based on the user's input and display it on the Tkinter window.
    """
    prompt = generate_brain_wave_prompt(initial_prompt, delta, theta, alpha, beta, gamma)
    image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
    img_path = "generated_image.png"
    image.save(img_path)
    display_image(window, img_path, img_label_var)

def on_generate_button_click():
    """
    Handle the button click event, read user input, and generate/display the image.
    """
    prompt = prompt_entry.get()
    path = data_entry.get()
    
    try:
        data_list = compute_frequencies_percentage(path)
        if len(data_list) != 5:
            raise ValueError("Invalid data format: Expected a list of five values.")
        
        delta, theta, alpha, beta, gamma = map(int, data_list)
        generate_image(prompt, img_label_var, delta, theta, alpha, beta, gamma)
    
    except Exception as e:
        print(f"Error: {e}")

# Create the Tkinter window
window = tk.Tk()
window.title("Brain Wave Image Generator")

# User input for initial prompt
prompt_label = tk.Label(window, text="Enter your initial prompt")
prompt_label.pack()
prompt_entry = Entry(window)
prompt_entry.pack()

# User input for EEG data path
data_label = tk.Label(window, text="Enter the path to your EEG csv data")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

# Image label variable for displaying the generated image
img_label_var = []

# Generate image button
generate_button = Button(window, text="Generate Image", command=on_generate_button_click)
generate_button.pack()

# Run the Tkinter application
window.mainloop()