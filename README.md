# ChatGPT Bash Terminal Plugin Quickstart

Get a Bash Terminal ChatGPT plugin up and running in under 5 minutes using Python. This plugin allows ChatGPT to interact with your computer's bash terminal, enabling you to execute bash commands directly from the ChatGPT interface. If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup

To install the required packages for this plugin, run the following command:

    pip install -r requirements.txt

To run the plugin, enter the following command:

    python main.py

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start by asking ChatGPT to execute a bash command on your local machine.

## Running in Docker (Recommended)

For added security, we recommend running the plugin inside a Docker container. This provides an additional layer of isolation and helps prevent unintended access to your system.

To run the plugin in Docker, use the following commands:

    # Build the Docker image
    docker build -t bash-terminal-plugin .

    # Run the Docker container
    docker run -p 5003:5003 bash-terminal-plugin

The plugin will now be running and accessible at `http://localhost:5003`. Follow the same steps as above to connect the plugin to ChatGPT.

## Disclaimer

This plugin allows the execution of arbitrary bash commands, which can pose a security risk. It is intended for educational and testing purposes only. Always exercise caution when executing arbitrary bash commands on your system.

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
