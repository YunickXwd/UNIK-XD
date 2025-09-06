import os
import sys
import platform
import subprocess
import time

# Function to display animated loading
def animated_loading(text, duration=2):
    animation = "|/-\\"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{text} {animation[i % len(animation)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * (len(text) + 2) + "\r")
    sys.stdout.flush()

# Check if device is 64-bit
def check_architecture():
    machine = platform.machine()
    if 'aarch64' in machine or 'arm64' in machine or 'x86_64' in machine:
        return True
    return False

# Git pull function to update the tool
def git_pull_update():
    print("\033[1;33m Checking for updates...\033[0m")
    animated_loading("Connecting to GitHub")
    try:
        result = subprocess.run(['git', 'pull'], 
                              capture_output=True, text=True, timeout=30)
        if "Already up to date" in result.stdout:
            print("\033[1;32m ✓ Tool is already up to date!\033[0m")
        elif result.returncode == 0:
            print("\033[1;32m ✓ Update successful! Changes applied.\033[0m")
            return True
        else:
            print("\033[1;33m ⚠ Could not check for updates. Continuing...\033[0m")
    except Exception as e:
        print(f"\033[1;33m ⚠ Update check failed. Continuing...\033[0m")
    return False

# Clear screen function
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Print banner
def print_banner():
    banner = """
\033[1;35m
╔══════════════════════════════════════════════════╗
║                UNIK XD TOOL                      ║
║                Author: UNIK-XD                   ║
║                Facebook: YunickXwd               ║
╚══════════════════════════════════════════════════╝
\033[0m
"""
    print(banner)

# Main function
def main():
    clear_screen()
    print_banner()
    
    # Check architecture
    print("\033[1;36m Checking device architecture...\033[0m")
    animated_loading("Analyzing system")
    
    if not check_architecture():
        print("\033[1;31m ❌ Sorry, this tool only works on 64-bit devices!\033[0m")
        print("\033[1;33m Your device architecture:", platform.machine(), "\033[0m")
        sys.exit(1)
    
    print("\033[1;32m ✓ 64-bit architecture detected\033[0m")
    
    # Check for updates
    git_pull_update()
    time.sleep(1)
    
    # Load the Cython module
    print("\033[1;36m Loading UNIK engine...\033[0m")
    animated_loading("Initializing modules")
    
    try:
        # Import the Cython compiled module
        import unikv1
        print("\033[1;32m ✓ UNIK engine loaded successfully!\033[0m")
        
        # Run the main function from the Cython module
        print("\033[1;36m Starting UNIK tool...\033[0m")
        time.sleep(1)
        unikv1.main()
        
    except ImportError as e:
        print(f"\033[1;31m ❌ Failed to load UNIK engine: {e}\033[0m")
        print("\033[1;33m Make sure 'unikv1.cpython-312.so' is in the same directory\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\033[1;31m ❌ Error running UNIK tool: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()