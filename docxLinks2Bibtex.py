'''
Fetches bibtex entries as described here: https://www.crossref.org/labs/citation-formatting-service/
Docx Link iterator from:  https://stackoverflow.com/questions/40475757/how-to-extract-the-url-in-hyperlinks-from-a-docx-file-using-python#40476383
'''

import sys
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from urllib.parse import urlparse
import requests
from pybib_utils import get_bibtex

if __name__ == "__main__":

    assert len(sys.argv) == 3, "Improper Usage! Please use as \'python docxLinks2Bibtex.py <path to input DOCX> " \
                               "<path of output BIB file>"

    inDocx = sys.argv[1]
    outBib = sys.argv[2]
    document = Document(inDocx)
    rels = document.part.rels

    def iter_hyperlink_rels(rels):
        for rel in rels:
            if rels[rel].reltype == RT.HYPERLINK:
                yield rels[rel]._target

    doisDone = []
    with open(outBib, 'w') as fle:
        for link in iter_hyperlink_rels(rels):
            parseResult = urlparse(link)
            if parseResult.netloc == "doi.org":
                doi = parseResult.path[1:]
                if doi not in doisDone:
                    doisDone.append(doi)
                    print("Doing {}".format(doi))
                    bibEntry = get_bibtex(doi)
                    if bibEntry:
                        fle.write(bibEntry + "\n")






