import discord, datetime, asyncio, random
import os

token = "access_token"

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 활성화 됨")
    print(client.user)
    print("===============================")

@client.event
async def on_message(message):
    if message.content == "-help":
        await message.channel.send("이 기능은 아직 지원하지 않아요.")    
    if message.content == "!득호":
        await message.channel.send("득호는 바보")
    if message.content == "!건우":
        await message.channel.send("건우 바보 :)")
    if message.content == "생산지":
        await message.channel.send("저는 대한민국에서 만들어졌어요")
    if message.content == "":
        await message.channel.send("득호는 바보")


    if message.content =="내정보":
        user = message.author
        data = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {data.year}/{data.month}/{data.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content == "!탈모 확률":
        await message.channel.send(random.choice(["1% 아이고 탈모..", "2%", "3%", "4% 탈모세포가 0.0001mm로 매우 작아요", "5%", "6%", "7%", "8%", "9%", "10%", "11%", "12%", "13%", "14%", "15% 괞찮아요..!", "16%", "17%", "18%", "19%", "20%", "21%", "22%", "23%탈모 이겨낼수 있어요!", "24%", "25%", "26%", "27%", "28%", "29%", "30% 탈모 초기 단계에요..!", "31%", "32%", "33%", "34%", "35%", "36%", "37%", "38%", "39%", "40% 잘하면 탈모를 막을수있어요!", "41%", "42%", "43%", "44%", "45%", "46%", "47%", "48%", "49%", "50% 탈모가 진행중이에요", "51%", "52%", "53%", "54%", "55%", "56%", "57%", "58%", "59%", "60%", "61%", "62%", "63%", "64%", "65%", "66% ㅠㅠ", "67%", "68%", "69%", "70%", "71%", "72%", "73%", "74%", "75%", "76%", "77%", "78%", "79%", "80%", "81%", "82%", "83%", "84%", "85%", "86%", "87%", "88%", "89% 힘네요!", "90%", "91%", "92%", "93%", "94%", "95%", "96%", "97%", "98%", "99%", "100%", "0% 탈모가 아니에요 축하해요", "탈모 말기에요.. 조심하세요!", "99.9% 우리 매일  이 고통을 느끼고 있을 성재한테 위로의 말 전해봐요"]))
    
    if message.content == "!타이머":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}님 10초가 지났어요!")

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지가 삭제되었어요")

access_token - os.environ["BOT_TOKEN"]        
client.run()
