selectChunks_outputs = [{'chunk_id': '0', 'content': 'Title: UKG Global Executive Presentation Deck.pdfWe selected UKG because \nthey have p...y \nrequirements for the \ncountry or area.\n', 'filepath': 'Sales Pitch Decks/UKG Global Executive Presentation Deck.pdf', 'metadata': None, 'score': 0.01639344262295082, 'title': 'UKG Global Executive Presentation Deck.pdfWe selected UKG because', 'url': 'Sales Pitch Decks/UKG Global Executive Presentation Deck.pdf'}, {'chunk_id': '0', 'content': 'Title: UKG Global Executive Presentation Deck.pdfAdrian Peace\nProductivity \nand Devel...rs15M+ EEs \nlive on UKG \naround the world\n', 'filepath': 'Sales Pitch Decks/UKG Global Executive Presentation Deck.pdf', 'metadata': None, 'score': 0.016129032258064516, 'title': 'UKG Global Executive Presentation Deck.pdfAdrian Peace', 'url': 'Sales Pitch Decks/UKG Global Executive Presentation Deck.pdf'}, {'chunk_id': '0', 'content': 'Title: UKG Global Executive Presentation Deck.pdf© 2020 UKG Inc. All rights reserved.Global Executive \nPresentation', 'filepath': 'Sales Pitch Decks/UKG Global Executive Presentation Deck.pdf', 'metadata': None, 'score': 0.015873015873015872, 'title': 'UKG Global Executive Presentation Deck.pdf© 2020 UKG Inc. All rights reserved.Global Executive', 'url': 'Sales Pitch Decks/UKG Global Executive Presentation Deck.pdf'}, {'chunk_id': '0', 'content': 'Title: UKG Testing Strategy Meeting PRO and Automation Version.pdfUKG Logo and Tagline\n45', 'filepath': 'Deployment Methodology/UKG Testing Strategy Meeting PRO and Automation Version.pdf', 'metadata': None, 'score': 0.015625, 'title': 'UKG Testing Strategy Meeting PRO and Automation Version.pdfUKG Logo and Tagline', 'url': 'Deployment Methodology/UKG Testing Strategy Meeting PRO and Automation Version.pdf'}, {'chunk_id': '0', 'content': 'Title: Analysis Readiness (ProDimensions)_PPT.pdf•What is Analysis?\n•Source Vendor Re...mers\n•Collecting System RequirementsAgenda', 'filepath': 'Deployment Methodology/Analysis Readiness (ProDimensions)_PPT.pdf', 'metadata': None, 'score': 0.015384615384615385, 'title': 'Analysis Readiness (ProDimensions)_PPT.pdf•What is Analysis?', 'url': 'Deployment Methodology/Analysis Readiness (ProDimensions)_PPT.pdf'}]
intent = ["what is ukg?"]

# def change_chunk_output(chunk_output: list):
#     """
#     This function just changes the list chunk_output
#     """
#     for chunk in chunk_output:
#         del chunk['metadata']
#         del chunk['score']
#     return chunk_output

def changeselectChunks_format(chunk_output: list, intent:list):
    """
    The output from selectChunks should be a string with a defined structure
    So we need to transform it into a dictionary first (the structure), and then into a string
    """
    # First, chunk_output has to have a different structure
    for chunk in chunk_output:
        del chunk['metadata']
        del chunk['score']
    output_dict = {"citations":chunk_output,"intent":intent}
    output = str(output_dict)
    return output

output_dict = changeselectChunks_format(selectChunks_outputs, intent)
print(output_dict)
print(type(output_dict))
