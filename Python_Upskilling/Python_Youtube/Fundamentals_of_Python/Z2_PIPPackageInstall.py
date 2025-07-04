# ========== Third Party Packages and PIP ==========

print( "Installing Third Party Packages Using PIP")

## ======= Installing Third Party Packages in Python Using PIP =========
    # Python standard library contains large number of utlilies which simply our python development needs
        # However, not one utility alone can of course satisy all a users needs
        # This is why individuals and companies create packages and make them available as open source sw for the entire community 
    # Modules are all collected in a single place called Python Package Index
        # Available at pypi.org
        # Now these packages can be installed on the system using PIP
        # Most computers already have PIP installed
        # Over 270,000 packages freely available

# How to install a package:
    # Open up command line and type in pip install
        # pip install requests --> installs requests package and makes package available for all python scripts
        # Can also upgrade package to it's latest version by putting:
            # pip install - u requests
            # In this case here in command line would upgrade from 2.2.0 to 2.2.1
        # Note, can also classify specific version when you're installing
    # You can also uninstall a package by running
        # pip uninstall requests
    # If you want to find some information out about the package you can also run 
        # pip show requests 
            # where show is used to request more detail about the requests
                # Including the name, the version the summary etc.