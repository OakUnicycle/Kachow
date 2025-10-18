import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file
API_KEY = os.getenv("OPENAI_API_KEY")


# Set your API key
os.environ["OPENAI_API_KEY"] = API_KEY
client = OpenAI()

source_article_text = """
President Volodymyr Zelensky appears to have come away empty-handed from a White House meeting after US President Donald Trump indicated he was not ready to supply sought-after Tomahawk cruise missiles to Ukraine.

Zelensky said after the cordial bilateral talks that he and Trump had talked about long-range missiles, but decided not to make statements on the issue "because the United States does not want an escalation".

Following the meeting, Trump took to social media to call for Kyiv and Moscow to "stop where they are" and end the war.

The Trump-Zelensky meeting came a day after Trump spoke with Russian President Vladimir Putin by phone and agreed to meet him in Hungary soon.

Zelensky believes using Tomahawks to strike at Russian oil and energy facilities would severely weaken Putin's war economy.

While Trump did not rule it out, his tone at the White House on Friday was non-committal.

"Hopefully they won't need it, hopefully we'll be able to get the war over without thinking about Tomahawks," the US president said, adding: "I think we're fairly close to that."

He described the weapons as "a big deal" and said that the US needed them for its own defence. He also said that supplying Tomahawks to Ukraine could mean a further escalation in the conflict, but that discussions about sending them would continue.

Asked by the BBC if the Tomahawks had prompted Putin to meet Trump, the US president said: "The threat of that [the missiles] is good, but the threat of that is always there."
Media caption,

Trump tells BBC Putin 'wants to make a deal', cites threat of Tomahawks

The Ukrainian leader suggested his country could offer drones in exchange for the Tomahawks, prompting smiles and nodding from Trump.

Zelensky also complimented Trump on his role in securing the first phase of a peace deal in the Middle East, suggesting the US leader could build on that momentum to help end Russia's war in Ukraine.

After the meeting, Zelensky was asked by a reporter outside the White House if he thought Putin wanted a deal or was just buying time with the planned meeting with Trump in Budapest.

"I don't know," he said, adding that the prospect of Ukraine having Tomahawks had caused Russia to be "afraid because it is a strong weapon".

Asked if he was leaving Washington more optimistic that Ukraine would get the Tomahawks, he said: "I am realistic."

The Ukrainian leader also appeared to suggest he would be amenable to Trump's suggestion of stopping the war along the current front line.

"We have to stop where we are, he is right, the president is right," Zelensky said. He added that the step after that would be "to speak".

He later posted on X, saying that he had called European leaders to share details of the meeting with Trump, adding that the "main priority now is to protect as many lives as possible, guarantee security for Ukraine, and strengthen all of us in Europe."

UK Prime Minister Keir Starmer said the call with European leaders was "productive" and promised that "the UK will continue to send humanitarian aid and military support".

While Trump had shown an openness to the idea of selling the Tomahawks in recent days, Putin warned that such a move would further strain the US-Russian relationship.

On Thursday, Trump said "great progress" was made during a phone call with Putin, with the pair agreeing to face-to-face talks soon in Hungary - although no date has been set.

Asked by a reporter on Friday if he was concerned Putin might be playing for time by agreeing to a new summit, Trump said: "I am."

"But I've been played all my life by the best of them, and I came out really well. So, it's possible, a little time, it's alright. But I think that I'm pretty good at this stuff. I think that he wants to make a deal," he said.

When asked by another reporter whether Zelensky would be involved in the prospective talks in Budapest, Trump - who was sat beside the Ukrainian president said there was "bad blood" between Putin and Zelenksy.

"We want to make it comfortable for everybody," Trump said. "We'll be involved in threes, but it may be separated." He added that the three leaders "have to get together".
Media caption,

Watch: How might Tomahawk missiles change the Ukraine-Russia war?

The US president said his call, the first with Putin since mid-August, was "very productive", adding that teams from Washington and Moscow would meet next week.

Trump had hoped a face-to-face summit in Alaska in August would help convince Putin to enter into comprehensive peace talks to end the war, but that meeting failed to produce a decisive breakthrough.

They spoke again days later when Trump interrupted a meeting with Zelensky and European leaders to call Putin.

Back in Ukraine, the BBC spoke on Friday to a couple repairing the small store they own in a suburb of Kyiv, after it was obliterated by Russian missiles last month.

When the store-owner, Volodymyr, was asked about Trump's forthcoming summit meeting with Putin, he began to say: "We appreciate all support".

But he stepped away as tears welled up in his eyes. After a long pause, he composed himself and started again.

"Truth and democracy will win, and all the terrorism and evil will disappear," he said. "We just want to live, we don't want to give up, we just want them to leave us alone."
"""

# A prompt designed to extract key info and create search queries
# We use JSON mode for a reliable, parsable output
system_prompt = """
You are a news analyst. Your task is to analyze the provided article
and generate 3-5 relevant search queries to find similar, more recent
news articles.

Return your answer in JSON format with two keys:
1. "main_topic": A brief summary of the main event.
2. "search_queries": A list of 5 search strings.
"""

try:
    response = client.chat.completions.create(
        model="gpt-4o",  # Use a modern, capable model
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": source_article_text}
        ]
    )

    # Parse the JSON response
    analysis = json.loads(response.choices[0].message.content)

    print(f"Main Topic: {analysis['main_topic']}\n")
    print("Generated Search Queries:")
    for query in analysis['search_queries']:
        print(f"  - {query}")

    # Store the queries for the next step
    search_queries_list = analysis['search_queries']
    import google_search as gs
    gs.print_results(gs.google_search(search_queries_list[0]))

except Exception as e:
    print(f"An error occurred: {e}")
