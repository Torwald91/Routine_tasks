#!/usr/bin/python3

import os
import sys
import subprocess
import time

def main():
    """
    Main function that displays a menu and executes corresponding actions based on user input.
    """
    os.system('clear')

    try:
        while True:
            print('**********Menu**********')
            print('\n1.\tUpdate system')
            print('2.\tClean system')
            print('3.\tClear log')
            print('0.\tExit\n')

            ans = input('Enter the number (0-3): ')

            if ans == '0':
                os.system('clear')
                print('\nGoodbye!\n')
                sys.exit()
            elif ans in ['1', '2', '3']:
                os.system('clear')
                print(f'\nExecuting option {ans}...')

                # Instead of using subprocess.run, directly call the functions
                if ans == '1':
                    update_system()
                elif ans == '2':
                    clean_system()
                elif ans == '3':
                    clear_logs()

                print('')
                time.sleep(2)
                os.system('clear')
                input('Press Enter to continue...')
                os.system('clear')
            else:
                print('')
                print('\nInvalid option. Please enter a number between 0 and 3.\n')
                input('Press Enter to continue...')
                os.system('clear')

    except Exception as e:
        print(f'\nError: {e}\n')
        input('Press Enter to continue...')


def update_system():
    """
    Function to update the system and optionally upgrade packages.
    """
    os.system('clear')
    print('')
    os.system('sudo apt update')
    print('')
    os.system('apt list --upgradeable -a')
    print('')
    snpref = subprocess.check_output(['snap', 'refresh', '--list']).decode('utf-8')
    print(snpref)
    print('')
    upgr = input('\nUpgrade system y/n? ')
    
    if upgr == 'y':
        
        print('')
        os.system('clear')
        os.system('sudo apt full-upgrade -y')
        print('')
        if 'All snaps up to date' not in snpref:
            print('')
        else:
            os.system('sudo snap refresh')
            time.sleep(2)
            return True

        time.sleep(2)

    else:
        
        print ('\nOk\n')
        time.sleep(2)


def clean_system():
    """
    Function to clean the system, remove unnecessary packages, and perform other cleanup tasks.
    """
    os.system('clear')
    username = os.getenv('USER')
    script_path = f'sudo /home/{username}/routine_tasks/Clean_script'
    os.system(script_path)
    print('')
    os.system('apt clean')

    os.system('clear')
    snap_clear_choice = input('Clear snap revisions? (y/n): ').lower()

    if snap_clear_choice == 'y':
        script_snp_path = f'sudo /home/{username}/routine_tasks/snap_clean'
        os.system(script_snp_path)
        print('\nCompleted\n')
        print('')
    else:
        print ('\nOk\n')

    flatpak_clear_choice = input('Clear unused dependencies from flatpak? (y/n): ').lower()

    if flatpak_clear_choice == 'y':
        os.system('sudo flatpak uninstall --unused')
        print('\nCompleted\n')


def clear_logs():
    """
    Function to clear log space based on user-defined time units.
    """
    os.system('clear')
    print('Usable space:\n')
    os.system('journalctl --disk-usage')

    lgpros = input('\nClear space in log? (y/n): ')

    if lgpros.lower() == 'y':
        print('\n*****Choose an option*****')
        print('\n1. \tClean up in the last seconds')
        print('2. \tClean up in the last minutes')
        print('3. \tClean up in the last hours')
        print('4. \tClean up in the last days\n')

        time_cl = int(input('Enter the number -> '))
        
        if 1 <= time_cl <= 4:
            time_units = ['seconds', 'minutes', 'hours', 'days']
            time_value = input(f'\nEnter {time_units[time_cl-1]} -> ')
            os.system(f'sudo journalctl --vacuum-time={time_value}{time_units[time_cl-1][0]}')
            print ('Usable space:\n')
            os.system('journalctl --disk-usage\n')
            time.sleep(2)
        else:
            print ('\nInvalid option\n')
            time.sleep(2)
    else:
        print ('\nOk\n')
        time.sleep(2)


if __name__ == '__main__':
    main()

