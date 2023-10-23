import streamlit as st

markdown_text = '''
# Top 10 Python Libraries for HL7 v2, v3, and v4 📚

1. **hl7apy** 🐍
    - A Python library for HL7 v2.x messages
    - [GitHub](https://github.com/crs4/hl7apy)
    - Example:
    ```python
    from hl7apy.parser import parse_message
    message = "MSH|^~\\&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A01|MSG00001|P|2.4"
    parsed_message = parse_message(message)
    print(parsed_message)
    ```

2. **python-hl7** 📄
    - A simple HL7 v2.x parsing library
    - [GitHub](https://github.com/johnpaulett/python-hl7)
    - Example:
    ```python
    import hl7
    message = "MSH|^~\\&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A01|MSG00001|P|2.4"
    parsed_message = hl7.parse(message)
    print(parsed_message)
    ```

3. **hl7v3** 🌐
    - A Python library for HL7 v3 messages
    - [GitHub](https://github.com/medrecord/hl7v3)
    - Example:
    ```python
    from hl7v3 import HL7v3Message
    message = "<xml>...</xml>"  # Replace with a valid HL7 v3 XML message
    parsed_message = HL7v3Message(message)
    print(parsed_message)
    ```

4. **fhirclient** 🔥
    - A Python client for FHIR (HL7 v4)
    - [GitHub](https://github.com/smart-on-fhir/client-py)
    - Example:
    ```python
    from fhirclient import client
    settings = {
        'app_id': 'my_app',
        'api_base': 'https://fhir.example.com/baseDstu2'
    }
    smart = client.FHIRClient(settings=settings)
    ```

5. **fhir.resources** 🌟
    - A Python library for FHIR (HL7 v4) resources
    - [GitHub](https://github.com/nazrulworld/fhir.resources)
    - Example:
    ```python
    from fhir.resources.patient import Patient
    patient = Patient()
    patient.id = "example"
    print(patient)
    ```

6. **fhir-parser** 📝
    - A Python library for parsing FHIR (HL7 v4) resources
    - [GitHub](https://github.com/nazrulworld/fhir-parser)
    - Example:
    ```python
    from fhir_parser import FHIR
    fhir = FHIR()
    patient = fhir.parse_resource('{"resourceType": "Patient", "id": "example"}')
    print(patient)
    ```

7. **fhirpy** 🚀
    - A Python library for working with FHIR (HL7 v4) servers
    - [GitHub](https://github.com/beda-software/fhirpy)
    - Example:
    ```python
    import fhirpy
    connection = fhirpy.FHIRClient(url='https://fhir.example.com/baseDstu2', authorization='Bearer TOKEN')
    patient = connection.resource('Patient')
    patient.id = "example"
    print(patient)
    ```

8. **hl7-fasthealthcareinteroperabilityresources-client** 🌉
    - A Python client for FHIR (HL7 v4) servers
    - [GitHub](https://github.com/Asymmetrik/hl7-fasthealthcareinteroperabilityresources-client)
    - Example:
    ```python
    from fhirclient import client
    settings = {
        'app_id': 'my_app',
        'api_base': 'https://fhir.example.com/baseDstu2'
    }
    smart = client.FHIRClient(settings=settings)
    ```

9. **ccda** 📋
    - A Python library for parsing CCDA (HL7 v3) documents
    - [GitHub](https://github.com/amida-tech/python-ccda)
    - Example:
    ```python
    from ccda import CCDA
    ccda = CCDA("<xml>...</xml>")  # Replace with a valid CCDA XML document
    print(ccda)
    ```

10. **hl7.fhir** 🌍
    - A Python library for FHIR (HL7 v4) resources
    - [GitHub](https://github.com/HL7/fhir-svn)
    - Example:
    ```python
    from hl7.fhir.r4.model import Patient
    patient = Patient()
    patient.id = "example"
    print(patient)
    ```
'''

st.markdown(markdown_text)