
from openai import OpenAI
import chapters
import pdf_creator
import web_scraper

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)

api_rolle = "You are a Translator. One of your less experienced co-workers comes over with his work and you have to fix the erros they oversaw. Sometimes the co-worker zones out so text that look like ads get added and you need to remove those. Dont add any unessicary comments. Just give out the improved chapter."
url = "https://novelbin.com/b/bjorn-yandel-the-barbarian/chapter-"

for i in range(chapters.chapter_start, chapters.chapter_end):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": api_rolle},
            {"role": "user", "content": web_scraper.scrape_chapter_text(f"{url}{i}")}
        ]
    )
    # print("response er ", response)
    pdf_creator.create_pdf(response.choices[0].message.content, i)


