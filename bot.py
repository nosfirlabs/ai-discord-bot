import discord
import requests

# Set up the Discord client
client = discord.Client()

# Define a command that makes a request to the external API and returns the response
@client.event
async def on_message(message):
    if message.content.startswith('!api'):
        # Return the response to Discord
        await message.channel.send(await do_ai_request(message.content.replace("!api", "")))

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
    
async def do_ai_request(aitext: str):
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://chai.ml/',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'developer_uid': 'mUCsg14rQqYbpRkcqMbiPKa29xg1',
        'developer_key': 'sLdHjVjwMKd_7pd4C4l8S8yugfqq8caILaez7KJAmtKrZErnAOIVx_RoyOF6xRcAMvQ_yqlkxEWi87X0FIoaOg',
        'Origin': 'https://chai.ml',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    json_data = {
        'text': aitext,
        'temperature': 0.7,
        'repetition_penalty': 1.1,
        'top_p': 1,
        'top_k': 40,
        'response_length': 64,
    }
    data = ""
    try:
         data = requests.post('https://model-api-shdxwd54ta-nw.a.run.app/generate/gptj', headers=headers,
                             json=json_data).json()["data"]
    except KeyError:
        print("AI failed to answer.")
        data = "I don't know what to say."
    finally:
        return data
