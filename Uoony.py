import discord
import asyncio
import random
import os

client = discord.Client()
owner_id = 456519752571944980

@client.event
async def on_ready():
    print(client.user.id)
    print("ProjectHentai is ready")
    game = discord.Game("유우니봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕")

    if message.content.startswith("!유우니"):
        if message.author.id == owner_id:
            await message.channel.send("유우니 천재...?")
        else:
            await message.channel.send("이 명령어를 사용할 권한이 없습니다")

    if message.content.startswith("!트게더"):
        await  message.channel.send("https://tgd.kr/uoony")

    if message.content.startswith("!유우니봇"):
        await  message.channel.send("Made by Ailchenbris/Project Hentai")

    if message.content.startswith("!DiviZara"):
        await  message.channel.send("디비자라")

    if message.content.startswith("!projecthentai"):
        await  message.channel.send("Project Hentai is ready")

    if message.content.startswith("!그룹"):
        await  message.channel.send("https://steamcommunity.com/groups/uooni")

    if message.content.startswith("!유투브"):
        await  message.channel.send("https://www.youtube.com/channel/UCnTJRFM9iXvtFzHdzRgYv5A")

    if message.content.startswith("!능지"):
        await  message.channel.send("처참")

    if message.content.startswith("!유하"):
        await message.channel.send("트하")

    if message.content.startswith("!유바니보"):
        await message.channel.send("유우니 바보 아니다...?")

    if message.content.startswith("!명령어"):
        help = discord.Embed(title="모든 사용 가능한 명령어 목록, 앞에 !입력 후 사용하세요", description="ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        help.add_field(name="안녕", value="안녕이라고 대답해줍니다", inline=False)
        help.add_field(name="유우니", value="스트리머 유우니에 대해 설명해줍니다", inline=False)
        help.add_field(name="유바니보", value="유우니 바보 아니다....?")
        help.add_field(name="능지", value="처참", inline=False)
        help.add_field(name="트게더", value="유게더 주소", inline=False)
        help.add_field(name="그룹", value="스팀그룹 가입링크", inline=False)
        help.add_field(name="유하", value="트수에게 인사해줍니다.", inline=False)
        help.add_field(name="유투브", value="유우니의바보상자 주소, 구독,좋아요 부탁드려요", inline=False)
        help.add_field(name="Divizara", value="디비자라", inline=False)
        help.add_field(name= "오늘 뭐먹지?", value="오늘 먹을 메뉴를 추천해줍니다", inline=False)
        help.add_field(name= "내일 뭐먹지?", value="내일 먹을 메뉴를 추천해줍니다", inline=False)
        help.add_field(name= "오늘 뭐잡지?", value="오늘 잡을 몬스터나, 조사퀘 보상 등을 지정해줍니다", inline=False)
        help.add_field(name= "오늘 뭐쓰지?", value="수렵시 사용할 무기를 지정해줍니다", inline=False)
        await message.channel.send(content=None, embed=help)

    if message.content.startswith("!오늘 뭐먹지?"):
        food = "중식 한식 분식 일식 치킨 피자 족발 보쌈 찜 탕 도시락 패스트푸드 디저트"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await message.channel.send(foodresult)

    if message.content.startswith("!내일 뭐먹지?"):
        food = "중식 한식 분식 일식 치킨 피자 족발 보쌈 찜 탕 도시락 패스트푸드 디저트"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await message.channel.send(foodresult)

    if message.content.startswith("!오늘 뭐잡지?"):
        food = "[멸진룡]네르기간테 [암적룡]도도가마루 [비적룡]도스기르오스 [적룡]도스쟈그라스 [각룡]디아블로스 [흑각룡]디아블로스아종 [골추룡]라도발킨 [풍표룡]레이기에나 [화룡]리오레우스 " \
               "[창화룡]리오레우스아종 [자화룡]리오레이아 [앵화룡]리오레이아아종 [폭린룡]바젤기우스 [시투룡]발하자크 [용암룡]볼가노스 [토사룡]볼보로스 [만악룡]안쟈나프 [참조룡]오도가론 " \
               "[폭추룡]우라간킨 [용산룡]조라-마그다라오스 [이어룡]쥬라토도스 [현조]치치야크 [소조]쿠루루야크 [강룡]크샬다오라 [환수]키린 [염왕룡]테오-테스카토르 " \
               "[비뢰룡]토비카가치 [부공룡]파오우르무 [독요조]푸케푸케 [명등룡]제노-지바 [공폭룡]이블조 [염비룡]나나-테스카토리 [마수]베히모스 [하위]조사퀘스트 " \
               "[상위]조사퀘스트 [역전]조사퀘스트 [조사]1수레-퀘스트 [조사]2수레-퀘스트 [조사]3수레-퀘스트 [조사]4수레-퀘스트 [조사]5수레-퀘스트 [하위]자유퀘스트 " \
               "[상위]자유퀘스트 [자유]격투장퀘스트 [조사]2금보상-퀘스트 [조사]1금보상-퀘스트 [고룡종] [비룡종] [수룡종] [조룡종] [어룡종] [아룡종]"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await message.channel.send(foodresult)

    if message.content.startswith("!오늘 뭐쓰지?"):
        food = "근거리무기 원거리무기 대검 한손검 해머 랜스 슬래시액스 조충곤 태도 쌍검 수렵피리 건랜스 차지액스 헤비보우건 활 라이트보우건"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await message.channel.send(foodresult)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

