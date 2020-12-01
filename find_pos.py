#%%



from os.path import join
from typing import List
import io

from jpype import JClass, getDefaultJVMPath, java, shutdownJVM, startJVM

if __name__ == '__main__':

    ZEMBEREK_PATH: str = join('..', '..', 'bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()

    #sentence: str = 'Keşke yarın hava güzel olsa'
    filename = 'text_1.txt' 
    with io.open(filename, 'r', encoding='utf8') as f:
        
        text_1 = f.read()

    analysis: java.util.ArrayList = (
        morphology.analyzeAndDisambiguate(text_1).bestAnalysis()
    )

    pos: List[str] = []

    for i, analysis in enumerate(analysis, start=1):
        print(
            f'\nAnalysis {i}: {analysis}',
            f'\nPrimary POS {i}: {analysis.getPos()}'
            f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}'
        )
        pos.append(
            f'{str(analysis.getLemmas()[0])}'
            f'-{analysis.getPos().shortForm}'
        )

    print(f'\nFull sentence with POS tags: {" ".join(pos)}')

    shutdownJVM()
#%%

import trnlp
from trnlp import TrnlpWord
from trnlp import *

text = open("text_1.txt","r", encoding = 'utf-8')   # We defined our corpus about intermitten fasting
corpus=text.read()





ayri = simple_token(corpus)

print(ayri)

for i in range(0,len(ayri)):
    obj = TrnlpWord()
    obj.setword(ayri[i])
    tagged= obj.get_morphology
    print(tagged,"\n")
#%%