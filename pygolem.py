# Core script of Golem

# 1- it check PyInstaller, if not installed, it install it

# 2- it check if a file named main is available in the directory, it will be the entry point

# 3- it loop all file to get all imported externals lbrairies

# 4- it add it to the final command line and execute it

# ----
# PyGolem class
# By Sanix-darker
# ----------------

from settings import *
from sys import exit
from os import path as os_path, walk as os_walk, system as ss, remove as os_remove, rmdir as os_rmdir
from subprocess import Popen, PIPE, STDOUT


class PyGolem:
    def __init__(self, path, stxt=None, INSERT=None, app_name="golem_app", debug_mode=True):
        self.app_name = app_name
        self.debug_mode = debug_mode
        self.path = path
        self.array_of_files = self.list_files()
        self.stxt = stxt
        self.INSERT = INSERT

    def print_log(self, *args):
        if self.debug_mode:
            print("[+] ", ' '.join(args))
            if self.stxt is not None:
                self.stxt.insert(self.INSERT, '\n[+] ' + ' '.join(args))

    def install_libs(self):
        # We install Golem requirements
        proc = Popen((MY_PIP + " install -r requirements.txt").split(" "), stdout=PIPE, stderr=STDOUT)
        output = proc.communicate()[0].decode('utf-8')
        self.print_log(output)

    def stop(self, reason):
        self.print_log(reason)
        exit()

    def clean_precedent_exe(self):
        try:
            os_remove(self.path + "/" + self.app_name + ".spec")
        except:
            pass
        try:
            os_rmdir(self.path + "/dist")
        except:
            pass
        try:
            os_rmdir(self.path + "/build")
        except:
            pass

    def list_files(self):
        to_return = []
        for subdir, dirs, files in os_walk(self.path):
            for file in files:
                to_return.append(os_path.join(subdir, file))
        return to_return

    def pyinstaller_checker(self):
        """
        This command just check if pyinstaller is installed or not
        :param self:
        :return:
        """
        self.print_log("Checking if pyinstaller is installed.")
        proc = Popen(COMMAND_TO_CHECK_PYINSTALLER_INSTALLED.split(" "), stdout=PIPE, stderr=STDOUT)
        output = proc.communicate()[0].decode('utf-8')
        if len(output) > 7:
            return False
        return True

    def print_check_file(self, file_name):
        """
        Just print the checking process
        :param self:
        :param file_name:
        :return:
        """
        self.print_log("Checking the file ", file_name, " in the ", self.path, "...")

    def check_main(self):
        """
        This method just check if the main file
        is present in the list of files
        :param array_of_files:
        :return:
        """
        self.print_check_file(MAIN_FILE_NAME)

        pathh = self.path + "/" + MAIN_FILE_NAME

        if pathh in self.array_of_files:
            if os_path.isfile(pathh):
                return True

        return False

    def check_requirements(self):
        """
        This method check if the requirements.txt is
        present in the list of files
        :param array_of_files:
        :return:
        """
        self.print_check_file(IMPORTS_FILE_NAME)

        pathh = self.path + "/" + IMPORTS_FILE_NAME

        if pathh in self.array_of_files:
            if os_path.isfile(pathh):
                with open(pathh, "r") as fl:
                    all_libs = fl.readlines()

                    return True, all_libs

        return False, 0

    def generate_app(self):
        # We perform some checkup
        if self.check_main():
            requirements_checks = self.check_requirements()
            print("requirements_checks: ", requirements_checks)
            if requirements_checks[0]:
                # Then we proceed
                all_libs = requirements_checks[1]

                # We install all available libs
                self.install_libs()

                if self.pyinstaller_checker():
                    # We perform some cleaning ...
                    self.clean_precedent_exe()

                    # We build the pyinstaller command
                    the_command = "cd " + self.path + " && " + "pyinstaller main.py "
                    for ll in all_libs:
                        the_command += " --hidden-import=" + ll.split("==")[0].replace("\n", "") + " "
                    the_command += " --onefile --name " + self.app_name

                    # We execute the command
                    self.print_log(the_command)
                    # We do a cd before pyinstaller
                    ss(the_command)
                    self.print_log("Application successfully generated !!!!!")
                    self.print_log("-----------------------------------------------")
                else:
                    self.stop("Stopping, PyInstaller not available !")
            else:
                self.stop("Stopping, requirements not available !")
        else:
            self.stop("Stopping, main not available !")
