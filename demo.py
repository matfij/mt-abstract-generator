import spacy
import pytextrank

# example text
text = """
Whether you’re cradling a travel mug on your way to work or dashing out after spin class to refuel with a skinny latte, it’s hard to imagine a day without it. The caffeine perks you up, and there’s something incredibly soothing about sipping a steaming cup of joe. But is drinking coffee good for you?

Good news: The case for coffee is stronger than ever. Study after study indicates you could be getting more from your favorite morning beverage than you thought: Coffee is chock full of substances that may help guard against conditions more common in women, including Alzheimer’s disease and heart disease.

“Caffeine is the first thing that comes to mind when you think about coffee. But coffee also contains antioxidants and other active substances that may reduce internal inflammation and protect against disease,” says Diane Vizthum, M.S., R.D., research nutritionist for Johns Hopkins University School of Medicine.
"""
# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_lg")

# add PyTextRank to the spaCy pipeline\
text_rank = pytextrank.TextRank()
nlp.add_pipe(text_rank.PipelineComponent, name='textrank', last=True)
doc = nlp(text)

# examine the top-ranked phrases in the document
for sentence in doc._.textrank.summary():
    print(sentence)