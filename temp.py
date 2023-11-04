from presidio_analyzer import AnalyzerEngine
import pprint
from presidio_anonymizer import AnonymizerEngine
pp = pprint.PrettyPrinter(indent=4)
with open('CustSeg-Logs.txt') as f:
    lines = f.readlines()
text = " ".join(lines)
# pp.pprint(text[737398:737413])
analyzer = AnalyzerEngine()
results = analyzer.analyze(text=text,
                           entities=["CREDIT_CARD", "US_SSN", "NRP"],
                           language='en')
pp.pprint(results)

# anonymizer = AnonymizerEngine()
# anonymized_text = anonymizer.anonymize(text=text,analyzer_results=results)
# print(anonymized_text)

# 'Credscore-Logs.txt' 6 FP 0 FN
# 'CustSeg-Logs.txt' 0 FP 0 FN

