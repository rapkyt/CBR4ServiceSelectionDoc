import os

import matplotlib.pyplot as plt
from stop_words import get_stop_words
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text3 = open(os.path.join(d, 'Capitulo3.lyx')).read()
text4 = open(os.path.join(d, 'Capitulo4.lyx')).read()
text5 = open(os.path.join(d, 'Capitulo5.lyx')).read()

text = text3 + text4 + text5

latex_stopwords = {
    'align', 'alignment', 'begin_inset', 'begin_layout', 'bottomline', 'cada', 'Caption', 'cell', 'center',
    'CommandInset', 'default', 'emph', 'end_inset', 'end_layout', 'english', 'false', 'Flex', 'Foot', 'footnotesize',
    'Formula', 'Itemize', 'label', 'lang', 'LatexCommand', 'Layout', 'left', 'leftline', 'Newline', 'none', 'Note',
    'on', 'Paragraph', 'Plain', 'ref', 'reference', 'rightline', 'row', 'scriptsize', 'sideways', 'size', 'Standard',
    'Status', 'stop', 'Text', 'top', 'topline', 'true', 'URL', 'use_package', 'usebox', 'valignment', 'wide'
}


stopwords = set(get_stop_words('spanish')) | latex_stopwords

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=2000, max_font_size=50).generate(text)

# Display the generated image:
# the matplotlib way:
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
