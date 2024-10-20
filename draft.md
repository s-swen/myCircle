@s-swen ➜ /workspaces/myCircle (main) $ source $HOME/.bashrc
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/postmkproject
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/initialize
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/premkvirtualenv
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/postmkvirtualenv
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/prermvirtualenv
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/postrmvirtualenv
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/predeactivate
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/postdeactivate
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/preactivate
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/postactivate
virtualenvwrapper.user_scripts creating /home/codespace/.virtualenvs/get_env_details

@s-swen ➜ /workspaces/myCircle (main) $ echo $HOME
/home/codespace

mkvirtualenv my_django_environment
deactivate — Exit out of the current Python virtual environment
workon — List available virtual environments
workon name_of_environment — Activate the specified Python virtual environment

export WORKON_HOME=/home/codespace/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/home/codespace/.python/current/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /home/codespace/.python/current/bin/python3 '
export PROJECT_HOME=/workspaces/myCircle
source /home/codespace/.python/current/bin/virtualenvwrapper.sh
