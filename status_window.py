import customtkinter as ctk
from get_status_string import get_random_status_string

def open_status_window(participant, current_health, initial_values, status_strings_list):
    # Create a new window for status
    status_window = ctk.CTkToplevel()
    status_window.title(f"Status for {participant}")
    status_window.attributes('-topmost', True)

    # Calculate health percentage
    current_hitpoints = current_health.get(participant)
    max_hitpoints = initial_values[participant][1]
    health_percentage = (current_hitpoints / max_hitpoints) * 100 if max_hitpoints > 0 else 0

    # Get health status string and color
    health_status, color = get_random_status_string(health_percentage, type=initial_values[participant][2], status_dict=status_strings_list)

    # Create label to display health status
    status_label = ctk.CTkLabel(status_window, text=health_status, fg_color=color)
    status_label.pack(padx=20, pady=20)

    # Add a close button
    close_button = ctk.CTkButton(status_window, text="Close", command=status_window.destroy)
    close_button.pack(pady=10)