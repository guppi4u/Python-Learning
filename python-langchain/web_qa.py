import os
import asyncio
import nest_asyncio
from langchain_anthropic import ChatAnthropic
from langchain_community.agent_toolkits.playwright.toolkit import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
# THE NEW 2026 IMPORT:
from langgraph.prebuilt import create_react_agent

nest_asyncio.apply()

async def main():
    # 1. Setup Browser & Tools
    browser = create_async_playwright_browser()
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    tools = toolkit.get_tools()

    # 2. Setup Claude 4.6
    api_key = os.getenv("LANGCHAIN_KEY")
    # In 2026, we use 'anthropic_api_key' to be explicit
    llm = ChatAnthropic(model="claude-sonnet-4-6", anthropic_api_key=api_key, temperature=0)

    # 3. CREATE THE AGENT
    # This is much simpler than the old 'initialize_agent'
    agent_executor = create_react_agent(llm, tools)

    print("--- 🕵️ AI QA Agent (2026 version) is NAVIGATING ---")
    
    # 4. Run the Agent
    # New agents use the 'invoke' pattern with a 'messages' list
    inputs = {"messages": [("user", "Go to https://www.google.com and tell me the text on the search button.")]}
    # The Agent will automatically navigate, then find the 'Gmail' link, then click it.
    # query = "1. Go to https://www.google.com. 2. Click on the 'Gmail' link. 3. Tell me the title of the page you are on."

    
    result = await agent_executor.ainvoke(inputs)
    
    # The result contains the whole conversation; we just want the last message
    print(f"\nFINAL RESULT: {result['messages'][-1].content}")

if __name__ == "__main__":
    asyncio.run(main())