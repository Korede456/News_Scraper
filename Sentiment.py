from textblob import TextBlob
def SentOriginal():
    Text = str("It was a good movie")

    Polarity = TextBlob(Text).sentiment.polarity
    Subjectivity = TextBlob(Text).sentiment.subjectivity

    PolarText = ()
    SubjText = ()

    if Polarity >= 0.5:
        PolarText = " highly positive sentiment"
    elif Polarity <= -0.5:
        PolarText = "highly negative sentiment"
    else:
        PolarText = "neutral sentiment"

    if Subjectivity < 0.5:
        SubjText = "more subjective perspective"
    else:
        SubjText = "more objective perspective"

    AnalysisOriginal = (f'The text is written with a {PolarText}  from a {SubjText}')


def SentParaphrased():
    Text = str("It was a good movie")

    Polarity = TextBlob(Text).sentiment.polarity
    Subjectivity = TextBlob(Text).sentiment.subjectivity

    PolarText = ()
    SubjText = ()

    if Polarity >= 0.5:
        PolarText = " highly positive sentiment"
    elif Polarity <= -0.5:
        PolarText = "highly negative sentiment"
    else:
        PolarText = "neutral sentiment"

    if Subjectivity < 0.5:
        SubjText = "more subjective perspective"
    else:
        SubjText = "more objective perspective"

    AnalysisParaphrased = (f'The text is written with a {PolarText}  from a {SubjText}')

