from app.core.config import Settings, get_settings

settings = get_settings()

print(f"App Name: {settings.app_name}")
print(f"App Environment: {settings.app_env}")
print(f"GROQ API Key: {settings.groq_api_key}")
print(f"Tavily API Key: {settings.tavily_api_key}")
print(f"Pinecone API Key: {settings.pinecone_api_key}")
print(f"Pinecone Index Name: {settings.pinecone_index_name}")
print(f"Pinecone Namespace: {settings.pinecone_namespace}")
print(f"Embedding Model: {settings.embedding_model}")
print(f"GROQ Model: {settings.groq_model}")
print(f"Top K: {settings.top_k}")
print(f"Max Retries: {settings.max_retries}")