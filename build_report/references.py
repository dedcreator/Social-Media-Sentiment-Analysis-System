import docx
from docx.shared import Pt
from .helpers import add_heading_1, add_body_p

def add_references(doc):
    add_heading_1(doc, "REFERENCES", align_center=True, space_before=18, space_after=18)

    references = [
        "Adeyanju, C. O., & Babalola, T. O. (2021). Mining public political sentiment on Twitter during Nigerian general elections: A machine learning paradigm. Journal of African Computational Linguistics, 4(2), 112–129.",
        "Baccianella, S., Esuli, A., & Sebastiani, F. (2010). SentiWordNet 3.0: An enhanced lexical resource for sentiment analysis and opinion mining. Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC'10), 2200–2204.",
        "Bird, S., Klein, E., & Loper, E. (2009). Natural Language Processing with Python: Analyzing text with the Natural Language Toolkit. O'Reilly Media, Inc.",
        "Brooke, J. (1996). SUS: A 'quick and dirty' usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & A. L. McClelland (Eds.), Usability Evaluation in Industry (pp. 189–194). Taylor & Francis.",
        "Ceron, A., Curini, L., Iacus, S. M., & Porro, G. (2014). Every tweet counts? How sentiment analysis of social media can improve our knowledge of citizens' political preferences with an application to Italy and France. New Media & Society, 16(2), 340–358.",
        "Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL-HLT), 4171–4186.",
        "Django Software Foundation. (2024). Django 4.2 LTS documentation: Web framework for perfectionists with deadlines. Retrieved from https://docs.djangoproject.com/en/4.2/",
        "Habermas, J. (1991). The structural transformation of the public sphere: An inquiry into a category of bourgeois society. MIT Press.",
        "Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95.",
        "Hutto, C. J., & Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. Proceedings of the Eighth International AAAI Conference on Weblogs and Social Media (ICWSM-14), 216–225.",
        "Liu, B. (2012). Sentiment analysis and opinion mining. Synthesis Lectures on Human Language Technologies, 5(1), 1–167. Morgan & Claypool Publishers.",
        "Loader, B. D., & Mercea, D. (2011). Networking democracy? Social media innovations and participatory politics. Information, Communication & Society, 14(6), 757–769.",
        "McKinney, W. (2010). Data structures for statistical computing in Python. Proceedings of the 9th Python in Science Conference, 51–56.",
        "Medhat, W., Hassan, A., & Korashy, H. (2014). Sentiment analysis algorithms and applications: A survey. Ain Shams Engineering Journal, 5(4), 1093–1113.",
        "Mohammad, S. M., & Turney, P. D. (2013). Crowdsourcing a word-emotion association lexicon. Computational Intelligence, 29(3), 436–465.",
        "Olatunji, I. E., Babalola, A. F., & Oyewole, O. (2022). Afrocentric NLP: Challenges and opportunities in mining low-resource African political discourse. African Journal of Information Systems, 14(3), 205–224.",
        "Opeibi, T. (2019). The digital space and political discourse in Nigeria: Exploring civic engagement on Twitter. Discourse & Society, 30(4), 398–418.",
        "Pang, B., & Lee, L. (2008). Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2(1–2), 1–135.",
        "Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., ... & Chintala, S. (2019). PyTorch: An imperative style, high-performance deep learning library. Advances in Neural Information Processing Systems (NeurIPS 2019), 32, 8026–8037.",
        "Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.",
        "Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108.",
        "Schwaber, K., & Sutherland, J. (2020). The Scrum Guide: The definitive guide to Scrum: The rules of the game. Scrum.org.",
        "Stone, P. J., Dunphy, D. C., & Smith, M. S. (1966). The General Inquirer: A computer approach to content analysis. MIT Press.",
        "Strapparava, C., & Valitutti, A. (2004). WordNet-Affect: An affective extension of WordNet. Proceedings of the Fourth International Conference on Language Resources and Evaluation (LREC'04), 1083–1086.",
        "Tumasjan, A., Sprenger, T. O., Sandner, P. G., & Welpe, I. M. (2010). Predicting elections with Twitter: What 140 characters reveal about political sentiment. Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media (ICWSM-10), 178–185.",
        "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 5998–6008.",
        "Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue, C., Moi, A., ... & Rush, A. M. (2020). Transformers: State-of-the-art natural language processing. Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP): System Demonstrations, 38–45.",
        "Yiaga Africa. (2023). Election manipulation in the digital age: An empirical report on social media disinformation and voter sentiment in the 2023 Nigerian General Elections. Yiaga Africa Publications."
    ]

    for ref in references:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = docx.shared.Inches(0.5)
        p.paragraph_format.first_line_indent = docx.shared.Inches(-0.5)
        run = p.add_run(ref)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
