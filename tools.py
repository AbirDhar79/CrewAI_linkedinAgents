# from crewai_tools import YoutubeChannelSearchTool

# # Initialize the tool with a specific Youtube channel handle to target your search
# yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')

from crewai_tools import YoutubeVideoSearchTool

def get_yt_video_tool(video_url):
    """Create YouTube video tool with the provided URL"""
    return YoutubeVideoSearchTool(
        youtube_video_url=video_url,
        config=dict(
            llm=dict(
                provider="openai",
                config=dict(
                    model="gpt-4-0125-preview",
                    temperature=0.7
                ),
            ),
            embedder=dict(
                provider="openai",
                config=dict(
                    model="text-embedding-ada-002"
                ),
            ),
        )
    )

# Initialize with a placeholder - will be updated when crew runs
yt_video_tool = get_yt_video_tool("")