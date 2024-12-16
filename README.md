# Automatic Oatmeal Maker

This project automates oatmeal preparation using a Raspberry Pi. It schedules and controls the preparation process based on predefined times for each weekday.

---

## Features
- **Automated Scheduling:** Prepare oatmeal on specific days and times.
- **Web Interface:** Modify and view schedules via a user-friendly web interface.
- **Hardware Integration:** Controls relays to dispense oatmeal and manage water dispensing.

---

## How It Works
1. **Schedule Configuration:** 
   - The `schedule.json` file defines the preparation times for each weekday.
   - The Flask web interface allows you to edit these schedules.

2. **Hardware Control:** 
   - Raspberry Pi GPIO pins control relays that manage the oatmeal dispensers and water dispensing machine.
   - Temperature sensors monitor the CPU temps as a fail safe to turn off the script.

3. **Flask Web App:**
   - Hosts a web interface for user interaction.

4. **Results**
   - Your bowl is prepared ready to eat with oatmeal and hot water
