import pyautogui
import pyperclip
import time

# Step 1: Click on the crome icon at (1402, 1053)
pyautogui.click(1402, 1053)

# Pause to ensure the action is registered
time.sleep(1)

# Step 2: Drag from (679, 219) to (1876, 899) to select text
pyautogui.moveTo(679, 219)
pyautogui.dragTo(1876, 899, duration=1)

# Pause to ensure the text is selected
time.sleep(0.5)

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Pause to ensure the text is copied
time.sleep(0.5)

# Step 4: Store the copied text in a variable
copied_text = pyperclip.paste()

# Print the copied text to verify
print(copied_text)

