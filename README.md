Script Description:

This script is a simple command-line menu tool designed for beginners using Linux (Debian, Ubuntu) to perform common system maintenance tasks. 
It supports two languages: English and Ukrainian.

The script provides the following options:

    Update System:
        Updates the package lists.
        Displays upgradable packages.
        Optionally upgrades the system and snaps.

    Clean System:
        Executes a custom cleanup script (Clean_script) to remove unnecessary packages and perform system cleanup.
        Cleans apt cache.
        Optionally clears old revisions of snaps and removes unused dependencies from Flatpak.

    Clear Logs:
        Displays available disk space used by logs.
        Allows the user to choose a time unit (seconds, minutes, hours, days) for log cleanup.

    Exit:
        Exits the script.

How to Use:

    Run the script using Python 3: python3 Universal_UpClean.py or make it executable with chmod +x Universal_UpClean.py and then run ./Universal_UpClean.py.
    Follow the on-screen menu prompts to choose an option (1-3).
    For the "Update System" option, choose whether to upgrade the system and snaps.
    For the "Clean System" option, choose whether to clear snap revisions and remove unused dependencies from Flatpak.
    For the "Clear Logs" option, choose a time unit and enter the corresponding value.

For Beginners:

    This script is designed for users who are new to Linux, specifically Debian and Ubuntu distributions.
    It simplifies routine maintenance tasks, providing a menu-based interface.
    Users can easily perform updates, clean up the system, and manage log files without needing to remember complex commands.

Note: Ensure that you have the necessary permissions to execute system commands using sudo. If you encounter any issues, review the README.md or contact your system administrator for assistance.