# Fedora-Package-Command-Line-Flash-Cards
Command Line Flash Cards for Fedora using https://github.com/fawzisal/study-cli

The following steps can be used to created the Command Line Flash Cards package:

Note: Terminal commands are provided in <>. Do not include <> when entering commands into terminal.

1. Install the necessary tools: 
You'll need to have some tools installed before you can begin packaging. Install them by running the following command:
<sudo dnf install rpmdevtools rpmlint mock>
This will install the RPM development tools, RPM linting tool, and the mock build tool.

2. Set up the RPM development environment: Run the following command to set up the RPM development environment:
<rpmdev-setuptree>
This will create the necessary directories for packaging and building RPMs.

3. Download the study-cli source code: Clone the study-cli source code from GitHub by running the following command:
<git clone https://github.com/study-cli/study-cli.git>
This will create a new directory named "study-cli" that contains the source code.

4. Create a spec file: In order to package the study-cli source code into an RPM, you'll need to create a spec file. 
Create a new file named "study-cli.spec" in the RPM development directory:
<cd ~/rpmbuild/SPECS>
<touch study-cli.spec>
Open the "study-cli.spec" file in a text editor and add the provided spec file contents.
Be sure to appropriately adjust the change log as needed at the bottom of the spec file.

5. Build the RPM: Now that you've created the spec file, you can use it to build the RPM package. Run the following command:
<rpmbuild -ba study-cli.spec>
This will build the RPM package and place it in the RPM build directory.

6. Install the RPM: Once the RPM is built, you can install it on your system. Run the following command:
<sudo dnf install ~/rpmbuild/RPMS/x86_64/study-cli-0.0.1-1.fc34.x86_64.rpm>
This will install the study-cli package on your Fedora system.

7. Check if the study-cli package is installed correctly:
<rpm -qa | grep study-cli>
This command will list all the installed packages on your system that have "study-cli" in their name.

8. Test the study-cli command:
<study-cli --help>
This command should display the help message for the study-cli command. If it does not display the help message, there may be an issue with the installation.

9. Create a new study:
<study-cli create my_study>
This command should create a new study named "my_study". If it does not create a new study, there may be an issue with the installation or the user permissions.

10. List all the studies:
<study-cli list>
This command should list all the studies on your system. If it does not list any studies or if it returns an error, there may be an issue with the installation or the user permissions.

11. Delete a study:
<study-cli delete my_study>
This command should delete the study named "my_study". If it does not delete the study, there may be an issue with the installation or the user permissions.

If all these commands run without any errors, then the study-cli software should be working correctly on your Fedora machine.

