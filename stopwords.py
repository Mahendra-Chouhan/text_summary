# encoding: UTF-8

english = """
all six eleven just less being indeed over both anyway detail four front already through yourselves fify
mill still its before move whose one system also somewhere herself thick show had enough should to only
seeming under herein ours two has might thereafter do them his around thereby get very de none cannot
every whether they not during thus now him nor name regarding several hereafter did always cry whither
beforehand this someone she each further become thereupon where side towards few twelve because often ten
anyhow doing km eg some back used go namely besides yet are cant our beyond ourselves sincere out even
what throughout computer give for bottom mine since please while per find everything behind does various
above between kg neither seemed ever across t somehow be we who were sixty however here otherwise whereupon
nowhere although found hers re along quite fifteen by on about didn last would anything via of could thence
put against keep etc s became ltd hence therein onto or whereafter con among own co afterwards formerly
within seems into others whatever yourself down alone everyone done least another whoever moreover couldnt
must your three from her their together top there due been next anyone whom much call too interest thru
themselves hundred was until empty more himself elsewhere mostly that fire becomes becoming hereby but
else part everywhere former don with than those he me forty myself made full twenty these bill using up us
will nevertheless below anywhere nine can theirs toward my something and sometimes whenever sometime then
almost wherever is describe am it doesn an really as itself at have in seem whence ie any if again hasnt
inc un thin no perhaps latter meanwhile when amount same wherein beside how other take which latterly you
fill either nobody unless whereas see though may after upon therefore most hereupon eight amongst never
serious nothing such why a off whereby third i whole noone many well except amoungst yours rather without
so five the first having once
"""



LANGUAGES = {"english": english}

def get_stopwords_by_language(language):
    if language in LANGUAGES:
        return LANGUAGES[language]
    return LANGUAGES["english"]
