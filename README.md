# Fedora-Package-Command-Line-Flash-Cards
Command Line Flash Cards for Fedora using https://github.com/fawzisal/study-cli

The following steps can be used to created the Command Line Flash Cards package:

Note: Terminal commands are provided in <>. Do not include <> when entering commands into terminal.

1. Install the necessary tools: 
In order to create the RPM package, you need to have a few tools installed on your system. These tools include rpmbuild, spectool, rpmdevtools, python3-devel, python3-setuptools, and python3-wheel. You can install these tools using the following command:
<sudo dnf install -y rpmbuild spectool rpmdevtools python3-devel python3-setuptools python3-wheel>

2. Create a new directory for the RPM build files:
<mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}>
Copy the source code for Command Line Flash Cards from PyPI into the ~/rpmbuild/SOURCES/ directory:
<cd ~/rpmbuild/SOURCES/>
<wget https://files.pythonhosted.org/packages/0c/58/0802bf2cc7ddfec15b49680f7c44e76eb11c5841a19f0deef4a4ac4fcd8a/study-cli-0.0.1.tar.gz>

3. Create a new spec file called study-cli.spec in the ~/rpmbuild/SPECS/ directory:
<cd ~/rpmbuild/SPECS/>
<gedit study-cli.spec>
Copy and paste the provided spec file contents into the study-cli.spec file and click save.
Be sure to update the changelog accordingly at the bottom of the spec file.

4. Build the RPM package:
<rpmbuild -bb study-cli.spec>
This will create the RPM package in the ~/rpmbuild/RPMS/noarch directory.

5. Install the RPM package:
You can install the RPM package using the following command:
<sudo dnf install -y ~/rpmbuild/RPMS/noarch/study-cli-0.0.1-1.fc33.noarch.rpm>

6. Check if the study-cli package is installed correctly:
<rpm -qa | grep study-cli>
This command will list all the installed packages on your system that have "study-cli" in their name.

7. Test the study-cli command:
<study-cli --help>
This command should display the help message for the study-cli command. If it does not display the help message, there may be an issue with the installation.

8. Create a new study:
<study-cli create my_study>
This command should create a new study named "my_study". If it does not create a new study, there may be an issue with the installation or the user permissions.

9. List all the studies:
<study-cli list>
This command should list all the studies on your system. If it does not list any studies or if it returns an error, there may be an issue with the installation or the user permissions.

10. Delete a study:
<study-cli delete my_study>
This command should delete the study named "my_study". If it does not delete the study, there may be an issue with the installation or the user permissions.

If all these commands run without any errors, then the study-cli software should be working correctly on your Fedora machine.

