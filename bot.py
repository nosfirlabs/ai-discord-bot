import discord
import requests

# Set up the Discord client
client = discord.Client()

# Set the URL of the external API server
uri = 'https://api.example.com/endpoint'

# Define a command that makes a request to the external API and returns the response
@client.event
async def on_message(message):
    if message.content.startswith('!api'):
        # Make the request to the external API
        response = requests.get(uri)

        # Return the response to Discord
        await message.channel.send(response.text)

# Run the bot using the bot's token
client.run('YOUR_BOT_TOKEN')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
