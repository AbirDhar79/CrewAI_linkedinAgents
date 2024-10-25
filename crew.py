# from crewai import Crew,Process
# from agents import blog_researcher,blog_writer
# from tasks import research_task,write_task


# # Forming the tech-focused crew with some enhanced configurations
# crew = Crew(
#   agents=[blog_researcher, blog_writer],
#   tasks=[research_task, write_task],
#   process=Process.sequential,  # Optional: Sequential task execution is default
#   memory=True,
#   cache=True,
#   max_rpm=100,
#   share_crew=True
# )

# ## start the task execution process with enhanced feedback
# result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
# print(result)

from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from tools import get_yt_video_tool, yt_video_tool
import sys

def analyze_video(video_url):
    # Update the YouTube tool with the provided URL
    global yt_video_tool
    yt_video_tool = get_yt_video_tool(video_url)
    
    # Create crew
    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True
    )

    # Execute tasks
    result = crew.kickoff(inputs={'video_url': video_url})
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crew.py <youtube_video_url>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    result = analyze_video(video_url)
    print(result)