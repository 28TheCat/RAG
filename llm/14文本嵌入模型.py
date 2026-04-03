from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv

load_dotenv()
embed = DashScopeEmbeddings()

print(embed.embed_query("喵喵"))
print(embed.embed_documents([
    '我有午饭',
    '我吃肉',
    '我喜欢听音乐'
]))
