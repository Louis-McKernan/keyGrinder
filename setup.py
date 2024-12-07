#setup.py
import subprocess
import sys

# Function to check and install required modules
def ensure_installed(modules):
    """
    Checks if the specified modules are installed. If not, installs them automatically.
    :param modules: A list of module names (as strings) to check and install.
    """
    for module in modules:
        try:
            __import__(module)  # Check if the module can be imported
        except ImportError:
            print(f"Module '{module}' is not installed. Installing it now...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        else:
            print(f"Module '{module}' is already installed.")

# Main function to ensure required modules are installed
def main():
    required_modules = ["pyautogui", "keyboard"]  # List of modules to ensure
    ensure_installed(required_modules)
    print("All required modules are installed and ready to use!")

# Run the module installer if this script is executed
if __name__ == "__main__":
    main()
