# from crewai import Task
# from tools import yt_tool
# from agents import blog_researcher,blog_writer

# ## Research Task
# research_task = Task(
#   description=(
#     "Identify the video {topic}."
#     "Get detailed information about the video from the channel video."
#   ),
#   expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
#   tools=[yt_tool],
#   agent=blog_researcher,
# )

# # Writing task with language model configuration
# write_task = Task(
#   description=(
#     "get the info from the youtube channel on the topic {topic}."
#   ),
#   expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
#   tools=[yt_tool],
#   agent=blog_writer,
#   async_execution=False,
#   output_file='new-blog-post.md'  # Example of output customization
# )

from crewai import Task
from tools import yt_video_tool
from agents import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description=(
        "Analyze the provided YouTube video and extract key information. "
        "Focus on main concepts, key points, and important details discussed in the video. "
        "Video URL: {video_url}"
    ),
    expected_output='A comprehensive 3-paragraph report summarizing the key contents and insights from the video.',
    tools=[yt_video_tool],
    agent=blog_researcher,
)

# Writing task
write_task = Task(
    description=(
        "Based on the research provided, create an engaging blog post that explains "
        "the concepts discussed in the video. Make it accessible and informative "
        "for a technical audience while maintaining clarity."
    ),
    expected_output='A well-structured blog post that summarizes and explains the video content in an engaging way.',
    tools=[yt_video_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='blog-post.md'
)
