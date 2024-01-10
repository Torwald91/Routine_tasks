#!/usr/bin/python3

import os
import sys
import subprocess
import time

def main():
    """
    Головна функція, яка виводить меню та виконує відповідні дії на основі введення користувача.
    """
    os.system('clear')

    try:
        while True:
            print('**********Меню**********')
            print('\n1.\tОновити систему')
            print('2.\tОчистити систему')
            print('3.\tОчистити логи')
            print('0.\tВихід\n')

            ans = input('Введіть число (0-3): ')

            if ans == '0':
                os.system('clear')
                print('\nДо побачення!\n')
                sys.exit()
            elif ans in ['1', '2', '3']:
                os.system('clear')
                print(f'\nВиконується опція {ans}...')

                # Замість використання subprocess.run, просто викликаємо функції напряму
                if ans == '1':
                    update_system()
                elif ans == '2':
                    clean_system()
                elif ans == '3':
                    clear_logs()

                print('')
                time.sleep(2)
                os.system('clear')
                input('Натисніть Enter, щоб продовжити...')
                os.system('clear')
            else:
                print('')
                print('\nНедійсна опція. Будь ласка, введіть число від 0 до 3.\n')
                input('Натисніть Enter, щоб продовжити...')
                os.system('clear')

    except Exception as e:
        print(f'\nПомилка: {e}\n')
        input('Натисніть Enter, щоб продовжити...')


def update_system():
    """
    Функція для оновлення системи та опційного оновлення пакунків.
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
    upgr = input('\nОновити систему т/н? ')
    
    if upgr == 'т':
        
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
        
        print ('\nДобре\n')
        time.sleep(2)


def clean_system():
    """
    Функція для очищення системи, видалення зайвих пакунків та інших завдань очищення.
    """
    os.system('clear')
    username = os.getenv('USER')
    script_path = f'sudo /home/{username}/routine_tasks/Clean_script'
    os.system(script_path)
    print('')
    os.system('apt clean')

    os.system('clear')
    snap_clear_choice = input('Очистити версії snap? (т/н): ').lower()

    if snap_clear_choice == 'т':
        script_snp_path = f'sudo /home/{username}/routine_tasks/snap_clean'
        os.system(script_snp_path)
        print('\nЗавершено\n')
        print('')
    else:
        print ('\nДобре\n')

    flatpak_clear_choice = input('Очистити невикористані залежності від flatpak? (т/н): ').lower()

    if flatpak_clear_choice == 'т':
        os.system('sudo flatpak uninstall --unused')
        print('\nЗавершено\n')


def clear_logs():
    """
    Функція для очищення простору в журналах на основі визначених користувачем часових одиниць.
    """
    os.system('clear')
    print('Доступний простір:\n')
    os.system('journalctl --disk-usage')

    lgpros = input('\nОчистити простір в журналах? (т/н): ')

    if lgpros.lower() == 'т':
        print('\n*****Оберіть опцію*****')
        print('\n1. \tОчистити за останні секунди')
        print('2. \tОчистити за останні хвилини')
        print('3. \tОчистити за останні години')
        print('4. \tОчистити за останні дні\n')

        time_cl = int(input('Введіть число -> '))
        
        if 1 <= time_cl <= 4:
            time_units = ['seconds', 'minutes', 'hours', 'days']
            time_value = input(f'\nВведіть кількість {time_units[time_cl-1]} -> ')
            os.system(f'sudo journalctl --vacuum-time={time_value}{time_units[time_cl-1][0]}')
            print ('Доступний простір:\n')
            os.system('journalctl --disk-usage\n')
            time.sleep(2)
        else:
            print ('\nНедійсна опція\n')
            time.sleep(2)
    else:
        print ('\nДобре\n')
        time.sleep(2)


if __name__ == '__main__':
    main()
